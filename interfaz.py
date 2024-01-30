from tkinter import *
from tkinter import messagebox,filedialog
import sqlite3, os

#FUENTES
fuente1=("Bahnschrift", 18)
fuente2=("Bahnschrift", 13)
fuente3=("Franklin Gothic Book", 10)
fuente4=("Rockwell Condensed", 14)
fuente5=("Segoe UI Black", 11)

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

amarillo="#FBFF6D"
verde="#75FD6D"
azul="#34B3F2"
naranja="#EF8A54"


#--------------------FUNCIONES Y METODOS DEL MENÚ----------------
def limpiar():
    mi_id.set(0)
    mi_cat.set("")
    mi_val.set(0)
    mi_des.set("")
    mi_fec.set("")

def salir():
    yes=messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
    if yes=="yes":
        root.destroy()


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

    except:
        serial=open(ruta_completa, "w")
        codigo+=1

    serial.write(str(codigo))   
    serial.close()
    return codigo


rutaBase=""
def creaBD():

    yes=messagebox.askquestion("Nueva BD", "¿Desea crear una nueva base de datos?")
    if yes=="yes":
        global rutaBase, ruta
        num=consecutivo()
        rutaBase=ruta+"\\"+"BD Gastos"+str(num)+".db"
        conexion=sqlite3.connect(rutaBase)
        cursor=conexion.cursor()
        cursor.execute('''CREATE TABLE GASTOS_PERSONALES(
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                CATERGORIA VARCHAR,
                                VALOR INTEGER,
                                DESCRIPCION VARCHAR,
                                FECHA VARCHAR
                        )''')
        conexion.close()
        print("se creó BD")
        messagebox.showinfo("Nueva BD", "Base de datos creada."+"\n"+"Nombre: BD Gastos"+str(num)+".db")




def conectaBD():
    #buscar en el equipo la base de datos a conectar, pero NO la conecta.
    global rutaBase
    rutaBase=filedialog.askopenfilename(title="Conectar Base de Datos",
                           initialdir=ruta,
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



#------------------------------------------------
#------------------VENTANA-----------------------
root=Tk()
root.title("Registro de gastos diarios")
root.config(bg=grisOscuro)
root.resizable(False,False)   

#Barra de menú
barraMenu=Menu(root)
root.config(menu=barraMenu)

#submenu de archivo
menuArchivo=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Archivo", menu=menuArchivo)
nuevaBD=menuArchivo.add_command(label="Nueva BD", command=creaBD)
conectarBD=menuArchivo.add_command(label="Conectar BD", command=conectaBD)
eliminarBD=menuArchivo.add_command(label="Eliminar BD", command=eliminaBD)
menuArchivo.add_separator()
menuArchivo.add_command(label="Salir", command=salir)

#submenu de edición
menuEdicion=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Edicion", menu=menuEdicion)
menuEdicion.add_command(label="Limpiar", command=limpiar)
menuEdicion.add_separator()
menuEdicion.add_command(label="Deshacer")
menuEdicion.add_command(label="Rehacer")
menuEdicion.add_separator()
menuEdicion.add_command(label="Cortar")
menuEdicion.add_command(label="Copiar")
menuEdicion.add_command(label="Pegar")

#submenu de exportar
menuExportar=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Exportar", menu=menuExportar)
exRegis=menuExportar.add_command(label="Exportar registro(s)")
exBD=menuExportar.add_command(label="Exportar Base de Datos")

#submenu de ayuda
menuAyuda=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)
menuAyuda.add_command(label="Acerca de", command=acerca)
menuAyuda.add_command(label="Instrucciones CRUD", command=instruccionesCRUD)
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------



#---------------------------------------------------------------------------
#----------------------------CAMPOS DE ENTRADA------------------------------
#contenedor
frameEntradas=Frame(root, bg=grisOscuro)
frameEntradas.pack(fill="both", expand="True", side="top", padx=35, pady=25)

#subtitulos
labelTitulo=Label(frameEntradas, text="Ingrese un gasto", font=fuente1, fg=blancoCalido, bg=grisOscuro)
labelTitulo.grid(row=0, column=0, columnspan=2, pady=10, padx=5)

labelId=Label(frameEntradas, text="Id: ", font=fuente2, fg=blancoCalido, bg=grisOscuro)
labelId.grid(row=1, column=0, pady=10, padx=5, sticky="w")

labelCat=Label(frameEntradas, text="Categoría: ", font=fuente2, fg=blancoCalido, bg=grisOscuro)
labelCat.grid(row=2, column=0, pady=10, padx=5, sticky="w")

labelValor=Label(frameEntradas, text="Valor: ", font=fuente2, fg=blancoCalido, bg=grisOscuro)
labelValor.grid(row=3, column=0, pady=10, padx=5, sticky="w")

labelDesc=Label(frameEntradas, text="Descripción: ", font=fuente2, fg=blancoCalido, bg=grisOscuro)
labelDesc.grid(row=4, column=0, pady=10, padx=5, sticky="w")

labelFecha=Label(frameEntradas, text="Fecha: ", font=fuente2, fg=blancoCalido, bg=grisOscuro)
labelFecha.grid(row=5, column=0, pady=10, padx=5, sticky="w")


#cuadros de texto
mi_id=IntVar()
mi_cat=StringVar()
mi_val=IntVar()
mi_des=StringVar()
mi_fec=StringVar()


entryId=Entry(frameEntradas, width=35, bg=grisClaro, font=fuente5, fg=moradoOscuro, textvariable=mi_id)
entryId.grid(row=1, column=1,)

entryCat=Entry(frameEntradas, width=35, bg=grisClaro, font=fuente5, fg=moradoOscuro, textvariable=mi_cat)
entryCat.grid(row=2, column=1,)

entryValor=Entry(frameEntradas, width=35, font=fuente5, bg=grisClaro, fg="red", textvariable=mi_val)
entryValor.grid(row=3, column=1,)

entryDesc=Entry(frameEntradas, width=35, font=fuente5, bg=grisClaro, fg=moradoOscuro, textvariable=mi_des)
entryDesc.grid(row=4, column=1)

entryFecha=Entry(frameEntradas, width=35, font=fuente5, bg=grisClaro, fg=moradoOscuro, textvariable=mi_fec)
entryFecha.grid(row=5, column=1)
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------
#--------------------------------------BOTONES CRUD--------------------------------
#Funciones y métodos
def createReg():

    try:          
        global rutaBase
        print(rutaBase)
        categoria=mi_cat.get()
        valor=mi_val.get()
        descripcion=mi_des.get()
        fecha=mi_fec.get()

        conexion=sqlite3.connect(rutaBase)
        cursor=conexion.cursor()
        
        try:
            if mi_id.get()!=0:
                confirma=messagebox.askokcancel("¡Campo ID autogenerado!", "El campo Id no se  puede asignar manualmente. Se asignará un consecutivo dependiendo de la tabla. ¿Desea crear este nuevo registro?")
                print(confirma)
                if confirma==False:
                    return
        except:
            pass
            
        cursor.execute('''INSERT INTO GASTOS_PERSONALES
                    VALUES
                       (NULL,?,?,?,?)''',
                       (categoria,valor,descripcion,fecha)
                       )
        conexion.commit()
        conexion.close()

        messagebox.showinfo("Registro creado", "Se añadió con éxito nuevo regitro")

    except sqlite3.OperationalError:
        messagebox.showerror("Base de datos no encontrada", "Aun no se ha conectado con ninguna base de datos. Ingrese al menú 'Archivo', en la opción 'Conectar BD' y seleccione una base de datos. O seleccione la opción 'Nueva BD' para crear una nueva base de datos")



def readReg():
    try:
        global rutaBase
        print(rutaBase)
        try:
            identificador=mi_id.get()
            conexion=sqlite3.connect(rutaBase)
            cursor=conexion.cursor()
            cursor.execute('SELECT * FROM GASTOS_PERSONALES WHERE Id='+str(identificador))
            registros=cursor.fetchall()
            print(registros)
            if registros==[]:
                messagebox.showinfo("Registro inexistente", "No existe un registro con Id #"+str(identificador)+"en la base de datos conectada. Intente buscar con otro Id o conecte con otra base de datos")

            for campo in registros:
                mi_cat.set(campo[1])
                mi_val.set(campo[2])
                mi_des.set(campo[3])
                mi_fec.set(campo[4])
        except:
            messagebox.showinfo("Campo Id inválido", "El campo Id debe ser numérico, y debe existir en la base datos")


    except sqlite3.OperationalError:
        messagebox.showerror("Base de datos no encontrada", "Aun no se ha conectado con ninguna base de datos. Ingrese al menú 'Archivo', en la opción 'Conectar BD' y seleccione una base de datos.")



def updateReg():
    try:
        global rutaBase
        print(rutaBase)
        try:
            identificador=mi_id.get()
        except:
            messagebox.showinfo("Campo Id inválido", "El campo Id debe ser numérico, y debe existir en la base datos")
        
        categoria=mi_cat.get()
        valor=mi_val.get()
        descripcion=mi_des.get()
        fecha=mi_fec.get()

        confirma=messagebox.askquestion("Actualizar registro","Se actualizará el registro con Id #"+str(identificador)+". ¿Está seguro de que desea cambiarlo?")
                
        if confirma=="yes":    
            conexion=sqlite3.connect(rutaBase)
            cursor=conexion.cursor()
            cursor.execute('SELECT * FROM GASTOS_PERSONALES WHERE Id='+str(identificador))
            registros=cursor.fetchone()

            if registros is None:
                messagebox.showerror("¡No existe registro!", "El registro con Id=#"+str(identificador)+" aun no existe.")

            else:
                cursor.execute('UPDATE GASTOS_PERSONALES SET CATERGORIA=?,VALOR=?,DESCRIPCION=?,FECHA=? WHERE Id=?',(categoria,valor,descripcion, fecha, identificador))
                conexion.commit()
                conexion.close()
            
                messagebox.showinfo("Registro actualizado", "El registro con Id=#"+str(identificador)+" ha sido actualizado")

    except sqlite3.OperationalError:
        messagebox.showerror("Base de datos no encontrada", "Aun no se ha conectado con ninguna base de datos. Ingrese al menú 'Archivo', en la opción 'Conectar BD' y seleccione una base de datos.")




def deleteReg():
    readReg()
    confirma=messagebox.askquestion("Eliminar registro","Si borra un registro de la BD, ya no podrá recuperarlo. ¿Desea borrar el registro?")
    if confirma=="yes":
        try:
            identificador=mi_id.get()   
            conexion=sqlite3.connect(rutaBase)
            cursor=conexion.cursor()
            cursor.execute('DELETE FROM GASTOS_PERSONALES WHERE Id='+str(identificador))
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Registro eliminado", f"El registro con Id #{identificador} ha sido eliminado")
        except:
            pass
            messagebox.showwarning("Registro No eliminado", f"No se eliminó ningun registro de la base de datos")
    

#Botones
frameBotones=Frame(root, bg=grisMedio)
frameBotones.pack(fill="both", expand="True", side="bottom", padx=15, pady=15)

botCreate=Button(frameBotones, text="CREATE", font=fuente4, bg=amarillo, width=10, command=createReg)
botCreate.grid(row=0, column=0, padx=18, pady=20, ipadx=3, ipady=2)

botRead=Button(frameBotones, text="READ", font=fuente4, bg=verde, width=10, command=readReg)
botRead.grid(row=0, column=1, padx=18, pady=20, ipadx=3, ipady=2)

botUpdate=Button(frameBotones, text="UPDATE", font=fuente4, bg=azul, width=10, command=updateReg)
botUpdate.grid(row=0, column=2, padx=18, pady=20, ipadx=3, ipady=2)

botDelete=Button(frameBotones, text="DELETE", font=fuente4, bg=naranja, width=10, command=deleteReg)
botDelete.grid(row=0, column=3, padx=18, pady=20, ipadx=3, ipady=2)
#-------------------------------------------------------------------------------


root.mainloop()