from tkinter import *

# Configuración de la raíz
root = Tk()
root.title("Centro de Salud")
root.resizable(1,1)
root.config(bg="white")
#root.iconbitmap('hola.ico')

#Frame del Paciente
frm_Paciente = Frame(root, width=480, height=320)
frm_Paciente.pack()
# Color de fondo, background
frm_Paciente.config(bg="lightblue")
frm_Paciente.config(relief="sunken")   # relieve del frame hundido
frm_Paciente.config(bd=4)             # tamaño del borde en píxeles  
frm_Paciente.pack(side=LEFT)
frm_Paciente.pack(anchor=N)
frm_Paciente.pack(fill="both", expand=1)

#Frame del Profesional 
frm_Profesional = Frame(root, width=480, height=320)
frm_Profesional.pack()

# Config frame profesional
frm_Profesional.config(bg="pink")
frm_Profesional.config(relief="sunken")   # relieve del frame hundido
frm_Profesional.config(bd=4)             # tamaño del borde en píxeles  
frm_Profesional.pack(side=RIGHT)
frm_Profesional.pack(anchor=N)
frm_Profesional.pack(fill="x", expand=1)

#Frame de Tabla 
frm_Tabla = Frame(root, width=480, height=320)
frm_Tabla.pack()

# Config frame Tabla
frm_Tabla.config(bg="gray")
frm_Tabla.config(relief="sunken")   # relieve del frame hundido
frm_Tabla.config(bd=4)             # tamaño del borde en píxeles  

#frm_Tabla.pack(side=)
frm_Tabla.pack(anchor=S)
frm_Tabla.pack(fill="x", expand=1)



# Finalmente bucle de la aplicación
root.mainloop()