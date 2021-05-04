from tkinter import *
import Profesional
import Alerta
import Paciente
import Centro_Salud
#Definir la ventana
root=Tk()
root.geometry("1200x600")
root.title("Centro de Salud")
root.resizable(0,0)

def salud():
    salud_label.config(
        bg="white",
        font=("Arial",18),
        padx=520
    )
    salud_label.grid(row=0, column=0, columnspan=6)

    #Opciones paciente
    salud_frame.grid(row=1)
    salud_paciente_label.grid(row=1,column=1, padx=5, pady=5, sticky=W)

    salud_nombre_label.grid(row=2,column=0, padx=5, pady=5, sticky=E)
    salud_paciente_n_entry.grid(row=2,column=1, padx=5, pady=5,sticky=W)

    salud_apellido_label.grid(row=3,column=0, padx=5, pady=5, sticky=E)
    salud_paciente_a_entry.grid(row=3,column=1, padx=5, pady=5,sticky=W)

    salud_fono_label.grid(row=4,column=0, padx=5, pady=5, sticky=E)
    salud_paciente_f_entry.grid(row=4,column=1, padx=5, pady=5,sticky=W)

    #Opciones medico

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



    #Ocultar pantallas
    alertas_label.grid_remove()
    alertas_frame.grid_remove()
    return True

def alertas():
    alertas_label.config(
        bg="red",
        font=("Arial",18),
        padx=560
    )
    alertas_label.grid(row=0, column=0)
    #Ocultar pantallas
    salud_label.grid_remove()
    salud_frame.grid_remove()

    #Opciones Pacientes
    alertas_frame.grid(row=1)
    alertas_alerta_label.grid(row=1,column=1, padx=5, pady=5)
    alertas_paciente_n_entry.grid(row=1, column=2, padx=5,sticky=W)
    botonRut.grid(row=1, column=3, padx=5, sticky=W)
    botonRut.config(cursor="hand2")
    botonAlerta.grid(row=2, column=2, padx=20,pady=20)
    botonAlerta.config(cursor="hand2",bg="red",padx=20,pady=20,font=("Arial", 18))

    return True

#Variables Centro de salud
nomP=StringVar()
nomM=StringVar()

nombreP=StringVar()
apellidoP=StringVar()
fonoP=IntVar()

nombreM=StringVar()
apellidoM=StringVar()
fonoM=IntVar()
especialidad=StringVar()

#Variables Paciente
nomPa=StringVar()
apellidoPa=StringVar()
fonoPa=IntVar()

#Definir campos salud
salud_label= Label(root, text="Centro de salud")

#Opciones centro de salud
salud_frame=Frame(root)
salud_paciente_label=Label(salud_frame, text="Paciente")
salud_nombre_label=Label(salud_frame,   text="Nombre :")
salud_apellido_label=Label(salud_frame, text="Apellido :")
salud_fono_label=Label(salud_frame,     text="Fono :")

salud_paciente_n_entry=Entry(salud_frame,textvariable=nombreP)
salud_paciente_a_entry=Entry(salud_frame,textvariable=apellidoP)
salud_paciente_f_entry=Entry(salud_frame,textvariable=fonoP)

salud_medico_label=Label(salud_frame,        text="Profesional")
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

#Definir campo alertas
alertas_label= Label(root, text="Paciente")

#Opciones Paciente
alertas_frame=Frame(root)
alertas_alerta_label=Label(alertas_frame, text="Rut")
alertas_paciente_n_entry=Entry(alertas_frame,textvariable=nomPa)
botonRut=Button(alertas_frame,text="Buscar")
botonAlerta=Button(alertas_frame, text="Emitir Alerta")


salud()
#Menu superior
menu_superior= Menu(root)
menu_superior.add_command(label="Centro de Salud", command=salud)
menu_superior.add_command(label="Paciente", command= alertas)
menu_superior.add_command(label="Salir", command=root.quit)
menu_superior.config(cursor="hand2")


#Cargar menu
root.config(menu=menu_superior)



root.mainloop()