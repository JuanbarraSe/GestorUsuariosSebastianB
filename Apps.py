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
                return redirect(url_for('inicio'))
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
     
     con = conectar()
     cursor = con.cursor()

     cursor.execute("SELECT * FROM usuarios")
     lista = cursor.fetchall()

     con.close()
     cursor.close()

     return render_template("index.html", user=lista)

#Cerrar la sesion
@apps.route("/salir")
def salir():
     session.clear()
     return redirect(url_for("login"))  

#Crear una ruta para eliminar los usuarios tipos usuarios
@apps.route("/Eliminar/<int:id>")
def eliminarusu(id):
    if "usuario" not in session:
        return redirect(url_for("login"))
    
    con = conectar()
    cursor = con.cursor()

    #Buscar el usuario
    sql = "SELECT rol FROM usuarios WHERE idUsuario=%s"
    cursor.execute(sql,(id,))

    usuario = cursor.fetchone()

    #Validar el rol del usuario
    if usuario:
         rol = usuario[0]

         if rol == "Administrador":
              flash("No se puede eliminar el administrador")

         else:
              cursor.execute("DELETE FROM usuarios WHERE idUsuario=%s",(id,))
              con.commit()
              flash("Empleado eliminado")

    cursor.close()
    con.close()
    return redirect(url_for("inicio"))
if __name__ == "__main__":
    apps.run(debug=True)