import sympy
import shelve
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as MessageBox
# Conexion con el menu principal
import main

def selection_changed(event): # seleciona y ejecuta la operacion seleccionada
    operacion = comboBox3.get() # toma la opcion del usuario

    if operacion == 'Suma':
        labelTop.configure(text= "+")
    elif operacion == 'Resta':
        labelTop.configure(text= "-")
    elif operacion == 'Multiplicacion':
        labelTop.configure(text= "-")

def regresar(): # se encarga de volver al menu
    raiz.destroy()
    main.main()


def evento(event): # se encarga de extraer el polinomio escogido por el usuario en el primer comboBox
    global selection
    selection = comboBox1.get()


def evento2(event):# se encarga de extraer el polinomio escogido por el usuario en el segundo comboBox
    global selection2
    selection2 = comboBox2.get()


def llenarPolis(): # se encarga de llenar automaticamente los comboBox con los polinomios en memoria
    try:
        datos = shelve.open("DataBase") # abre el shelve para extraer los datos
        aux = []
        for i in datos:
            aux.append(sympy.simplify(datos[i].poli).as_expr())
        comboBox2["values"] = aux
        comboBox1["values"] = aux
        datos.close()
    except KeyError:
        MessageBox.showerror(message="No hay polinomios agregados")
        datos.close()


def sumar(): # se encarga de identificar los polinomios a sumar y sumarlos mediante el metodo suma de la clase polinomio
    datos = shelve.open("DataBase")
    aux1 = 0
    aux2 = 0
    for i in datos:
        if str(selection) == str(datos[i].poli.as_expr()):
            aux1 = i
        if str(selection2) == str(datos[i].poli.as_expr()):
            aux2 = i
    r = datos[aux1].sumar(datos[aux2])
    respuesta.insert(0, r.as_expr()) # incerta el resultado en el texbox
def restar():# se encarga de identificar los polinomios a restar y restarlos mediante el metodo resta de la clase polinomio
    datos = shelve.open("DataBase")
    aux1 = 0
    aux2 = 0
    for i in datos:
        if str(selection) == str(datos[i].poli.as_expr()):
            aux1 = i
        if str(selection2) == str(datos[i].poli.as_expr()):
            aux2 = i
    r = datos[aux1].resta(datos[aux2])
    respuesta.insert(0, r.as_expr())
def multiplicar():# se encarga de multiplicar los polinomios
    datos = shelve.open("DataBase")
    aux1 = 0
    aux2 = 0
    for i in datos:
        if str(selection) == str(datos[i].poli.as_expr()):
            aux1 = i
        if str(selection2) == str(datos[i].poli.as_expr()):
            aux2 = i
    r = datos[aux1].multi(datos[aux2])
    respuesta.insert(0, r.as_expr())

def calcular(): # identifica la operacion que desea realizar el usuario

      try:
          respuesta.delete(0, 'end')
          if comboBox3.get() == 'Suma':
              sumar()
          elif comboBox3.get() == 'Resta':
              restar()
          elif comboBox3.get() == 'Multiplicacion':
              multiplicar()
      except NameError:
          MessageBox.showerror(message="Favor seleccionar los polinomios")


def ventana_op(): # ventana
    global raiz
    raiz = tk.Tk()
    raiz.title("Calculadora de polinomios (Suma)")  # Cambiar el nombre de la ventana
    raiz.geometry("700x500")  # Configurar tamaño
    raiz.configure(bg="dark turquoise")

    global comboBox1
    comboBox1 = ttk.Combobox(raiz, width=30, state="readonly",
                             values=["Polinomios"], postcommand=llenarPolis)

    comboBox1.place(x=50, y=50)

    comboBox1.current(0)
    comboBox1.bind("<<ComboboxSelected>>", evento)
    global labelTop
    labelTop = tk.Label(raiz, text="+")
    labelTop.configure(bg="dark turquoise")
    labelTop.place(x=270, y=50)
    global comboBox2
    comboBox2 = ttk.Combobox(raiz, width=30, state="readonly",
                             values=["Polinomios"], postcommand=llenarPolis)

    comboBox2.place(x=300, y=50)
    comboBox2.bind("<<ComboboxSelected>>", evento2)
    comboBox2.current(0)

    global comboBox3
    comboBox3 = ttk.Combobox(raiz, width=30, state="readonly",
                             values=['Suma',
                                     'Resta',
                                     'Multiplicacion'])

    comboBox3.place(x=200, y=150)
    comboBox3.bind("<<ComboboxSelected>>", selection_changed)
    comboBox3.current(0)

    boton = ttk.Button(text="Calcular", command=calcular)
    boton.place(x=250, y=90, width=90, height=40)

    botonreg = ttk.Button(text="Regresar", command=regresar)
    botonreg.place(x=250, y=400, width=90, height=40)


    label_res = tk.Label(raiz, text="=")
    label_res.place(x=40, y=250)

    global respuesta
    respuesta = ttk.Entry()
    respuesta.place(x=50, y=300, width=400, height=40)

    raiz.mainloop()