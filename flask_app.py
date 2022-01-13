from flask import Flask, request, render_template, redirect, url_for
from flask.json import jsonify

app = Flask(__name__)

from db_dummy import * # import a dummy database

# ------------------------------------------------------------------------------
#
#                                   WEB
#
# ------------------------------------------------------------------------------


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html'), 200


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html'), 200

    elif request.method == 'POST':
        data = {
            'login':request.form.get('login'),
            'senha':request.form.get('password'),
            }

        if data['login'] == 'admin' \
        and data['senha'] == 'admin':
            return redirect(url_for('manager'))

        else:
            return redirect(url_for('index'))

@app.route('/manager', methods = ['GET', 'POST'])
def manager():
    if request.method == 'GET':

        dados_login = {
            index : {
                'login': item[0],
                'data': item[1],
                'ID': item [2],
                'Versão': item[3]}
            for index, item in enumerate(usuarios)}

        dados_auth = {dado[0] : dado[1] for dado in dicti}

        variavel = {
            'usuario' : {
                'titulo' : 'Painel de Usuario',
                'dados' : dados_login
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
                'dados' : dados_auth
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




# ------------------------------------------------------------------------------
#
#                       API - FRONT END
#
# ------------------------------------------------------------------------------

@app.route('/api/manager/req', methods = ['GET', 'POST'])
def api_manager_():
    if request.method == 'GET':
        return 'API TESTE', 200

    elif request.method == 'POST':
        data = request.get_json()

        if data['oper'] == 'id_auth':
            for auth in dicti:
                if data['pc_id'] == auth[0]:
                    data['auth'] = auth[1]

        if data['oper'] == 'oper':
            ...
 
        if data['oper'] == 'duv_fin':
            ...
 
        if data['oper'] == 'duv_ret':
            ...
 
        if data['oper'] == 'duv_tec':
            ...
 
        data['conclu'] = 'OK'

        return data, 200

    else:
        return '', 404

@app.route('/api/manager/auth', methods = ['GET', 'POST'])
def api_manager_auth():
    if request.method == 'GET':
        return 'API TESTE', 200

    elif request.method == 'POST':
        data = request.get_json()

        for auth in dicti:
            if data['pc_id'] == auth[0]:
                auth[1] = data['auth']

        data['conclu'] = 'OK'

        return data, 200

    else:
        return '', 404

@app.route('/api/manager/edit_data', methods = ['GET', 'POST'])
def api_manager_edit_data():
    if request.method == 'GET':
        return 'API TESTE', 200

    elif request.method == 'POST':
        data = request.get_json()

        if data['oper'] == 'oper':
            ...

        elif data['oper'] == 'duv_fin':
            ...

        elif data['oper'] == 'duv_ret':
            ...

        elif data['oper'] == 'duv_tec':
            ...

        data['conclu'] = 'OK'

        return data, 200

    else:
        return '', 404



if __name__ == '__main__':
    app.run(debug=True)