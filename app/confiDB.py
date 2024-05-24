import mysql.connector
import os
from dotenv import load_dotenv


load_dotenv()
host = os.getenv('MYSQL_HOST')
user = os.getenv('MYSQL_USER')
port = os.getenv('MYSQL_PORT')
passwd = os.getenv('MYSQL_PASSWORD')
database = os.getenv('MYSQL_DB')

def coneccionBD():
    mydb = mysql.connector.connect(
        host = host,
        user = user,
        port = port,
        passwd = passwd,
        database = database
    )

    if mydb:
        print ("Conexion exitosa")
    else:
        print ("Error en la conexion a BD")
    return mydb