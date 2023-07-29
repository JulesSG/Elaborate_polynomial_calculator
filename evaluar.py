import sympy
import shelve
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as MessageBox
# Conexion con el menu principal
import main

def regresar(): # regresa al menu
    raiz.destroy()
    main.main()
def evento(event): # identifica la seleccion del usuario
    global selection
    selection = comboBox.get()


def llenarPolis(): # llena el comboBox con los polinomios en memoria
    try:
        datos = shelve.open("DataBase")
        aux = []
        for i in datos:
            aux.append(sympy.simplify(datos[i].poli).as_expr())
        comboBox["values"] = aux
        datos.close()
    except KeyError:
        MessageBox.showerror(message="No hay polinomios agregados")
        datos.close()

def calcular(): # evalua el polinomio usando el metodo evaluar de la clase polinimio
    datos = shelve.open("DataBase")
    aux = 0
    try:
        for i in datos:
            if str(selection) == str(datos[i].poli.as_expr()):
                aux = i

        try:
            resp.delete(0,"end")
            resp.insert(0, str(datos[aux].evaluar(num.get())))
        except ValueError:
            MessageBox.showerror(message="El valor ingresado no se puede evaluar")
    except NameError:
        MessageBox.showerror(message="Porfavor seleccionar un polinomio")

def ventanaEv():# ventana
    global raiz
    raiz = tk.Tk()
    raiz.title("Evaluar polinomio")  # Cambiar el nombre de la ventana
    raiz.geometry("700x500")  # Configurar tamaño
    raiz.configure(bg="dark turquoise")
    global comboBox
    comboBox = ttk.Combobox(raiz, width=30, state="readonly",
                             values=["Seleccione el polinomio"], postcommand=llenarPolis)

    comboBox.place(x=300, y=50)

    comboBox.current(0)
    comboBox.bind("<<ComboboxSelected>>", evento)

    label = tk.Label(raiz, text="Ingrese el numero a evaluar: ")
    label.place(x=50, y=75)

    global num
    num= ttk.Entry()
    num.place(x=220, y=75, width=50, height=50)

    label3 = tk.Label(raiz, text="Respuesta: ")
    label3.place(x=50, y=150)
    global resp
    resp = ttk.Entry()
    resp.place(x=120, y=150, width=50, height=50)

    boton = ttk.Button(text="Calcular", command=calcular)
    boton.place(x=350, y=110, width=90, height=40)

    botonreg = ttk.Button(text="Regresar", command=regresar)
    botonreg.place(x=250, y=400, width=90, height=40)

    raiz.mainloop()