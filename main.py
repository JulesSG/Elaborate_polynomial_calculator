import sympy         # Libreria para operar polinomios
from sympy import *
import  shelve # libreria para guardar objetos en memoria
import tkinter as tk # libreria para crear ventanas
from tkinter import ttk
from tkinter import messagebox as MessageBox

# Se importan  las demas ventanas
import operaciones
import Agregar_poli
import evaluar
global x
x = Symbol("x") # se declara la variable de los polinomios

class Polinomio:  # se crea la clase polinomio
    def __init__(self, poli):
        self.poli = poli
    # se crean los metodos para operar polinomios
    def sumar(self, poli2):
        suma = self.poli + poli2.poli
        return simplify(suma)
    def resta(self, poli2):
        resta = self.poli - poli2.poli
        return simplify(resta)
    def multi(self, poli2):
        multipoli= self.poli * poli2.poli
        return simplify(multipoli)
    def evaluar(self, num):
        try:
            print(num, self.poli)
            numero = self.poli.subs(x, num).evalf(int(5))
            return numero
        except AttributeError:
            MessageBox.showerror(message="El valor no se puede evaluar en la funcion")


def memoria(poli): # se crea una funcion para guardar los polinomios en memoria
    try:
        datos = shelve.open("DataBase")
        k = list(datos.keys())
        try:
            k = int(k.pop()) + 1
        except IndexError:
            k = 0
        datos[f"{k}"] = Polinomio(sympy.Poly(poli))
        MessageBox.showinfo(title="Memoria", message="Tarea exitosa")
        datos.close()
    except SympifyError:
        MessageBox.showerror(title='SyntaxError',message='El polinomoio esta mal escrito')


def selection_changed(event): # funcion encargardad de navegar entre ventanas
    selection = comboBox.get()

    if selection == "Agregar polinomio":
        raiz.destroy() # esconde la ventana actual
        Agregar_poli.ventanaAg() # abre la ventana que llama
    elif selection=="Operar polinomios":
        raiz.destroy()
        operaciones.ventana_op()
    elif selection == "Evaluar polinomio":
        raiz.destroy()
        evaluar.ventanaEv()

def main(): # funcion principal
    global raiz
    raiz = tk.Tk()
    raiz.title("Calculadora de polinomios")  # Cambiar el nombre de la ventana
    raiz.geometry("520x480")  # Configurar tamaño
    raiz.configure(bg="dark turquoise") # color de la ventana
    #label
    labelTop = tk.Label(raiz, text="Escojer la tarea a realizar: ")
    labelTop.grid(column=0, row=8)

    global comboBox
    comboBox = ttk.Combobox(raiz, width=30, state="readonly",
                            values=[
                                "Agregar polinomio",
                                "Operar polinomios",
                                "Evaluar polinomio"])

    comboBox.place(x=150, y=50)
    comboBox.current(0)
    comboBox.bind("<<ComboboxSelected>>", selection_changed)# se encarga de leer la seleccion del usuario

    raiz.mainloop()

if __name__ == '__main__': # se llama a la funcion principal al iniciar el programa
    main()