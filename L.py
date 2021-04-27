from tkinter import *

#Definir la ventana
root=Tk()
root.geometry("600x400")
root.title("Centro de Salud")
root.resizable(0,0)

def salud():
    salud_label.config(
        bg="white",
        font=("Arial",18),
        padx=220
    )
    salud_label.grid(row=0, column=0, columnspan=6)

    #Opciones
    salud_frame.grid(row=1)
    salud_paciente_label.grid(row=1,column=0, padx=5, pady=5, sticky=E)
    salud_paciente_entry.grid(row=1,column=1, padx=5, pady=5, sticky=W)

    salud_medico_label.grid(row=2,column=0, padx=5, pady=5,sticky=E)
    salud_medico_entry.grid(row=2,column=1, padx=5, pady=5,sticky=W)

    botonA.grid(row=1,column=3, sticky=W)
    botonA.config(cursor="hand2", bg="green")

    botonE.grid(row=1,column=4, sticky=W)
    botonE.config(cursor="hand2", bg="red")

    botonB.grid(row=1,column=5, sticky=W)
    botonB.config(cursor="hand2")


    botonAM.grid(row=2,column=3, sticky=W)
    botonAM.config(cursor="hand2", bg="green")

    botonEM.grid(row=2,column=4, sticky=W)
    botonEM.config(cursor="hand2",bg="red")

    botonBM.grid(row=2,column=5, sticky=W)
    botonBM.config(cursor="hand2")



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

#Variables
nomP=StringVar()
nomM=StringVar()
#Definir campos salud
salud_label= Label(root, text="Centro de salud")

#Opciones centro de salud
salud_frame=Frame(root)
salud_paciente_label=Label(salud_frame, text="Nombre del paciente: ")
salud_paciente_entry=Entry(salud_frame,textvariable=nomP)

salud_medico_label=Label(salud_frame, text="Nombre del Profesional: ")
salud_medico_entry=Entry(salud_frame,textvariable=nomM)

botonA=Button(salud_frame,text="Agregar")
botonE=Button(salud_frame,text="Eliminar")
botonB=Button(salud_frame,text="Buscar")

botonAM=Button(salud_frame,text="Agregar")
botonEM=Button(salud_frame,text="Eliminar")
botonBM=Button(salud_frame,text="Buscar")

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