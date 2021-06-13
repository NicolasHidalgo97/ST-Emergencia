from tkinter import *
from tkinter import ttk
dash=Tk()

dato=StringVar()
dato2=StringVar()
datosg=[]
def guardarda():
    datosg.append([
        dato.get(),
        dato2.get()
    ])
    #for d in datosg:
        #if len(d)==2:
           # Label(caja_datos, text=d[0]).grid()
           # Label(caja_datos,text=d[1]).grid()
    #print(datosg)

    for d in datosg:
        if len(d)==2:
            d.append("added")
            datos_table.insert("",0,text=d[0],values=(d[1]))
           

dash.geometry("600x400")
dash.resizable
dash.title("Alerta")


caja_datos=Frame(dash)
Label(caja_datos).grid(row=0)
datos_table=Label(caja_datos)
caja_datos.grid(row=5,column=1,padx=5, pady=5, sticky=W)

datos_table=ttk.Treeview(height=8,column=2)
datos_table.grid(row=6,column=1, columnspan=1)
datos_table.heading("#0",text="Nombre", anchor=W)
datos_table.heading("#1",text="Apellido", anchor=W)



infor_label= Label(dash, text="Alertas")
infor_label.grid(row=1,column=1, padx=5, pady=5, sticky=W)
entry_dato=Entry(dash,textvariable=dato)
entry_dato2=Entry(dash,textvariable=dato2)

entry_dato.grid(row=2,column=1,padx=5,pady=5, sticky=W)
entry_dato2.grid(row=3,column=1,padx=5,pady=5, sticky=W)

botonguar=Button(dash, text="Guardar", command=guardarda)
botonguar.grid(row=4,column=1,padx=5,pady=5, sticky=W)
    
dash.mainloop()