from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import *
window = Tk()
lista = []


def opciones(opcion, y):    
    if opcion != "" and y != "":
        accion(opcion, y)
    else:
        messagebox.showerror('Error', 'Seleccione y LLene una acción.')

def ordenar():
     lista.sort()
     contenedor()

def accion(opcion, contenido):
    if opcion==1:
         lista.append(contenido)
         contenedor()
         messagebox.showinfo(message="Se agrego correctamente.", title="Success")
    elif opcion==2:
        indice = lista.index(contenido)
        lista.pop(indice)
        contenedor()
        messagebox.showinfo(message="Se borro correctamente.", title="Success")
    else:
        messagebox.showerror('Error', 'No existe esa selección.')
        
    


def contenedor():
    quote = ', '.join(lista)
    txt = Text(window, height=20, width=50)
    txt.insert(INSERT, quote)
    txt.grid(column=6, row=4)
