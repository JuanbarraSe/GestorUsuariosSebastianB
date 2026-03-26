from flask import Flask, render_template,url_for,request,flash,redirect, session
from database import conectar

#Crear la app del proyecto

apps = Flask(__name__)
apps.secret_key = "854759548"

#Crear ruta de ingresar
@apps.route("/")
def login():
    return render_template("login.html")

#Procesar el formulario
@apps.route("/login", methods=['POST'])
def login_form():
    #Crea variables de python, user y contraseña para recibir del formulario
    user = request.form["txtusuario"]
    password = request.form["txtcontraseña"]

    #Llamar a la base de datos
    con = conectar()
    cursor = con.cursor()
    sql= "SELECT * FROM usuarios WHERE Usuario=%s and PASSWORD=%s"
    cursor.execute(sql,(user,password))

    #Resultado de la consulta
    user = cursor.fetchone()
    if user:

        #Guarda las variables de sesion
            session["usuario"] = user[1]
            session["rol"] = user[3]
            #if rol == rol:

            if user[3] == "Administrador":
                return render_template("index.html")
            else:
                return "Bienvenido empleado"
    else: 
        flash("Usuario y contraseña incorrecta", "danger")
        return redirect(url_for("login"))
#Validar sesion en la pagina inicial
@apps.route("/inicio")
def inicio():
     if "usuario" not in session:
          return redirect(url_for("login"))
     else:
          render_template("index.html")

#Cerrar la sesion
@apps.route("/salir")
def salir():
     session.clear()
     return redirect(url_for("login"))  
if __name__ == "__main__":
    apps.run(debug=True)