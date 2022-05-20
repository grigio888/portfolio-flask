#imports built-in
import os
import peewee

import sys
sys.path.append('../')


#imports third party
from datetime import timedelta
from flask import Flask, flash, jsonify, request, send_file, render_template, make_response, redirect, url_for, session
from flask_pydantic_spec import FlaskPydanticSpec
from api.persistent.methods import duv_disp



#import local
from api.tools.encrypt import encoder_token



# initialiazing the app
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.permanent_session_lifetime = timedelta(minutes=30)
app.secret_key = os.urandom(24)

spec = FlaskPydanticSpec('flask', title='update.client')
spec.register(app)



# import db models
db = peewee.SqliteDatabase('persistent/db.sqlite3')
from api.persistent.models import *


# ------------------------------------------------------------------------------
#
#                                   WEB
#
# ------------------------------------------------------------------------------


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index_v2.html'), 200


@app.route('/login/request', methods = ['POST'])
def login_request():
    if request.method == 'POST':
        data = request.get_json()

        try:
            user = User.get(User.username == data['username'])
            if user.password == data['password']:
                session['username'] = user.username
                session['access_level'] = user.access_level
                return jsonify({
                    "status": "ok",
                    "message" : "Login concluido"
                    }), 200
            else:
                return jsonify({
                    "status": "error",
                    "message": "Senha incorreta"
                    }), 200
        except peewee.DoesNotExist:
            return jsonify({
                "status": "error",
                "message": "Usuario não existe"
                }), 200

    else:
        return jsonify({
            "status": "error",
            "message": "Metodo incorreto"
            }), 200
            

@app.route('/logout')
def logout():
    if request.method == 'GET':
        session.pop('username', None)
        return redirect(url_for('index'))


@app.route('/manager', methods = ['GET'])
def manager():
    if request.method == 'GET':
        if 'username' in session:

            login_clientes = sorted([(app.login, app.pc_id, app.date, app.ver) for app in AppUser.select()], key=lambda x: x[2])

            dados_login = {
                index : {
                    'login': item[0],
                    'data': item[2],
                    'ID': item [1],
                    'Versão': item[3]}
                for index, item in enumerate(login_clientes)}

            pcs_auth = [(auth.pc_id, auth.auth) for auth in Authorization.select()]

            dados_auth = {dado[0] : dado[1] for dado in pcs_auth}

            variavel = {
                'usuario' : {
                    'titulo' : 'Painel de Usuario',
                    'dados' : dados_login,
                },
                'contexto' : {
                    'titulo' : 'Painel de Contexto',
                    'texto' : [
                        'Exemplo de painel.',
                        'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
                    ],
                },
                'login' : {
                    'titulo' : 'Painel de Login',
                    'dados' : dados_auth,
                },
                'config' : {
                    'titulo' : 'Painel de Configuração',
                    'texto' : [
                        'Exemplo de painel.',
                        'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
                    ],
                }
            }

            return render_template('manager.html', data = variavel), 200
        else:
            return redirect(url_for('index'))






# ------------------------------------------------------------------------------
#
#                       API - FRONT END
#
# ------------------------------------------------------------------------------

@app.route('/api/manager/context/get')
def api_manager_context_get():
    if session['access_level'] < 5:
        return jsonify({
            "status": "error",
            "message": "Usuario sem acesso"
            }), 200

    else:
        methods = {
            'a_oper' : 'Operações',
            'b_duv' : 'Dúvidas',
            'c_fin' : 'Finalizações',
        }

        return jsonify({
            "status": "ok",
            "message": "ok",
            "avaliable": methods,
        }), 200


@app.route('/api/manager/context/<method>')
def api_manager_context_options(method):
    if session['access_level'] < 5:
        return jsonify({
            "status": "error",
            "message": "Usuario sem acesso"
            }), 200

    else:
        if method == 'a_oper':
            from api.persistent.methods import oper_disp
            opcoes = {
                'a_id_op' : 'ID', 
                'b_oper' : 'Operação', 
                'c_suboper' : 'Sub-Operação'
            }
            saida = oper_disp()

        elif method == 'b_duv':
            from api.persistent.methods import duv_disp
            opcoes = {
                'a_id_duv' : 'ID',
                'b_titulo' : 'Título',
                'c_corpo' : 'Corpo',
                'd_finalizacao' : 'Finalização',
            }
            saida = duv_disp('All')

        elif method == 'c_fin':
            from api.persistent.methods import final_disp
            opcoes = {
                'a_section' : 'Seção',
                'b_solution' : 'Solução',
                'c_fluxo' : 'Fluxo',
                'd_fechar_chamado' : 'Fechar Chamado',
                'e_finalização' : 'Finalização',
            }
            saida = final_disp('All')

        else:
            return jsonify({
                "status": "error",
                "message": "Metodo incorreto",
                }), 200

        return jsonify({
            "status": "ok",
            "message": "ok",
            "avaliable": opcoes,
            "data" : saida,
        }), 200


@app.route('/api/manager/auth/req/', methods = ['POST'])
def api_manager_auth_req():
    if request.method == 'POST':
        """
        Requested by the Manager WebPage.

        Used to display who is using, when and where.
        """
        data = request.get_json()

        if session['access_level'] < 5:
            return jsonify({
                "status": "error",
                "message": "Usuario sem acesso"
                }), 200

        else:
            try:                  
                auth = Authorization.get(Authorization.pc_id == data['pc_id'])
                
                return jsonify({
                    "status" : "ok",
                    "message" : "",
                    "pc_id" : data['pc_id'],
                    "auth" : auth.auth
                }), 200

            except peewee.DoesNotExist:
                return jsonify({
                    "status": "error",
                    "message": "Usuario não existe"
                    }), 200
    else:
        return '', 404

@app.route('/api/manager/auth/post/', methods = ['POST'])
def api_manager_auth_post():
    if request.method == 'POST':
        """
        Requested by the Manager WebPage.

        Used to change the authorized status for a PC.
        """
        data = request.get_json()

        if session['access_level'] < 5:
            return jsonify({
                "status": "error",
                "message": "Usuario sem acesso"
                }), 200
        
        else:
            pc = Authorization.get(Authorization.pc_id == data['pc_id'])
            pc.auth = data['auth']
            pc.save()

            return data, 200

    else:
        return '', 404







# ------------------------------------------------------------------------------
#
#                       API - GERENCIADOR DE RELATORIOS
#
# ------------------------------------------------------------------------------

@app.route('/api/auth', methods = ['POST'])
def api_auth():
    """
    Requested by the App - Gerador de Relatório.

    Route responsible for authorize the app at the startup routine.
    """
    if request.method == 'POST':
        data = request.get_json()

        if len(data['pc_id']) == 36:
            try:
                pc_id = Authorization.get(Authorization.pc_id == data['pc_id'])

                if pc_id.auth == 1:
                    auth = encoder_token('encript', data['pc_id'])
                    return make_response({'auth':auth}), 200

                else:
                    return make_response({'auth':False}), 404

            except peewee.DoesNotExist:
                Authorization.create(pc_id = data['pc_id'], auth = 0)
                return make_response({'auth':False}), 404

        return 'Acesso Negado', 403

    else:
        return '', 404

@app.route('/api/login', methods = ['GET', 'POST'])
def api_login():
    """
    Requested by the App - Gerador de Relatório.

    Route responsible to emit a autorized token, for the person who logged, to
    access other routes.

    Also feed who is currently logged.
    https://grigio.pythonanywhere.com/cliente/login
    """
    if request.method == 'POST':
        data = request.get_json()

        try:
            user = AppUser.get(AppUser.username == data['login'])
            user.date = data['date']
            user.ver = data['ver']
            user.save()

        except peewee.DoesNotExist:
            AppUser.create(username = data['login'], pc_id = data['pc_id'], date = data['date'], ver = data['ver'])


        encriptado = encoder_token('encript', data['pc_id'])

        return make_response({'token':encriptado}), 200

    else:
        return '', 404

@app.route('/api/oper', methods = ['GET', 'POST'])
def api_oper():
    """
    Requested by the App - Gerador de Relatório.

    Route responsible to feed the App with content, if the token is valid.
    """
    if request.method == 'POST':
        data = request.get_json()

        auth = encoder_token('decript', data['token'])

        try:
            user = AppUser.get(AppUser.pc_id == auth)

            if data['oper'] == 'oper':

                from api.persistent.methods import oper_disp

                operacoes = oper_disp(True)

                return make_response(jsonify(operacoes)), 200

            else:
                try:
                    from api.persistent.methods import duv_disp
                    oper = duv_disp(data['oper'])
                    return make_response(jsonify({data["oper"]:oper})), 200

                except peewee.DoesNotExist:
                    return jsonify({
                        "status": "error",
                        "message": "Operacao não existe"
                        }), 200

        except peewee.DoesNotExist:
            return jsonify({
                "status": "error",
                "message": "Usuario não existe"
                }), 200

    else:
        return '', 404

@app.route('/api/oper/methods', methods = ['POST'])
def api_oper_methods():
    if request.method == 'POST':
        """
        Requested by the App - Gerador de Relatório.

        Route responsible to feed the App with closing arguments, if the token is valid.

        Input:
        {
            'oper':'method',
            'method' : 'targeted_method',
            'token': xxxxxx
        }

        Output:
        'method' : {
            'solucao1' : {
                'fluxo' : '0.00',
                'fechar_chamado' : True,
                'finalizacao' : 'finalizacao'
            },
            'solucao2': {
                'fluxo' : '0.0',
                'fechar_chamado' : True,
                'finalizacao' : 'finalizacao'
            }
        }
        """

        data = request.get_json()

        auth = encoder_token('decript', data['token'])

        try:
            user = AppUser.get(AppUser.pc_id == auth)

            if data['oper'] == 'method':
                try:
                    tabela = {}
                    for fin in Finalization.select().where(Finalization.section == data['method']):
                        if tabela.get(fin.section) is None:
                            tabela.update({fin.section: {fin.solution_n : {'fluxo' : fin.fluxo, 'fechar_chamado' : fin.fechar_chamado, 'finalizacao' : fin.finalizacao}}})
                        else:
                            tabela[fin.section].update({fin.solution_n : {'fluxo' : fin.fluxo, 'fechar_chamado' : fin.fechar_chamado, 'finalizacao' : fin.finalizacao}})

                    return make_response(jsonify(tabela[data['method']])), 200

                except peewee.DoesNotExist:
                    return jsonify({
                        "status": "error",
                        "message": "Operacao não existe"
                        }), 200

        except peewee.DoesNotExist:
            return '', 403

    else:
        return '', 404




if __name__ == '__main__':  
    app.run(debug=True)