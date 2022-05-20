import peewee
import datetime

db = peewee.SqliteDatabase('persistent/db.sqlite3')

# initialiazing BaseModel
class BaseModel(peewee.Model):
    class Meta:
        database = db


# User model for user authorized to enter the manager page
class User(BaseModel):
    username = peewee.CharField(unique=True)
    password = peewee.CharField()
    access_level = peewee.IntegerField(default=0)
    last_login = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        table_name = 'user'







# Models about the App
# Authorization Model
class AppUser(BaseModel):
    login = peewee.CharField()
    pc_id = peewee.CharField()
    date = peewee.CharField()
    ver = peewee.CharField()

    class Meta:
        table_name = 'app_user'

class Authorization(BaseModel):
    pc_id = peewee.CharField()
    auth = peewee.IntegerField()

    class Meta:
        table_name = 'authorization'





# creating operations
class Operation(BaseModel):
    id_o = peewee.CharField()
    oper = peewee.CharField()
    suboper = peewee.CharField()

    class Meta:
        table_name = 'operacoes'


# creating duv_table
class DuvTable(BaseModel):
    id_duv = peewee.CharField()
    titulo = peewee.CharField()
    corpo = peewee.CharField()
    finalizacao = peewee.CharField()

    class Meta:
        table_name = 'duv_table'

# Finalizations Table
class Finalization(BaseModel):
    section = peewee.CharField()
    solution_n = peewee.CharField()
    fluxo = peewee.CharField()
    fechar_chamado = peewee.BooleanField()
    finalizacao = peewee.CharField()


if __name__ == '__main__':
    for item in [User, AppUser, Authorization, Operation, DuvTable, Finalization]:
        try: item.create_table()
        except peewee.OperationalError: print(f"Tabela {item} ja existe!")
