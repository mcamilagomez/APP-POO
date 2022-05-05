from enum import Enum
# Importamos las librerías para la GUI
import tkinter as tk
from tkinter import ttk
from tkinter import Entry, StringVar, Toplevel, messagebox
import tkinter.font as tkFont
from turtle import color
# PARA CREAR LA INTERFAZ GRÁFICA
# Creamos la ventana principal
ventana = tk.Tk()
# Tamaño de la ventana:
Height = 918
Width = 520
ventana.geometry("918x520+230+100")
# Título de la ventana principal
ventana.title("Pc Explorer")
ventana.resizable(width=0, height=0)
# Tipo de letra
Fuente_principal = tkFont.Font(family="Lucida Bright", size=11)
# Fondos
imagen = tk.PhotoImage(file="pp.png")
fondo = tk.Label(ventana, image=imagen).place(x=0, y=0)
credits = tk.PhotoImage(file="credits.png")
opciones = tk.PhotoImage(file="opciones.png")
Explicacion = tk.PhotoImage(file="como funciona.png")
Imagen_Regresar = tk.PhotoImage(file="boton regresar.png")
Imagen_Regresar_Creditos = tk.PhotoImage(file="regresar Creditos.png")
Fondo_Pisos = tk.PhotoImage(file="pisos.png")
Bloque_B = tk.PhotoImage(file="bloqueb.png")
Bloque_C = tk.PhotoImage(file="bloquec.png")
Bloque_D = tk.PhotoImage(file="bloqued.png")
Bloque_K = tk.PhotoImage(file="bloqueK.png")
Bloque_G = tk.PhotoImage(file="bloqueg.png")
Biblioteca = tk.PhotoImage(file="biblioteca.png")
Casa_Estudio = tk.PhotoImage(file="casaestudio.png")
Piso1 = tk.PhotoImage(file="piso1.png")
Piso2 = tk.PhotoImage(file="piso2.png")
Piso3 = tk.PhotoImage(file="piso3.png")
Disponibles_G = tk.PhotoImage(file="disponibles.png")

# PARA CREAR LAS DEMÁS VENTANAS
# Cada función es un menú


def MainMenu():
    # Esta clase valida que el usuario no ingrese letras, solo números que hacen
    # referencia  a su código estudiantil
    class codigos():
        def __init__(self, text):
            self.text = text

        def validate_code(text: str):
            return text.isdecimal()

    # Para resetear la pantalla cuando uno se devuelva al menu principal
    for ele in ventana.winfo_children():
        ele.destroy()
    # Label que muestra la imagen de la pantalla principal
    label2 = tk.Label(ventana, image=imagen)
    label2.pack()
    # Botón creditos que hace que se cambie a la ventana de créditos
    Boton_Creditos = tk.Button(ventana, text="Créditos", width=8, height=1, font=Fuente_principal,
                               command=Ventana_creditos, bg="#FFFFFF",  bd=1, disabledforeground=None,  relief="flat")
    Boton_Creditos.place(x=618, y=65)
    # Botón explicacion que hace que se cambie a la ventana de "How does it work?"
    Boton_Explicacion = tk.Button(ventana, text="¿Cómo funciona?", width=20, height=1, font=Fuente_principal,
                                  command=Ventana_Explicacion, bg="#FFFFFF",  bd=1, disabledforeground=None,  relief="flat")
    Boton_Explicacion.place(x=160, y=65)
    # Para crear el textfile en el que el usuario ingresará su código
    codigo = StringVar()
    # Aquí se valida lo que el usuario ingresa
    codigoEntry = Entry(ventana, textvariable=codigo, bg="#ECE7E6", width=35, validate="key",
                        validatecommand=(ventana.register(codigos.validate_code), "%S"))
    codigoEntry.place(x=473, y=385, width=100, height=30)

    # LOGIN
    def login():
        # Validar que el campo no este vacío
        Validar_codigo = codigoEntry.get()
        if(Validar_codigo == ""):
            Error = tk.Label(ventana, text="Error, campos vacíos, intente de nuevo.",
                             font=Fuente_principal, disabledforeground=None, bg="#FFFFFF")
            Error.place(x=600, y=385)
        else:  # si no esta vacío entonces se muestra la otra interfaz
            if Validar_codigo in readfile:
                Ventana_Opciones()
            else:
                Error = tk.Label(ventana, text="Error, código no encontrado.",
                                 font=Fuente_principal, disabledforeground=None, bg="#FFFFFF")
                Error.place(x=600, y=385)
    # Abrimos el archivo txt que contiene los códigos estudiantiles
    filename = ("file/codigos.txt")
    with open(filename) as file:
        readfile = file.read()

    # boton para ingresar o acceder
    Button_login = tk.Button(ventana, text="Acceder", width=7,
                             height=1, command=login, font=Fuente_principal)
    Button_login.place(x=500, y=430)

# Ventana de creditos


def Ventana_Disponibilidad_G():
    # Destruye o resetea todo lo que se encuentra en la ventana anterior
    for ele in ventana.winfo_children():
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Disponibles_G)
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    prueba = Disponibilidad_G()
    prueba.dispo_pc()
            
def Ventana_creditos():
    # Destruye o resetea todo lo que se encuentra en la ventana anterior
    for ele in ventana.winfo_children():
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=credits)
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    Boton_Regreso = tk.Button(ventana, text="", command=MainMenu, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar_Creditos, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Regreso.place(x=847, y=449, width=63, height=64)

class Disponibilidad_G():
        def __init__(self):
            file = open("file\dispo.txt")
            self.readfile = file.readlines()
 
        def dispo_pc(self): 
            for string in self.readfile:
                fila = string.split(",")
                lugar = fila[0]
                piso = fila[1]
                disponibilidad = fila[2]
                cantidad = int(fila[3])
                if (lugar == "Bloque G"):
                    if (disponibilidad == "true"):
                        print(cantidad)

def Ventana_Opciones():
    # Destruye o resetea todo lo que se encuentra en la ventana anterior
    for ele in ventana.winfo_children():
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz_opciones = tk.Canvas(ventana)
    interfaz_opciones.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz_opciones, image=opciones)
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    Boton_Regreso = tk.Button(ventana, text="", command=MainMenu, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Regreso.place(x=830, y=445, width=74, height=70)
    Boton_PisoB = tk.Button(ventana, text="Bloque B", command=Ventana_Pisos_BloqueB, width=7, height=1,
                            font=Fuente_principal, image=Bloque_B, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_PisoB.place(x=50, y=305, width=200, height=49)
    Boton_PisoC = tk.Button(ventana, text="Bloque C", width=7, height=1, font=Fuente_principal,
                            image=Bloque_C, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_PisoC.place(x=50, y=400, width=200, height=49)
    Boton_PisoD = tk.Button(ventana, text="Bloque D", width=7, height=1, font=Fuente_principal,
                            image=Bloque_D, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_PisoD.place(x=270, y=305, width=200, height=49)
    Boton_PisoK = tk.Button(ventana, text="Bloque K", width=7, height=1, font=Fuente_principal,
                            image=Bloque_K, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_PisoK.place(x=270, y=400, width=200, height=49)
    Boton_Biblioteca=tk.Button(ventana, text = "Biblioteca", width = 7, height = 1,
                                 image = Biblioteca, bg = "#FFFFFF", bd = 1, disabledforeground = None,  relief = "flat")
    Boton_Biblioteca.place(x = 490, y = 400, width = 200, height = 49)
    Boton_CasaE=tk.Button(ventana, text = "Casa Estudio", width = 7, height = 1, command = Ventana_Pisos_CasaE,
                            image = Casa_Estudio, bg = "#FFFFFF", bd = 1, disabledforeground = None,  relief = "flat")
    Boton_CasaE.place(x = 710, y = 355, width = 200, height = 49)
    Boton_PisoG = tk.Button(ventana, text="Bloque G", width=7, height=1, font=Fuente_principal, command=Ventana_Disponibilidad_G,
                            image=Bloque_G, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_PisoG.place(x=490, y=305, width=200, height=49)
    Boton_Biblioteca = tk.Button(ventana, text="Biblioteca", width=7, height=1,
                                 image=Biblioteca, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Biblioteca.place(x=490, y=400, width=200, height=49)
    Boton_CasaE = tk.Button(ventana, text="Casa Estudio", width=7, height=1, command=Ventana_Pisos_CasaE,
                            image=Casa_Estudio, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_CasaE.place(x=710, y=355, width=200, height=49)
    
def Ventana_Explicacion():
    # Destruye o resetea todo lo que se encuentra en la ventana anterior
    for ele in ventana.winfo_children():
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz_Explicacion=tk.Canvas(ventana)
    interfaz_Explicacion.pack()
    # En el label se carga la imagen
    label1=tk.Label(interfaz_Explicacion, image = Explicacion)
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    Boton_Regreso=tk.Button(ventana, text = "", command = MainMenu, width = 7, height = 1, font = Fuente_principal,
                              image = Imagen_Regresar, bg = "#FFFFFF", bd = 1, disabledforeground = None,  relief = "flat")
    Boton_Regreso.place(x = -3, y = 467, width = 74, height = 70)


def Ventana_Pisos_BloqueB():
    # Destruye o resetea todo lo que se encuentra en la ventana anterior
    for ele in ventana.winfo_children():
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz=tk.Canvas(ventana)
    interfaz.pack()
    # En el label se carga la imagen
    label1=tk.Label(interfaz, image = Fondo_Pisos)
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    Boton_Regreso=tk.Button(ventana, text = "", command = Ventana_Opciones, width = 7, height = 1, font = Fuente_principal,
                              image = Imagen_Regresar, bg = "#FFFFFF", bd = 1, disabledforeground = None,  relief = "flat")
    Boton_Regreso.place(x = 830, y = 430, width = 74, height = 70)
    Boton_Piso1=tk.Button(ventana, text = "",  width = 7, height = 1, font = Fuente_principal,
                            image = Piso1, bg = "#FFFFFF", bd = 1, disabledforeground = None,  relief = "flat")
    Boton_Piso1.place(x = 150, y = 355, width = 200, height = 49)
    Boton_Piso2=tk.Button(ventana, text = "",  width = 7, height = 1, font = Fuente_principal,
                            image = Piso2, bg = "#FFFFFF", bd = 1, disabledforeground = None,  relief = "flat")
    Boton_Piso2.place(x = 480, y = 355, width = 200, height = 49)


def Ventana_Pisos_CasaE():
    # Destruye o resetea todo lo que se encuentra en la ventana anterior
    for ele in ventana.winfo_children():
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz=tk.Canvas(ventana)
    interfaz.pack()
    # En el label se carga la imagen
    label1=tk.Label(interfaz, image = Fondo_Pisos)
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    Boton_Regreso=tk.Button(ventana, text = "", command = Ventana_Opciones, width = 7, height = 1, font = Fuente_principal,
                              image = Imagen_Regresar, bg = "#FFFFFF", bd = 1, disabledforeground = None,  relief = "flat")
    Boton_Regreso.place(x = 830, y = 430, width = 74, height = 70)
    Boton_Piso1=tk.Button(ventana, text = "",  width = 7, height = 1, font = Fuente_principal,
                            image = Piso1, bg = "#FFFFFF", bd = 1, disabledforeground = None,  relief = "flat")
    Boton_Piso1.place(x = 98, y = 345, width = 200, height = 49)
    Boton_Piso2=tk.Button(ventana, text = "",  width = 7, height = 1, font = Fuente_principal,
                            image = Piso2, bg = "#FFFFFF", bd = 1, disabledforeground = None,  relief = "flat")
    Boton_Piso2.place(x = 328, y = 345, width = 200, height = 49)
    Boton_Piso3=tk.Button(ventana, text = "",  width = 7, height = 1, font = Fuente_principal,
                            image = Piso3, bg = "#FFFFFF", bd = 1, disabledforeground = None,  relief = "flat")
    Boton_Piso3.place(x = 558, y = 345, width = 200, height = 49)

MainMenu()
# El mainloop lleva el registro de todo lo que está sucediendo en la ventana:
ventana.mainloop()
