from tkinter import *
from tkinter import ttk
from Centro_Salud import*
from ficha import*
from Paciente import*
from Profesional import*
from Alerta import*
from functools import partial
#from Pillow import ImageTk, Image

#LISTAS DE ELEMENTOS
alerta=Alerta(1,"los sauces",1,"pendiente",22,16)
pte=Paciente(1,"n","h",123)
fch=Ficha_Medica("","","",0,0)
centro=[]
lista_paciente=[]
profesional=[]


root=Tk()
root.geometry("1150x700")
root.title("Centro de control")

#Declarando Frames
inicio = Frame(root, bg="#CEE1F2")
inicio.pack(expand=True, fill='both')

frm_Paciente = Frame(root, bg="Gray")
frm_Paciente.pack(expand=True, fill='both')

#Frame que contiene a la tabla PENDIENTES
alertas = Frame(inicio)
lbl_tablaPendientes = Label(inicio, text="Alertas Pendientes", font=("Verdana",13), bg="#CEE1F2")
lbl_tablaPendientes.place(x=610,y=10)
lbl_tablaPendientes.config()
alertas.config(height=400,width=400)
alertas.place(x=300,y=60)

#Frame que contiene a la tabla DESPACHADOS
despachado = Frame(inicio)
despachado.config(height=400,width=400)
lbl_tablaDespachados = Label(inicio, text="Alertas Despachadas", font=("Verdana",13), bg="#CEE1F2")
lbl_tablaDespachados.place(x=610,y=300)
despachado.place(x=300,y=350)



#Frame Botonera
botonera = Frame(inicio)
botonera.config(height=649,width=250,bg="#41576B")
botonera.pack(fill='y',side="left")

#variables paciente
nombreP=StringVar(value="")
apellidoP=StringVar(value="")
numeroP=StringVar(value="")
rutP=IntVar(value=0)

def paciente(nombreP,apellidoP,numerop,rutP):
    #variables pacientes
    

    #variables ficha medica

    direccionF=StringVar()
    latitudF=IntVar()
    longitudF=IntVar()

    paciente = Toplevel()
    paciente.title("Ficha Medica")
    paciente.geometry("310x420")
    paciente.config(bg="#41576B")

    lbl_pac=Label(paciente,      text="Paciente",font=("Verdena",11))
    lbl_pac.config(bg="#41576B",fg="white")
    lbl_nombre=Label(paciente,   text="Nombre :",bg="#41576B",fg="white")
    lbl_apellido=Label(paciente, text="Apellido :",bg="#41576B",fg="white")
    lbl_numero=Label(paciente,   text="Numero :",bg="#41576B",fg="white")
    lbl_rut=Label(paciente,      text="Rut :",bg="#41576B",fg="white")

    entry_nombre=Entry(paciente,textvariable=nombreP)
    entry_apellido=Entry(paciente,textvariable=apellidoP)
    entry_numero=Entry(paciente,textvariable=numeroP)
    entry_rut=Entry(paciente,textvariable=rutP)

    #Campos PACIENTE
    lbl_pac.grid(row=1,column=1, padx=5, pady=5, sticky=W)

    lbl_rut.grid(row=2,column=0, padx=5, pady=5, sticky=E)
    entry_rut.grid(row=2,column=1, padx=5, pady=5,sticky=W)

    lbl_nombre.grid(row=3,column=0, padx=5, pady=5, sticky=E)
    entry_nombre.grid(row=3,column=1, padx=5, pady=5,sticky=W)

    lbl_apellido.grid(row=4,column=0, padx=5, pady=5, sticky=E)
    entry_apellido.grid(row=4,column=1, padx=5, pady=5,sticky=W)

    lbl_numero.grid(row=5,column=0, padx=5, pady=5, sticky=E)
    entry_numero.grid(row=5,column=1, padx=5, pady=5,sticky=W)


    #Campos FICHA

    lbl_ficha=Label(paciente,      text="Ficha medica",bg="#41576B",fg="white",font=("Verdena",11))
    lbl_direccion=Label(paciente, text="Direccion :",bg="#41576B",fg="white")
    lbl_latitud=Label(paciente,   text="Latitud :",bg="#41576B",fg="white")
    lbl_longitud=Label(paciente,  text="Longitud :",bg="#41576B",fg="white")

    entry_direccion=Entry(paciente,textvariable=direccionF)
    entry_latitud=Entry(paciente,textvariable=latitudF)
    entry_longitud=Entry(paciente,textvariable=longitudF)

    lbl_ficha.grid(row=6,column=1, padx=5, pady=5, sticky=W)

    lbl_direccion.grid(row=7,column=0, padx=5, pady=5, sticky=E)
    entry_direccion.grid(row=7,column=1, padx=5, pady=5,sticky=W)

    lbl_latitud.grid(row=8,column=0, padx=5, pady=5, sticky=E)
    entry_latitud.grid(row=8,column=1, padx=5, pady=5,sticky=W)

    lbl_longitud.grid(row=9,column=0, padx=5, pady=5, sticky=E)
    entry_longitud.grid(row=9,column=1, padx=5, pady=5,sticky=W)

    #BOTONES
    
    
    btn_agregar=Button(paciente,text="Agregar",font=("Verdana",10),height=2,width=6, bg="#74C69D",command=partial(guardarPaciente,rutP,nombreP,apellidoP,numeroP,direccionF)).place(x=20,y=300)
    btn_editar=Button(paciente,text="Editar",font=("Verdana",10),height=2,width=6,command=partial(editarPaciente,rutP,nombreP,apellidoP,numeroP,direccionF)).place(x=90,y=300)
    btn_buscar=Button(paciente,text="Buscar",font=("Verdana",10),height=2,width=6,command=partial(buscarPaciente,rutP,paciente)).place(x=160,y=300)
    btn_eliminar=Button(paciente,text="Eliminar",font=("Verdana",10),height=2,width=6,bg="#9D0208").place(x=230,y=300)
    

def medico():
    #variables MEDICO
    nombreM=StringVar()
    apellidoM=StringVar()
    numeroM=IntVar()
    rutM=IntVar()
    especialidad=StringVar()

    medico = Toplevel()
    medico.title("Agregar Medico")
    medico.geometry("310x420")
    medico.config(bg="#41576B")

    lbl_med=Label(medico,          text="Medico",bg="#41576B",fg="white",font=("Verdena",11))
    lbl_nombre=Label(medico,       text="Nombre :",bg="#41576B",fg="white")
    lbl_apellido=Label(medico,     text="Apellido :",bg="#41576B",fg="white")
    lbl_numero=Label(medico,       text="Numero :",bg="#41576B",fg="white")
    lbl_rut=Label(medico,          text="Rut :",bg="#41576B",fg="white")
    lbl_especialidad=Label(medico, text="Especialidad :",bg="#41576B",fg="white")

    entry_nombre=Entry(medico,textvariable=nombreM)
    entry_apellido=Entry(medico,textvariable=apellidoM)
    entry_numero=Entry(medico,textvariable=numeroM)
    entry_rut=Entry(medico,textvariable=rutM)
    entry_especialidad=Entry(medico,textvariable=especialidad)

    #Campos medico
    lbl_med.grid(row=1,column=1, padx=5, pady=5, sticky=W)

    lbl_rut.grid(row=2,column=0, padx=5, pady=5, sticky=E)
    entry_rut.grid(row=2,column=1, padx=5, pady=5,sticky=W)

    lbl_nombre.grid(row=3,column=0, padx=5, pady=5, sticky=E)
    entry_nombre.grid(row=3,column=1, padx=5, pady=5,sticky=W)

    lbl_apellido.grid(row=4,column=0, padx=5, pady=5, sticky=E)
    entry_apellido.grid(row=4,column=1, padx=5, pady=5,sticky=W)

    lbl_numero.grid(row=5,column=0, padx=5, pady=5, sticky=E)
    entry_numero.grid(row=5,column=1, padx=5, pady=5,sticky=W)


    lbl_especialidad.grid(row=6,column=0, padx=5, pady=5, sticky=E)
    entry_especialidad.grid(row=6,column=1, padx=5, pady=5,sticky=W)

    #BOTONES

    btn_agregar=Button(medico,text="Agregar",font=("Verdana",10),height=2,width=6,bg="#74C69D").place(x=20,y=300)
    btn_editar=Button(medico,text="Editar",font=("Verdana",10),height=2,width=6).place(x=90,y=300)
    btn_buscar=Button(medico,text="Buscar",font=("Verdana",10),height=2,width=6).place(x=160,y=300)
    btn_eliminar=Button(medico,text="Eliminar",font=("Verdana",10),height=2,width=6,bg="#9D0208").place(x=230,y=300)

def estadoAlerta():
    #variables pacientes
    nombreP=StringVar()
    apellidoP=StringVar()
    numeroP=IntVar()
    rutP=IntVar()

    #variables ficha medica

    nombreMed=StringVar()
    apellidoMed=StringVar()
    rutMed=IntVar()
    especialidad=StringVar()

    #variables Alerta

    idAlerta=StringVar()
    prioridad=IntVar()
    estado=IntVar()
    observaciones=StringVar()



    estadoAlerta = Toplevel()
    estadoAlerta.title("Estado de Alerta")
    estadoAlerta.geometry("700x420")
    estadoAlerta.config(bg="#41576B")

    #Campos PACIENTE

    lbl_pac=Label(estadoAlerta,      text="Paciente",font=("Verdena",11))
    lbl_pac.config(bg="#41576B",fg="white")
    lbl_nombre=Label(estadoAlerta,   text="Nombre :",bg="#41576B",fg="white")
    lbl_apellido=Label(estadoAlerta, text="Apellido :",bg="#41576B",fg="white")
    lbl_numero=Label(estadoAlerta,   text="Numero :",bg="#41576B",fg="white")
    lbl_rut=Label(estadoAlerta,      text="Rut :",bg="#41576B",fg="white")

    entry_nombre=Entry(estadoAlerta,textvariable=nombreP)
    entry_apellido=Entry(estadoAlerta,textvariable=apellidoP)
    entry_numero=Entry(estadoAlerta,textvariable=numeroP)
    entry_rut=Entry(estadoAlerta,textvariable=rutP)

    #Posicion campos PACIENTE
    lbl_pac.grid(row=1,column=1, padx=5, pady=5, sticky=W)

    lbl_rut.grid(row=2,column=0, padx=5, pady=5, sticky=E)
    entry_rut.grid(row=2,column=1, padx=5, pady=5,sticky=W)

    lbl_nombre.grid(row=3,column=0, padx=5, pady=5, sticky=E)
    entry_nombre.grid(row=3,column=1, padx=5, pady=5,sticky=W)

    lbl_apellido.grid(row=4,column=0, padx=5, pady=5, sticky=E)
    entry_apellido.grid(row=4,column=1, padx=5, pady=5,sticky=W)

    lbl_numero.grid(row=5,column=0, padx=5, pady=5, sticky=E)
    entry_numero.grid(row=5,column=1, padx=5, pady=5,sticky=W)


    #Campos MEDICO

    lbl_ficha=Label(estadoAlerta,      text="Medico Asignado",bg="#41576B",fg="white",font=("Verdena",11))
    lbl_direccion=Label(estadoAlerta, text="Direccion :",bg="#41576B",fg="white")
    lbl_latitud=Label(estadoAlerta,   text="Latitud :",bg="#41576B",fg="white")
    lbl_rutMed=Label(estadoAlerta,  text="Longitud :",bg="#41576B",fg="white")


    lbl_nombreMed=Label(estadoAlerta,   text="Nombre :",bg="#41576B",fg="white")
    lbl_apellidoMed=Label(estadoAlerta, text="Apellido :",bg="#41576B",fg="white")
    lbl_rutMed=Label(estadoAlerta,      text="Rut :",bg="#41576B",fg="white")
    lbl_especialidad=Label(estadoAlerta,      text="Especialidad :",bg="#41576B",fg="white")

    entry_nombreMed=Entry(estadoAlerta,textvariable=nombreMed)
    entry_apellidoMed=Entry(estadoAlerta,textvariable=apellidoMed)
    entry_rutMed=Entry(estadoAlerta,textvariable=rutMed)
    entry_especialidad=Entry(estadoAlerta,textvariable=especialidad)

    #Posicion campos MEDICO
    lbl_ficha.grid(row=6,column=1, padx=5, pady=5, sticky=W)

    lbl_rutMed.grid(row=7,column=0, padx=5, pady=5, sticky=E)
    entry_rutMed.grid(row=7,column=1, padx=5, pady=5,sticky=W)

    lbl_nombreMed.grid(row=8,column=0, padx=5, pady=5, sticky=E)
    entry_nombreMed.grid(row=8,column=1, padx=5, pady=5,sticky=W)

    lbl_apellidoMed.grid(row=9,column=0, padx=5, pady=5, sticky=E)
    entry_apellidoMed.grid(row=9,column=1, padx=5, pady=5,sticky=W)

    lbl_especialidad.grid(row=10,column=0, padx=5, pady=5, sticky=E)
    entry_especialidad.grid(row=10,column=1, padx=5, pady=5,sticky=W)

    #Campos ALERTA

    lbl_alerta=Label(estadoAlerta,   text="Alerta :",bg="#41576B",fg="white")
    lbl_idAlerta=Label(estadoAlerta,   text="Id :",bg="#41576B",fg="white")
    lbl_prioridad=Label(estadoAlerta, text="Prioridad :",bg="#41576B",fg="white")
    lbl_estado=Label(estadoAlerta,      text="Estado :",bg="#41576B",fg="white")
    lbl_observaciones=Label(estadoAlerta,      text="Observaciones :",bg="#41576B",fg="white")

    entry_idAlerta=Entry(estadoAlerta,textvariable=idAlerta)
    entry_prioridad=Entry(estadoAlerta,textvariable=prioridad)
    entry_estado=Entry(estadoAlerta,textvariable=estado)
    entry_observaciones=Text(estadoAlerta, height=3,width=15)

    #Posicion campos ALERTA

    lbl_alerta.grid(row=1,column=4, padx=5, pady=5, sticky=W)

    lbl_idAlerta.grid(row=2,column=4, padx=5, pady=5, sticky=E)
    entry_idAlerta.grid(row=2,column=5, padx=5, pady=5,sticky=W)

    lbl_prioridad.grid(row=3,column=4, padx=5, pady=5, sticky=E)
    entry_prioridad.grid(row=3,column=5, padx=5, pady=5,sticky=W)

    lbl_estado.grid(row=4,column=4, padx=5, pady=5, sticky=E)
    entry_estado.grid(row=4,column=5, padx=5, pady=5,sticky=W)

    lbl_observaciones.grid(row=5,column=4, padx=5, pady=5, sticky=E)
    entry_observaciones.grid(row=5,column=5, padx=5, pady=5,sticky=W)



    #BOTONES

    btn_eliminar=Button(estadoAlerta,text="Actualizar",font=("Verdana",10),height=2,width=9,bg="#FAA307").grid(row=10,column=5, padx=5, pady=5, sticky=W)
    btn_eliminar=Button(estadoAlerta,text="Salir",font=("Verdana",10),height=2,width=9,bg="#9D0208").grid(row=10,column=6, padx=5, pady=5, sticky=W)

""" def infoAlertas():

    info_label.config(
        fg="black",
        bg="#ccc",
        font=("Arial", 18),
        padx=400,
    )

    info_label.grid(row=0,column=0)
    add_separator.grid(row=1)
    alertas_table.grid(row=2)


    return True

def infoDespacho():

    info_label.config(
        fg="black",
        bg="#ccc",
        font=("Arial", 18),
        padx=400,
    )

    info_label.grid(row=0,column=0)
    add_separator.grid(row=1)
    alertas_table.grid(row=2)


    return True """

#Boton Estado de Alerta
btn_m=Button(inicio,text="Estado de Alerta",foreground="white",font=("Verdana",14),height=2,width=20, bg="#4E85B7",command=estadoAlerta).place(x=610,y=610)

#Controlador Botonera
def control():
    inicio.pack(expand=True, fill='both')
    lbl_tituloBotonera=Label(botonera,text="Administrador",font=("Verdana",14),foreground="white",bg="#41576B").place(x=55,y=15)

    btn_p=Button(botonera,text=" IR ",font=("Verdana",11),height=2,width=6, bg="#93C2ED",command=partial(paciente,nombreP,apellidoP,numeroP,rutP)).place(x=10,y=170)
    btn_m=Button(botonera,text=" IR ",font=("Verdana",11),height=2,width=6, bg="#93C2ED",command=medico).place(x=10,y=370)


    lbl_btnP=Label(botonera,text="Pacientes",font=("Verdana",11),foreground="white",bg="#41576B").place(x=85,y=180)
    lbl_btnM=Label(botonera,text="Medicos",font=("Verdana",11),foreground="white",bg="#41576B").place(x=85,y=380)
    
    frm_Paciente.pack_forget()
    

#add_separator = Label(alertas,text="")
#lbl_titulo = Label(alertas,text="HOLAMUNDO")
#lbl_titulo.grid
#tabla alertas 
alertas_table = ttk.Treeview(alertas,height=10, columns = ('#1','#2','#3'))
alertas_table.grid(row=4,column=0,columnspan=5)
alertas_table.heading("#0",text="Nombre", anchor=W)
alertas_table.heading("#1",text="Apellido", anchor=W)
alertas_table.heading("#2",text="Numero", anchor=W)
alertas_table.heading("#3",text="Prioridad", anchor=W)

#add_separator = Label(despachado,text="")

despacho_table = ttk.Treeview(despachado,height=10, columns = ('#1','#2','#3'))
despacho_table.grid(row=4,column=0,columnspan=5)
despacho_table.heading("#0",text="Nombre", anchor=W)
despacho_table.heading("#1",text="Apellido", anchor=W)
despacho_table.heading("#2",text="Numero", anchor=W)
despacho_table.heading("#3",text="Prioridad", anchor=W)


#Definir campo alertas
alertas_label= Label(root, text="Paciente")



#Variables Paciente
nomPa=StringVar()
apellidoPa=StringVar()
fonoPa=IntVar()

#Opciones Paciente
alertas_frame=Frame(root)
alertas_alerta_label=Label(alertas_frame, text="Rut")
alertas_paciente_n_entry=Entry(alertas_frame,textvariable=nomPa)
botonRut=Button(alertas_frame,text="Buscar")
botonAlerta=Button(alertas_frame, text="Emitir Alerta")

def pestaña():
    frm_Paciente.pack(expand=True, fill='both') 
    #Opciones del paciente
    #Agregar clases para entrega 2
    rutPa=""
    nom=""
    ap=""
    te=""
    lbl_Paciente=Label(frm_Paciente,text="PACIENTE",font=("Arial",24),bg="Gray").place(x=510,y=10)
    lbl_Rut=Label(frm_Paciente,          text="RUT :",font=("Verdana",12),bg="Gray").place(x=100,y=140)
    btn_EmitirAlerta=Button(frm_Paciente,text="Emitir Alerta",font=("Verdana",18),height=2,width=10,bg="red").place(x=840,y=300)
    btn_Buscar=Button(frm_Paciente,text="Buscar",font=("Verdana",11),height=1,width=6).place(x=350,y=140)
    entry_rut=Entry(frm_Paciente,textvariable=rutPa).place(x=180,y=143)
    lbl_No=Label(frm_Paciente,          text="Nombre :",font=("Verdana",12),bg="Gray").place(x=100,y=200)
    lbl_Ap=Label(frm_Paciente,          text="Apellido :",font=("Verdana",12),bg="Gray").place(x=100,y=250)
    lbl_Te=Label(frm_Paciente,          text="Telefono :",font=("Verdana",12),bg="Gray").place(x=100,y=300)
    entry_Nom=Entry(frm_Paciente,textvariable=nom).place(x=200,y=200)
    entry_Ap=Entry(frm_Paciente,textvariable=ap).place(x=200,y=250)
    entry_Te=Entry(frm_Paciente,textvariable=te).place(x=200,y=300)
    lbl_Fi=Label(frm_Paciente,          text="Comentarios :",font=("Verdana",12),bg="Gray").place(x=450,y=140)
    ficha=Text(frm_Paciente, height=10,width=30).place(x=450,y=200)



    #Ocultar pantallas
    inicio.pack_forget()

    return True

#Funciones para botones pacientes
def guardarPaciente(Rut,Nombre,Apellido,Fono,Direccion):
    pte.setRut(Rut.get())
    pte.setNombre(Nombre.get())
    pte.setApellido(Apellido.get())
    pte.setFono(Fono.get())
    fch.setDireccion(Direccion.get())
    pte.setFicha(fch)
    lista_paciente.append(pte)
    rutP=""
    print(pte.rut,pte.nombre,pte.apellido,pte.fono,pte.ficha.direccion)

def buscarPaciente(Rut,Frame):
        largo=len(lista_paciente)
        for i in range(largo):
            nv=lista_paciente[i].rut
            print(nv,Rut.get())
            if nv==Rut.get():
                nombreP.set(lista_paciente[i].nombre)
                apellidoP.set(lista_paciente[i].apellido)
                numeroP.set(lista_paciente[i].fono)

def editarPaciente(Rut,Nombre,Apellido,Fono,Direccion):
    largo=len(lista_paciente)
    for i in range(largo):
        nv=lista_paciente[i].rut
        print(nv,Rut.get())
        if nv==Rut.get():
            lista_paciente[i].setRut(Rut.get())
            lista_paciente[i].setNombre(Nombre.get())
            lista_paciente[i].setApellido(Apellido.get())
            lista_paciente[i].setFono(Fono.get())
            fch.setDireccion(Direccion.get())
            lista_paciente[i].setFicha(fch)
            print(lista_paciente[i].rut,lista_paciente[i].nombre,lista_paciente[i].apellido,lista_paciente[i].fono,lista_paciente[i].ficha.direccion)

def eliminarPaciente():
    lee="puto"
                
                

menu_superior=Menu(root)
menu_superior.add_command(label="Centro de salud", command=control)
menu_superior.add_command(label="Paciente", command=pestaña)
root.config(menu=menu_superior)

control()
root.mainloop()


