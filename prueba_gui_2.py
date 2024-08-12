from tkinter import *
from tkinter import ttk

def saludar(*args):
    saludo.set('¡Bienvenide, '+nombre.get()+'!')


root = Tk()
root.title("Saludo")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Ingrse su nombre:").grid(column=0, row=0, sticky=W)

nombre = StringVar()
nombre_entry = ttk.Entry(mainframe, width=10, textvariable=nombre)
nombre_entry.grid(column=1, row=0, sticky=(W, E))

ttk.Button(mainframe, text="¡Saludar!", command=saludar).grid(column=2, row=0, sticky=W)

saludo = StringVar()
ttk.Label(mainframe, textvariable=saludo).grid(column=0, row=1, sticky=(W, E), columnspan=3)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

nombre_entry.focus()
root.bind("<Return>", saludar)

root.mainloop()