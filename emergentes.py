import sqlite3, os
from tkinter import *
from tkinter import messagebox,filedialog


#COLORES
grisOscuro="#333147"
grisMedio="#B8B5FF"
grisClaro="#D4D8FA"
blancoHueso="#F4F5CD"
blancoFrio="#D4FFF0"
blancoCalido="#FEEAEA"
moradoOscuro="#521893"
moradoMedio="#6645A9"
moradoClaro="#9E47FF"


global ruta_completa
ruta = r"D:\\NUEVO PORTATAIL\\PROGRAMACIÓN\\PYTHON\\EJERCICIO 18 bases de datos\\CRUD"
nombre = "consecutivo.txt"
ruta_completa = os.path.join(ruta,nombre)


def consecutivo():
    global ruta_completa
    codigo=0

    try:
        serial=open(ruta_completa, "r")
        codigo=int(serial.read())+1
        serial.close()
        serial=open(ruta_completa, "w")
        print("try abrió de nuevo archivo para escribir")

    except:
        serial=open(ruta_completa, "w")
        codigo+=1

    serial.write(str(codigo))   
    serial.close()
    return codigo



def creaBD():
    #seleccionar carpeta donde se creará la base de datos
    #ruta=filedialog.askdirectory()
    yes=messagebox.askquestion("Nueva BD", "¿Desea crear una nueva base de datos?")

    if yes=="yes":
        num=consecutivo()
        conexion=sqlite3.connect("BD Gastos"+str(num)+".db")
        cursor=conexion.cursor()
        cursor.execute('''
                            CREATE TABLE GASTOS_PERSONALES(
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                CATERGORIA VARCHAR,
                                VALOR INTEGER,
                                DESCRIPCION INTEGER,
                                FECHA INTERGER
                                )''')
        conexion.close()
        print("se creó BD")
        messagebox.showinfo("Nueva BD", "Base de datos creada."+"\n"+"Nombre: BD Gastos"+str(num)+".db")




rutaBase=""
def conectaBD():
    #buscar en el equipo la base de datos a conectar
    global rutaBase
    rutaBase=filedialog.askopenfilename(title="Conectar Base de Datos",
                           initialdir=ruta_completa,
                           filetypes=(
                                    ("Archivos de Bases de datos", "*.db"),
                                    ("Todos los archivos","*.*")
                                    ))
    print(rutaBase)


def eliminaBD():
    #mensaje emergente para advertir sobre borrar base de datos
    ok=messagebox.askokcancel("Eliminar Base de Datos",
                           "Si elimina una base de datos, ya no podrá recuperar la información.\n\
                           ¿Desea continuar?")
    
    if ok==True:
    #buscar en el equipo la base de datos a borrar
        filedialog.askopenfilename(title="Eliminar Base de Datos",
                           initialdir="C:",
                           filetypes=(
                                    ("Archivos de Bases de datos", "*.db"),
                                    ("Todos los archivos","*.*")
                                    ))
   

def acerca():
    texto="La presente aplicación utiliza cuatro (4) campos para registrar y actualizar información en bases de datos sobre gastos personales. Podrá guardar la información en una base de datos o exportarla a un archivo de texto."
    messagebox.showinfo("Sobre CRUD",texto)


def instruccionesCRUD():
    texto="CRUD es el acrónimo de Create (Crear), Read (Leer), Update (Actualizar) y Delete (Borrar). Este concepto se utiliza para describir las cuatro operaciones básicas que pueden realizarse en la mayoría de las bases de datos y sistemas de gestión de información."
    messagebox.showinfo("Sobre CRUD",texto)