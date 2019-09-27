from lista import * 

from tkinter.ttk import *

 
window.title("Lista")
selected = IntVar() 
window.geometry('640x480')
contenedor()
rad1 = Radiobutton(window,text='Agregar', value=1, variable=selected)
 
rad2 = Radiobutton(window,text='Eliminar', value=2, variable=selected)
 
rad3 = Button(window,text='Ordenar', command=ordenar) 
lbl = Label(window, text="Acción")
txt = Entry(window,width=10)
def clicked(): 
  opciones(selected.get(),txt.get())

btn = Button(window,text='Enviar', command=clicked) 






rad1.grid(column=0, row=0) 
rad2.grid(column=1, row=0) 
rad3.grid(column=2, row=0)
btn.grid(column=3, row=0)
lbl.grid(column=0, row=2)
txt.grid(column=1, row=2)
window.mainloop()