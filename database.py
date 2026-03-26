import mysql.connector
#Conectar a la base de datos
#Crear un objeto para la conexion
def conectar():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password= "",
        database = "empresa"
)

    if conn.is_connected():
            print("Conexion a la base de datos")
    return conn