import sympy
import shelve
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as MessageBox
# Conexion con el menu principal
import main

def regresar(): # regresa al menu principal
    raiz.destroy()
    main.main()


def agregar(): # agrega un polinomio usando la funcion memoria
    main.memoria(poli.get())
    poli.delete(0, 'end')
def ventanaAg():#ventana
    global raiz
    raiz = tk.Tk()
    raiz.title("Agregar polinomio")  # Cambiar el nombre de la ventana
    raiz.geometry("700x500")  # Configurar tamaño
    raiz.configure(bg="dark turquoise")




    label = tk.Label(raiz, text="Ingrese el polinomio: ")
    label.place(x=50, y=50)
    global poli
    poli = ttk.Entry()
    poli.place(x=200, y=50, width=400, height=50)

    boton = ttk.Button(text="Agregar", command=agregar)
    boton.place(x=250, y=110, width=90, height=40)

    botonreg = ttk.Button(text="Regresar", command=regresar)
    botonreg.place(x=250, y=400, width=90, height=40)

    labelpoli = tk.Label(raiz, text="Forma de como escribir un polinomio: a*X**n + ..... \n"
                                    "Siendo a y n numeros reales")
    labelpoli.place(x=50, y=175)

    raiz.mainloop()