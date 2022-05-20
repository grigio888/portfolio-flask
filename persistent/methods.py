import sys
sys.path.insert(0, './')

import peewee

from persistent.models import *

"""
creating a table

for item in [User]:
    try: item.create_table()
    except peewee.OperationalError: print(f"Tabela {item} ja existe!")



 creating a data
 User.create(username='admin', password='admin', access_level=0)

 reading a data
 User.select() -> read all
 User.get(User.username == user) -> read one

 updating a data
 user = User.get(User.username == 'admin')
 user.password = 'admin2'
 user.save()

 deleting a data
 user = User.get(User.username == 'admin')
 user.delete_instance()



 FK demo
 pc_id = '3D6AE900-2148-11EA-B3AD-02C11E892500'
 pedido = (Pedido.select().join(Cliente, on=(Pedido.cliente == Cliente.identidade)).where(Cliente.nome == cliente))
 for p in pedido:
     print(p.criado_em,p.produto.nome,p.quantidade, p.codigo)
"""


def oper_disp(serialized = False):
    oper = Operation.select()

    if not serialized:
        return [(item.id_o, item.oper, item.suboper) for item in oper]
    if serialized:
        operacoes = {}

        for item in [(item.id_o, item.oper, item.suboper) for item in oper]:
            if operacoes.get(item[0]) == None:
                operacoes[item[0]] = {}

            if operacoes[item[0]].get('nome') == None:
                operacoes[item[0]]['nome'] = item[1]
                operacoes[item[0]]['sub'] = []
                operacoes[item[0]]['sub'].append(item[2])
            else:
                operacoes[item[0]]['sub'].append(item[2])

        for item in operacoes.keys():
            operacoes[item]['sub'] = {f'{index+1:02d}':item for index, item in enumerate(sorted(operacoes[item]['sub']))}
        
        return operacoes



def duv_disp(table = 'All', serialized = False):
    if table == 'All':
        duvtable = DuvTable.select()
    elif table in {item.id_duv for item in DuvTable.select()}:
        duvtable = DuvTable.select().where(DuvTable.id_duv == table)

    if not serialized:
        return [(duv.id_duv, duv.titulo, duv.corpo, duv.finalizacao) for duv in duvtable]
    if serialized:
        return {item: {duv.titulo : (duv.corpo, duv.finalizacao) for duv in duvtable if duv.id_duv == item} for item in {set.id_duv for set in duvtable}}



def final_disp(table = 'All', serialized = False):
    if table == 'All':
        final = Finalization.select()
    elif table in {item.section for item in Finalization.select()}:
        final = Finalization.select().where(Finalization.section == table)

    if not serialized:
        return [(item.section, item.solution_n, item.fluxo, item.fechar_chamado, item.finalizacao) for item in final]
    if serialized:
        return {item.section: item.finalizacao for item in final}