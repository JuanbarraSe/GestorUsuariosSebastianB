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

     cursor.execute("SELECT * FROM empleados")
     empleados = cursor.fetchall()

     con.close()
     cursor.close()

     return render_template("index.html", user=lista, empleados=empleados)

#Cerrar la sesion
@apps.route("/salir")
def salir():
     session.clear()
     return redirect(url_for("login"))  

#Crear una ruta para eliminar los empleados tipos usuarios
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

#Crear una ruta para registrar los usuarios 
@apps.route("/registro")
def registro():
    return render_template("registrarusu.html")

@apps.route("/registrar", methods=['POST'])
def registrarUsuario():
     if "usuario" not in session:
          return redirect(url_for("login"))
     
     usuario = request.form["txtusuario"]
     password = request.form["txtcontraseña"]
     rol = request.form["txtrol"]
     documento = request.form["txtdocumento"]

     con = conectar()
     cursor = con.cursor()

     sql = "INSERT INTO usuarios (Usuario, PASSWORD, rol, DocumentoEmplea) VALUES (%s,%s,%s,%s)"
     cursor.execute(sql,(usuario, password, rol, documento))
     con.commit()

     cursor.close()
     con.close() 

     flash("Usuario registrado correctamente")
     return redirect(url_for("inicio"))


#Registrar un empleado
@apps.route("/registroemple", methods=["POST"])
def registroempleado():
    Documento = request.form["txtdocumento"]
    Nombre = request.form["txtnombre"]
    Apellido = request.form["txtapellido"]
    Cargo = request.form["txtcargo"]
    HorasExtras = int(request.form["txthorasExtras"])
    Bonificacion = float(request.form["txtbonificacion"])
    NombreDepartamento = (request.form["txtdepartamento"])

    def calcularSalarioBase():
        if Cargo.lower() == "gerente":
            return 5000000
        elif Cargo.lower() == "administrador":
            return 3500000
        elif Cargo.lower() == "contador":
            return 2800000
        else: 
            return 1800000 
        
    Salabase = calcularSalarioBase()
    TotalExtras = HorasExtras * 3000
    Salariobru = Salabase + TotalExtras + Bonificacion
    Salud = Salariobru * 0.04
    Pension = Salariobru * 0.04
    SalarioNeto = Salariobru - Salud - Pension

    con = conectar()
    cursor= con.cursor()

    sqlDep = "SELECT idArea FROM departamentos WHERE NombreDepartamento=%s"
    cursor.execute(sqlDep,(NombreDepartamento,))
    Resultado = cursor.fetchone()

    if Resultado:
        Nombredepar = Resultado[0]
        sql = "INSERT INTO empleados (DocumentoEmplea, NombreEmplea, ApellidoEmplea, Cargo, HorasExtras, Bonificacion, SalarioB, Salud, Pension, SalarioNeto, idDepa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (Documento, Nombre, Apellido, Cargo, HorasExtras, Bonificacion, Salariobru, Salud, Pension, SalarioNeto, Nombredepar) 
        cursor.execute(sql,datos)
        con.commit()

        print("Empleado guardado en la base de datos")
    else:
        print("El departamento no existe")
     
    cursor.close()
    con.close()
    return redirect(url_for("inicio"))

#Eliminar empleado
@apps.route("/eliminarempleado")
def eliminarempleado():
    if "usuario" not in session:
        return redirect(url_for("login"))
    
    con = conectar()
    cursor = con.cursor()

    #Eliminar el empleado
    sql = "DELETE * FROM empleados"
    cursor.execute(sql)

    empleado = cursor.fetchone()
    if empleado:
        
    flash("Empleado eliminado")

    cursor.close()
    con.close()
    return redirect(url_for("inicio"))

if __name__ == "__main__":
    apps.run(debug=True)