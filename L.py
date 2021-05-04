from tkinter import *

#Definir la ventana
root=Tk()
root.geometry("900x500")
root.title("Centro de Salud")
root.resizable(0,0)

def salud():
    salud_label.config(
        bg="white",
        font=("Arial",18),
        padx=380
    )
    salud_label.grid(row=0, column=0, columnspan=6)

    #Campos paciente y medico hasta row 10 y column 1
    salud_frame.grid(row=1)
    salud_paciente_label.grid(row=1,column=1, padx=5, pady=5, sticky=W)

    salud_nombre_label.grid(row=2,column=0, padx=5, pady=5, sticky=E)
    salud_paciente_n_entry.grid(row=2,column=1, padx=5, pady=5,sticky=W)

    salud_apellido_label.grid(row=3,column=0, padx=5, pady=5, sticky=E)
    salud_paciente_a_entry.grid(row=3,column=1, padx=5, pady=5,sticky=W)

    salud_fono_label.grid(row=4,column=0, padx=5, pady=5, sticky=E)
    salud_paciente_f_entry.grid(row=4,column=1, padx=5, pady=5,sticky=W)

    #Opciones MEDICO

    salud_medico_label.grid(row=5,column=1, padx=5, pady=5, sticky=W)

    salud_nombreM_label.grid(row=6,column=0, padx=5, pady=5, sticky=E)
    salud_medico_n_entry.grid(row=6,column=1, padx=5, pady=5,sticky=W)

    salud_apellidoM_label.grid(row=7,column=0, padx=5, pady=5, sticky=E)
    salud_medico_a_entry.grid(row=7,column=1, padx=5, pady=5,sticky=W)

    salud_fonoM_label.grid(row=8,column=0, padx=5, pady=5, sticky=E)
    salud_medico_f_entry.grid(row=8,column=1, padx=5, pady=5,sticky=W)

    salud_especialidad_label.grid(row=9,column=0, padx=5, pady=5, sticky=E)
    salud_medico_e_entry.grid(row=9,column=1, padx=5, pady=5,sticky=W)

    botonA.grid(row=10,column=1, sticky=W)
    botonA.config(cursor="hand2", bg="green")

    botonE.grid(row=10,column=2, sticky=W)
    botonE.config(cursor="hand2", bg="red")

    botonB.grid(row=10,column=3, sticky=W)
    botonB.config(cursor="hand2")


    botonAM.grid(row=10,column=1, sticky=W)
    botonAM.config(cursor="hand2", bg="green")

    botonEM.grid(row=10,column=2, sticky=W)
    botonEM.config(cursor="hand2",bg="red")

    botonBM.grid(row=10,column=3, sticky=W)
    botonBM.config(cursor="hand2")

    #campos FICHAMEDICA

    salud_ficha_label.grid(row=1,column=4, padx=5, pady=5, sticky=W)

    salud_pacienteF_label.grid(row=2,column=3, padx=5, pady=5, sticky=E)
    salud_ficha_p_entry.grid(row=2,column=4, padx=5, pady=5,sticky=W)

    salud_direccionF_label.grid(row=3,column=3, padx=5, pady=5, sticky=E)
    salud_ficha_d_entry.grid(row=3,column=4, padx=5, pady=5,sticky=W)

    salud_latitudF_label.grid(row=4,column=3, padx=5, pady=5, sticky=E)
    salud_ficha_la_entry.grid(row=4,column=4, padx=5, pady=5,sticky=W)

    salud_longitudF_label.grid(row=5,column=3, padx=5, pady=5, sticky=E)
    salud_ficha_lo_entry.grid(row=5,column=4, padx=5, pady=5,sticky=W)

    #campos ALERTAS

    salud_alerta_label.grid(row=1,column=8, padx=5, pady=5, sticky=W)

    salud_pacienteA_label.grid(row=2,column=7, padx=5, pady=5, sticky=E)
    salud_alerta_p_entry.grid(row=2,column=8, padx=5, pady=5,sticky=W)

    salud_profesionalA_label.grid(row=3,column=7, padx=5, pady=5, sticky=E)
    salud_alerta_pro_entry.grid(row=3,column=8, padx=5, pady=5,sticky=W)

    salud_prioridadA_label.grid(row=4,column=7, padx=5, pady=5, sticky=E)
    salud_alerta_pri_entry.grid(row=4,column=8, padx=5, pady=5,sticky=W)

    salud_ubicacionA_label.grid(row=5,column=7, padx=5, pady=5, sticky=E)
    salud_alerta_u_entry.grid(row=5,column=8, padx=5, pady=5,sticky=W)

    salud_estadoA_label.grid(row=6,column=7, padx=5, pady=5, sticky=E)
    salud_alerta_e_entry.grid(row=6,column=8, padx=5, pady=5,sticky=W)

    #Ocultar pantallas
    alertas_label.grid_remove()
    return True

def alertas():
    alertas_label.config(
        bg="red",
        font=("Arial",18),
        padx=250
    )
    alertas_label.grid(row=0, column=0)
    #Ocultar pantallas
    salud_label.grid_remove()
    salud_frame.grid_remove()
    return True

#Variables pacientes/profesionales
nomP=StringVar()
nomM=StringVar()

nombreP=StringVar()
apellidoP=StringVar()
fonoP=IntVar()

nombreM=StringVar()
apellidoM=StringVar()
fonoM=IntVar()
especialidad=StringVar()
#variables ficha medica

pacienteF=StringVar()
direccionF=StringVar()
latitudF=IntVar()
longitudF=IntVar()

#variables alertas

pacienteA=StringVar()
profesionalA=StringVar()
prioridadA=StringVar()
ubiacionA=IntVar()
estadoA=IntVar()


#Definir campos salud
salud_label= Label(root, text="Centro de salud")

#Opciones centro de salud pacientes/Medicos
salud_frame=Frame(root)
salud_paciente_label=Label(salud_frame, text="Paciente")
salud_nombre_label=Label(salud_frame,   text="Nombre :")
salud_apellido_label=Label(salud_frame, text="Apellido :")
salud_fono_label=Label(salud_frame,     text="Fono :")

salud_paciente_n_entry=Entry(salud_frame,textvariable=nombreP)
salud_paciente_a_entry=Entry(salud_frame,textvariable=apellidoP)
salud_paciente_f_entry=Entry(salud_frame,textvariable=fonoP)

salud_medico_label=Label(salud_frame,        text="Medico")
salud_nombreM_label=Label(salud_frame,       text="Nombre :")
salud_apellidoM_label=Label(salud_frame,     text="Apellido :")
salud_fonoM_label=Label(salud_frame,         text="Fono :")
salud_especialidad_label=Label(salud_frame,  text="Especialidad :")

salud_medico_n_entry=Entry(salud_frame,textvariable=nombreM)
salud_medico_a_entry=Entry(salud_frame,textvariable=apellidoM)
salud_medico_f_entry=Entry(salud_frame,textvariable=fonoM)
salud_medico_e_entry=Entry(salud_frame,textvariable=especialidad)



botonA=Button(salud_frame,text="Agregar")
botonE=Button(salud_frame,text="Eliminar")
botonB=Button(salud_frame,text="Buscar")

botonAM=Button(salud_frame,text="Agregar")
botonEM=Button(salud_frame,text="Eliminar")
botonBM=Button(salud_frame,text="Buscar")

#Opciones ficha medica

salud_ficha_label=Label(salud_frame,      text="Ficha medica")
salud_pacienteF_label=Label(salud_frame,  text="Paciente :")
salud_direccionF_label=Label(salud_frame, text="Direccion :")
salud_latitudF_label=Label(salud_frame,   text="Latitud :")
salud_longitudF_label=Label(salud_frame,  text="Longitud :")

salud_ficha_p_entry=Entry(salud_frame,textvariable=pacienteF)
salud_ficha_d_entry=Entry(salud_frame,textvariable=direccionF)
salud_ficha_la_entry=Entry(salud_frame,textvariable=latitudF)
salud_ficha_lo_entry=Entry(salud_frame,textvariable=longitudF)

#opciones alertas
salud_alerta_label=Label(salud_frame,       text="Alertas")
salud_pacienteA_label=Label(salud_frame,   text="Paciente :")
salud_profesionalA_label=Label(salud_frame,text="Profesional :")
salud_prioridadA_label=Label(salud_frame,   text="Prioridad :")
salud_ubicacionA_label=Label(salud_frame,  text="Ubicacion :")
salud_estadoA_label=Label(salud_frame,     text="Estado :")

salud_alerta_p_entry=Entry(salud_frame,textvariable=pacienteA)
salud_alerta_pro_entry=Entry(salud_frame,textvariable=profesionalA)
salud_alerta_pri_entry=Entry(salud_frame,textvariable=prioridadA)
salud_alerta_u_entry=Entry(salud_frame,textvariable=ubiacionA)
salud_alerta_e_entry=Entry(salud_frame,textvariable=estadoA)

#Definir campo alertas
alertas_label= Label(root, text="Paciente")



salud()
#Menu superior
menu_superior= Menu(root)
menu_superior.add_command(label="Centro de Salud", command=salud)
menu_superior.add_command(label="Alertas", command= alertas)
menu_superior.add_command(label="Salir", command=root.quit)
menu_superior.config(cursor="hand2")


#Cargar menu
root.config(menu=menu_superior)



root.mainloop()