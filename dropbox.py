from tkinter import *

ventana = Tk()
ventana.geometry("400x400")

encabezado = Label(ventana,text="Formularios 2")
encabezado.config(padx=15,pady=15,bd=1,fg="black",bg="#ccc", font=("Consolas", 28))
encabezado.grid(row=0, column=0,columnspan=6, sticky="W")


## Button Check ##

def MostrarProfesion():
    texto = ""

    if web.get():
        texto += "Desarrollo Web "
    if movil.get():
        if web.get():
            texto += "y Desarrollo Movil"
        else:
            texto += "Desarrollo Movil"

    mostrar.config(
        text=texto,
        bg="green",
        fg="white"

    )

web = IntVar()
movil = IntVar()

Label(ventana, text="A que te dedicas?").grid(row=1,column=0)

Checkbutton(ventana, text="Desarrollo web",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=MostrarProfesion
).grid(row=2, column=0)

Checkbutton(ventana, text="Desarrollo Movil",
    variable=movil,
    onvalue=1,
    offvalue=0,
    command=MostrarProfesion
).grid(row=3,column=0)


mostrar =  Label(ventana, text="")
mostrar.grid(row=4,column=0)


## Radio Button ##
def Marcar():                                                                   ## Metodo para obtener la informacion del boton que se marque
    Marcado.config(text=opcion.get())

opcion = StringVar()                                                            ## Guardo la variable como un string pq es una palabra
opcion.set(None)                                                                ## Para que cuando inicie el programa este no tenga nada marcado

Label(ventana,text="Cual es tu genero: ").grid(row=5)
Radiobutton(
    ventana,
    text="Masculino",                                                           ## Nombre del checkbox
    value="Masculino",                                                          ## lo que quiero guardar como variable
    variable=opcion,
    command=Marcar

).grid(row=6)

Radiobutton(
    ventana,
    text="Femenino",
    value="Femenino",
    variable=opcion,
    command=Marcar

).grid(row=7)

Marcado = Label(ventana)                                                        ## label que muestra lo que se marque de la funcion Marcar
Marcado.grid(row=8)





## Option ## 

def Seleccionar():
    Seleccionado.config(text=OpcionMenu.get())

OpcionMenu= StringVar()
OpcionMenu.set("Opcion 1")

Label(ventana,text="Seleccione una opcion").grid(row=5, column=1)

select = OptionMenu(ventana,OpcionMenu, "Opcion 1", "Opcion 2", "Opcion 3")
select.option_add(OpcionMenu,"caca")
select.grid(row=6, column=1)

Button(ventana, text="Ver", command=Seleccionar).grid(row=7,column=1)


Seleccionado = Label(ventana)
Seleccionado.grid(row=8,column=1)



ventana.mainloop()