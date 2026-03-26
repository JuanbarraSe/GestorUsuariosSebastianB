from flask import Flask, render_template, request
from database import conectar

#Crear app del proyecto

app = Flask(__name__)

#Crear la ruta principal

@app.route("/")
def inicio():
    return render_template("index.html")
#Crear la ruta para registar usuarios

@app.route('/guardar_usuario', methods=['POST'])
def guardar_usuario():
    usuario = request.form['txtusuario']
    password = request.form['txtcontraseña']
    rolusu =request.form['txtrol']
    documento = request.form['txtdocumento']

    #Llamar a la conexion

    con = conectar()
    cursor = con.cursor()
    #Para saber si el usuario existe o no
    sql = "SELECT * FROM usuarios WHERE DocumentoEmplea=%s"
    cursor.execute(sql,(documento,))
    resultado = cursor.fetchone()
    if resultado:
        return "Usuario ya registrado"
    else:
        "Usuario no existe"
    #Crear el sql
    #Para registar un usuario
        sql = "INSERT INTO usuarios (Usuario, PASSWORD, rol, DocumentoEmplea)VALUES(%s,%s,%s,%s)"
        #Ejecutar
        cursor.execute(sql, (usuario, password, rolusu, documento))
        con.commit()
        return "Usuario guardado"
if __name__ == "__main__":
    app.run(debug=True)