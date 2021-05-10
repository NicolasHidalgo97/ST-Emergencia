from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.geometry("1150x560")
root.title("Centro de control")
alertas = Frame(root)
alertas.config(height=400,width=400,bg="red")
alertas.place(x=250,y=60)

despachado = Frame(root)
despachado.config(height=400,width=400,bg="red")
despachado.place(x=680,y=60)

def control():

    #panel botones a la izquierda
    btnp=Button(root,text="Aceptar",font=("Verdana",10),height=3,width=6,command=paciente).place(x=10,y=60)
    btnm=Button(root,text="Aceptar",font=("Verdana",10),height=3,width=6,command=medico).place(x=10,y=140)
    btna=Button(root,text="Aceptar",font=("Verdana",10),height=3,width=6).place(x=10,y=320)


    lbl_btnp=Label(root,text="Agregar Paciente",font=("Verdana",8)).place(x=75,y=80)
    lbl_btnp=Label(root,text="Agregar Medico",font=("Verdana",8)).place(x=75,y=160)
    lbl_btna=Label(root,text="Alerta Azar",font=("Verdana",8)).place(x=75,y=340)
    return True

def paciente():
    #variables pacientes
    nombreP=StringVar()
    apellidoP=StringVar()
    numeroP=IntVar()
    rutP=IntVar()

    #variables ficha medica

    direccionF=StringVar()
    latitudF=IntVar()
    longitudF=IntVar()

    paciente = Toplevel()
    paciente.title("Ficha Medica")
    paciente.geometry("230x450")

    lbl_pac=Label(paciente,      text="Paciente")
    lbl_nombre=Label(paciente,   text="Nombre :")
    lbl_apellido=Label(paciente, text="Apellido :")
    lbl_numero=Label(paciente,   text="Numero :")
    lbl_rut=Label(paciente,      text="Rut :")

    entry_nombre=Entry(paciente,textvariable=nombreP)
    entry_apellido=Entry(paciente,textvariable=apellidoP)
    entry_numero=Entry(paciente,textvariable=numeroP)
    entry_rut=Entry(paciente,textvariable=rutP)

    #Campos PACIENTE
    lbl_pac.grid(row=1,column=1, padx=5, pady=5, sticky=W)

    lbl_nombre.grid(row=2,column=0, padx=5, pady=5, sticky=E)
    entry_nombre.grid(row=2,column=1, padx=5, pady=5,sticky=W)

    lbl_apellido.grid(row=3,column=0, padx=5, pady=5, sticky=E)
    entry_apellido.grid(row=3,column=1, padx=5, pady=5,sticky=W)

    lbl_numero.grid(row=4,column=0, padx=5, pady=5, sticky=E)
    entry_numero.grid(row=4,column=1, padx=5, pady=5,sticky=W)

    lbl_rut.grid(row=5,column=0, padx=5, pady=5, sticky=E)
    entry_rut.grid(row=5,column=1, padx=5, pady=5,sticky=W)

    #Campos FICHA

    lbl_ficha=Label(paciente,      text="Ficha medica")
    lbl_direccion=Label(paciente, text="Direccion :")
    lbl_latitud=Label(paciente,   text="Latitud :")
    lbl_longitud=Label(paciente,  text="Longitud :")

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

    btn_agregar=Button(paciente,text="Agregar",font=("Verdana",10),height=3,width=6).place(x=10,y=300)
    btn_editar=Button(paciente,text="Editar",font=("Verdana",10),height=3,width=6).place(x=80,y=300)
    btn_buscar=Button(paciente,text="Buscar",font=("Verdana",10),height=3,width=6).place(x=150,y=300)
    btn_eliminar=Button(paciente,text="Eliminar",font=("Verdana",10),height=3,width=6).place(x=10,y=380)

def medico():
    #variables MEDICO
    nombreM=StringVar()
    apellidoM=StringVar()
    numeroM=IntVar()
    rutM=IntVar()
    especialidad=StringVar()

    medico = Toplevel()
    medico.title("Agregar Medico")
    medico.geometry("230x450")

    lbl_med=Label(medico,          text="Medico")
    lbl_nombre=Label(medico,       text="Nombre :")
    lbl_apellido=Label(medico,     text="Apellido :")
    lbl_numero=Label(medico,       text="Numero :")
    lbl_rut=Label(medico,          text="Rut :")
    lbl_especialidad=Label(medico, text="Especialidad :")

    entry_nombre=Entry(medico,textvariable=nombreM)
    entry_apellido=Entry(medico,textvariable=apellidoM)
    entry_numero=Entry(medico,textvariable=numeroM)
    entry_rut=Entry(medico,textvariable=rutM)
    entry_especialidad=Entry(medico,textvariable=especialidad)

    #Campos medico
    lbl_med.grid(row=1,column=1, padx=5, pady=5, sticky=W)

    lbl_nombre.grid(row=2,column=0, padx=5, pady=5, sticky=E)
    entry_nombre.grid(row=2,column=1, padx=5, pady=5,sticky=W)

    lbl_apellido.grid(row=3,column=0, padx=5, pady=5, sticky=E)
    entry_apellido.grid(row=3,column=1, padx=5, pady=5,sticky=W)

    lbl_numero.grid(row=4,column=0, padx=5, pady=5, sticky=E)
    entry_numero.grid(row=4,column=1, padx=5, pady=5,sticky=W)

    lbl_rut.grid(row=5,column=0, padx=5, pady=5, sticky=E)
    entry_rut.grid(row=5,column=1, padx=5, pady=5,sticky=W)

    lbl_especialidad.grid(row=6,column=0, padx=5, pady=5, sticky=E)
    entry_especialidad.grid(row=6,column=1, padx=5, pady=5,sticky=W)

    #BOTONES

    btn_agregar=Button(medico,text="Agregar",font=("Verdana",10),height=3,width=6).place(x=10,y=300)
    btn_editar=Button(medico,text="Editar",font=("Verdana",10),height=3,width=6).place(x=80,y=300)
    btn_buscar=Button(medico,text="Buscar",font=("Verdana",10),height=3,width=6).place(x=150,y=300)
    btn_eliminar=Button(medico,text="Eliminar",font=("Verdana",10),height=3,width=6).place(x=10,y=380)
    

control()
root.mainloop()