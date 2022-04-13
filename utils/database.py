import os.path as path
import urllib.parse as up
import psycopg2

if path.exists("creds_local.py"):
    from creds_local import cred
else:
    from creds import cred


# setup creds
owner_id = int(cred.OWNER_ID)
my_db = cred.DB_NAME
my_user = cred.USER_NAME
my_host = cred.HOST_NAME
my_pass = cred.USER_PASS
my_creden = "dbname=%s user=%s host=%s password=%s" % (my_db,my_user,my_host,my_pass)
api_token = cred.API_TOKEN

# connect db
def connectdb():
    up.uses_netloc.append("postgres")
    connection = psycopg2.connect(my_creden)
    curs = connection.cursor()
    return connection, curs

# create table
def create_table(connection, curs):
    curs.execute("""SELECT EXISTS (SELECT table_name FROM information_schema.tables WHERE table_name = 'ids');""")
    connection.commit()
    doesTableExist = curs.fetchone()
    if not doesTableExist[0]:
        curs.execute("""CREATE TABLE ids (id varchar(30), notify varchar(30));""")
        curs.execute("""CREATE TABLE logs (total varchar(50);""")
    connection.commit()



