from cgitb import text
from enum import Enum
# Importamos las librerías para la GUI
from tkinter import *
import tkinter as tk
from tkinter import Label, Tk, ttk
from tkinter import Entry, StringVar, Toplevel, messagebox
import tkinter
import tkinter.font as tkFont
from turtle import color
from tkinter.__init__ import Label
from funcionalidades import *

# PARA CREAR LA INTERFAZ GRÁFICA
# Creamos la ventana principal
ventana = tk.Tk()
# Tamaño de la ventana:
Height = 918
Width = 520
ventana.geometry("918x520+230+100")  # para el tamaño y centrado de la interfaz
# Título de la ventana principal
ventana.title("Pc Explorer")
# Esto sirve para que el usuario no pueda agrandar la pantalla, ya que
# de lo contrario, se distorciona la interfaz
ventana.resizable(width=0, height=0)
# Creamos un Tipo de letra para colocarselo a los botones en las pantallas
Fuente_principal = tkFont.Font(family="Lucida Bright", size=11)
# Tipo de letra de la disponibilidad en los label
Fuente_Disponibilidad = tkFont.Font(family="Lucida Bright", size=30)
# tipo de letras de las preguntas de disponibilida en los label
Fuente_Disponibilidad_Preguntas = tkFont.Font(family="Lucida Bright", size=16)
# Cargamos todas las imagenes que vamos a necesitar en el trabajo
# Las guardamos en una variable de tipo PhotoImage
imagen = tk.PhotoImage(file="pp.png")  # Imagen de la pantalla principal
# Esta imagen la ubicamos en el label principal que será nuestro fondo
fondo = tk.Label(ventana, image=imagen).place(x=0, y=0)
credits = tk.PhotoImage(file="credits.png") #Imagen de los créditos
opciones = tk.PhotoImage(file="opciones.png") #Fondo de interfaz de las opciones
Explicacion = tk.PhotoImage(file="como funciona.png") #Fondo de la interfaz de explicación
Imagen_Regresar = tk.PhotoImage(file="boton regresar.png") # Imagen del boton regresar a la pág anterior
Imagen_Regresar_Creditos = tk.PhotoImage(file="regresar Creditos.png") #Imagen del boton regresar de los créditos
Fondo_Pisos = tk.PhotoImage(file="pisos.png") #Fondo de la interfaz de los pisos
Bloque_B = tk.PhotoImage(file="bloqueb.png") #Boton del Bloque B
Bloque_C = tk.PhotoImage(file="bloquec.png") #Boton del Bloque C
Bloque_D = tk.PhotoImage(file="bloqued.png") #Boton del Bloque D
Bloque_K = tk.PhotoImage(file="bloqueK.png") #Boton del Bloque K
Bloque_G = tk.PhotoImage(file="bloqueg.png") #Boton del Bloque G
Biblioteca = tk.PhotoImage(file="biblioteca.png") #Boton de Biblioteca
Casa_Estudio = tk.PhotoImage(file="casaestudio.png") #Boton de CasaEstudio
Piso1 = tk.PhotoImage(file="piso1.png") #Boton de los pisos del Bloque B y Casa Estudio 
Piso2 = tk.PhotoImage(file="piso2.png") #Boton de los pisos del Bloque B y Casa Estudio 
Piso3 = tk.PhotoImage(file="piso3.png") #Boton de los pisos del Bloque B y Casa Estudio 
Disponibles_G = tk.PhotoImage(file="disponibles.png") #Fondo de disponibilidad del bloque G
Disponibles_D = tk.PhotoImage(file="disD.png") #Fondo de disponibilidad del bloque D
Disponibles_K = tk.PhotoImage(file="disK.png") #Fondo de disponibilidad del bloque K
Disponibles_C = tk.PhotoImage(file="disC.png") #Fondo de disponibilidad del bloque C
Disponibles_Biblioteca = tk.PhotoImage(file="disbib.png") #Fondo de disponibilidad de Biblioteca
Disponibles_CasaE_1 = tk.PhotoImage(file="disCasa1.png") #Fondo de disponibilidad de CasaEstudio piso 1
Disponibles_CasaE_2 = tk.PhotoImage(file="disCasa2.png") #Fondo de disponibilidad de CasaEstudio piso 2
Disponibles_CasaE_3 = tk.PhotoImage(file="disCasa3.png") #Fondo de disponibilidad de CasaEstudio piso 3
Bloque_B_1 = tk.PhotoImage(file="disB1.png") #Fondo de disponibilidad de Bloque B piso 1
Bloque_B_2 = tk.PhotoImage(file="disB2.png") #Fondo de disponibilidad de Bloque B piso 2

# PARA CREAR LAS DEMÁS VENTANAS
# Cada función es un menú


def MainMenu():
    # Esta clase valida que el usuario no ingrese letras, solo números que hacen
    # referencia  a su código estudiantil

    prueba = Estudiantes(text)

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
                        validatecommand=(ventana.register(Estudiantes.validate_code), "%S"))
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

def Ventana_Disponibilidad_B_2():
    # Destruye o resetea todo lo que se encuentra en la ventana anterior
    for ele in ventana.winfo_children():
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Bloque_B_2)
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    piso = "2"
    bloque = "Bloque B"
    computadores = Disponibilidad()
    computadores.disponible(Ventana_Disponibilidad_B_2,
                            Fuente_Disponibilidad, piso, bloque)
    label4 = tk.Label(interfaz, text="¿Deseas reservar un computador?",
                      bg="#FFFFFF", font=Fuente_Disponibilidad_Preguntas)
    label4.place(x=420, y=340)
    
    Boton_Reserva = tk.Button(ventana, text="Hacer reserva", width=7, height=10, font=Fuente_principal, command=ReservaB2,
                              bg="#FFFFFF", disabledforeground=None)
    Boton_Reserva.place(x=560, y=400, width=110, height=50)
   
def ReservaB2():
    with open("file\dispo.txt", "r+"):
        pass
    Ventana_Disponibilidad_B_2()

def Ventana_Disponibilidad_B_1():
    # Destruye o resetea todo lo que se encuentra en la ventana anterior
    for ele in ventana.winfo_children():
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Bloque_B_1)
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    piso = "1"
    bloque = "Bloque B"
    computadores = Disponibilidad()
    computadores.disponible(Ventana_Disponibilidad_B_1,
                            Fuente_Disponibilidad, piso, bloque)
    label4 = tk.Label(interfaz, text="¿Deseas reservar un computador?",
                      bg="#FFFFFF", font=Fuente_Disponibilidad_Preguntas)
    label4.place(x=420, y=340)
    Boton_Reserva = tk.Button(ventana, text="Hacer reserva", width=7, height=10, font=Fuente_principal,
                              bg="#FFFFFF", disabledforeground=None)
    Boton_Reserva.place(x=560, y=400, width=110, height=50)


def Ventana_Disponibilidad_CasaE_3():
    # Destruye o resetea todo lo que se encuentra en la ventana anterior
    for ele in ventana.winfo_children():
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Disponibles_CasaE_3)
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    piso = "3"
    bloque = "Casa estudio"
    computadores = Disponibilidad()
    computadores.disponible(Ventana_Disponibilidad_CasaE_3,
                            Fuente_Disponibilidad, piso, bloque)
    label4 = tk.Label(interfaz, text="¿Deseas reservar un computador?",
                      bg="#FFFFFF", font=Fuente_Disponibilidad_Preguntas)
    label4.place(x=420, y=340)
    Boton_Reserva = tk.Button(ventana, text="Hacer reserva", width=7, height=10, font=Fuente_principal,
                              bg="#FFFFFF", disabledforeground=None)
    Boton_Reserva.place(x=560, y=400, width=110, height=50)


def Ventana_Disponibilidad_CasaE_2():
    # Destruye o resetea todo lo que se encuentra en la ventana anterior
    for ele in ventana.winfo_children():
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Disponibles_CasaE_2)
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    piso = "2"
    bloque = "Casa estudio"
    computadores = Disponibilidad()
    computadores.disponible(Ventana_Disponibilidad_CasaE_2,
                            Fuente_Disponibilidad, piso, bloque)
    label4 = tk.Label(interfaz, text="¿Deseas reservar un computador?",
                      bg="#FFFFFF", font=Fuente_Disponibilidad_Preguntas)
    label4.place(x=420, y=340)
    Boton_Reserva = tk.Button(ventana, text="Hacer reserva", width=7, height=10, font=Fuente_principal,
                              bg="#FFFFFF", disabledforeground=None)
    Boton_Reserva.place(x=560, y=400, width=110, height=50)


def Ventana_Disponibilidad_CasaE_1():
    # Destruye o resetea todo lo que se encuentra en la ventana anterior
    for ele in ventana.winfo_children():
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Disponibles_CasaE_1)
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    piso = "1"
    bloque = "Casa estudio"
    computadores = Disponibilidad()
    computadores.disponible(Ventana_Disponibilidad_CasaE_1,
                            Fuente_Disponibilidad, piso, bloque)
    label4 = tk.Label(interfaz, text="¿Deseas reservar un computador?",
                      bg="#FFFFFF", font=Fuente_Disponibilidad_Preguntas)
    label4.place(x=420, y=340)
    Boton_Reserva = tk.Button(ventana, text="Hacer reserva", width=7, height=10, font=Fuente_principal,
                              bg="#FFFFFF", disabledforeground=None)
    Boton_Reserva.place(x=560, y=400, width=110, height=50)


def Ventana_Disponibilidad_Biblioteca():
    # Destruye o resetea todo lo que se encuentra en la ventana anterior
    for ele in ventana.winfo_children():
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Disponibles_Biblioteca)
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    piso = "1"
    bloque = "Biblioteca"
    computadores = Disponibilidad()
    computadores.disponible(
        Ventana_Disponibilidad_Biblioteca, Fuente_Disponibilidad, piso, bloque)
    label4 = tk.Label(interfaz, text="¿Deseas reservar un computador?",
                      bg="#FFFFFF", font=Fuente_Disponibilidad_Preguntas)
    label4.place(x=420, y=300)
    Boton_Reserva = tk.Button(ventana, text="Hacer reserva", width=7, height=10, font=Fuente_principal,
                              bg="#FFFFFF", disabledforeground=None)
    Boton_Reserva.place(x=560, y=400, width=110, height=50)


def Ventana_Disponibilidad_C():
    # Destruye o resetea todo lo que se encuentra en la ventana anterior
    for ele in ventana.winfo_children():
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Disponibles_C)
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    piso = "1"
    bloque = "Bloque C"
    computadores = Disponibilidad()
    computadores.disponible(Ventana_Disponibilidad_C,
                            Fuente_Disponibilidad, piso, bloque)
    label4 = tk.Label(interfaz, text="¿Deseas reservar un computador?",
                      bg="#FFFFFF", font=Fuente_Disponibilidad_Preguntas)
    label4.place(x=420, y=300)
    Boton_Reserva = tk.Button(ventana, text="Hacer reserva", width=7, height=10, font=Fuente_principal,
                              bg="#FFFFFF", disabledforeground=None)
    Boton_Reserva.place(x=560, y=400, width=110, height=50)


def Ventana_Disponibilidad_k():
    # Destruye o resetea todo lo que se encuentra en la ventana anterior
    for ele in ventana.winfo_children():
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Disponibles_K)
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    piso = "4"
    bloque = "Bloque K"
    computadores = Disponibilidad()
    computadores.disponible(Ventana_Disponibilidad_k,
                            Fuente_Disponibilidad, piso, bloque)
    label4 = tk.Label(interfaz, text="¿Deseas reservar un computador?",
                      bg="#FFFFFF", font=Fuente_Disponibilidad_Preguntas)
    label4.place(x=420, y=300)
    Boton_Reserva = tk.Button(ventana, text="Hacer reserva", width=7, height=10, font=Fuente_principal,
                              bg="#FFFFFF", disabledforeground=None)
    Boton_Reserva.place(x=560, y=400, width=110, height=50)


def Ventana_Disponibilidad_G():
    # Destruye o resetea todo lo que se encuentra en la ventana anterior
    for ele in ventana.winfo_children():
        ele.destroy()
    # Se crea la nueva Interfaz
    interfazG = tk.Canvas(ventana)
    interfazG.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfazG, image=Disponibles_G)
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    piso = "5"
    bloque = "Bloque G"
    computadores = Disponibilidad()
    computadores.disponible(Ventana_Disponibilidad_G,
                            Fuente_Disponibilidad, piso, bloque)

    label4 = tk.Label(interfazG, text="¿Deseas reservar un computador?",
                      bg="#FFFFFF", font=Fuente_Disponibilidad_Preguntas)
    label4.place(x=420, y=300)
    Boton_Reserva = tk.Button(ventana, text="Hacer reserva", width=7, height=10, font=Fuente_principal,
                              bg="#FFFFFF", disabledforeground=None)
    Boton_Reserva.place(x=560, y=400, width=110, height=50)


def Ventana_Disponibilidad_D():
    # Destruye o resetea todo lo que se encuentra en la ventana anterior
    for ele in ventana.winfo_children():
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Disponibles_D)
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    piso = "1"
    bloque = "Bloque D"
    computadores = Disponibilidad()
    computadores.disponible(Ventana_Disponibilidad_D,
                            Fuente_Disponibilidad, piso, bloque)
    label4 = tk.Label(interfaz, text="¿Deseas reservar un computador?",
                      bg="#FFFFFF", font=Fuente_Disponibilidad_Preguntas)
    label4.place(x=420, y=300)
    Boton_Reserva = tk.Button(ventana, text="Hacer reserva", width=7, height=10, font=Fuente_principal,
                              bg="#FFFFFF", disabledforeground=None)
    Boton_Reserva.place(x=560, y=400, width=110, height=50)


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
    Boton_PisoC = tk.Button(ventana, text="Bloque C", width=7, height=1, font=Fuente_principal, command=Ventana_Disponibilidad_C,
                            image=Bloque_C, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_PisoC.place(x=50, y=400, width=200, height=49)
    Boton_PisoD = tk.Button(ventana, text="Bloque D", width=7, height=1, font=Fuente_principal, command=Ventana_Disponibilidad_D,
                            image=Bloque_D, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_PisoD.place(x=270, y=305, width=200, height=49)
    Boton_PisoK = tk.Button(ventana, text="Bloque K", width=7, height=1, font=Fuente_principal, command=Ventana_Disponibilidad_k,
                            image=Bloque_K, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_PisoK.place(x=270, y=400, width=200, height=49)
    Boton_Biblioteca = tk.Button(ventana, text="Biblioteca", width=7, height=1, command=Ventana_Disponibilidad_Biblioteca,
                                 image=Biblioteca, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Biblioteca.place(x=490, y=400, width=200, height=49)
    Boton_CasaE = tk.Button(ventana, text="Casa Estudio", width=7, height=1, command=Ventana_Pisos_CasaE,
                            image=Casa_Estudio, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_CasaE.place(x=710, y=355, width=200, height=49)
    Boton_PisoG = tk.Button(ventana, text="Bloque G", width=7, height=1, font=Fuente_principal, command=Ventana_Disponibilidad_G,
                            image=Bloque_G, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_PisoG.place(x=490, y=305, width=200, height=49)
    Boton_CasaE = tk.Button(ventana, text="Casa Estudio", width=7, height=1, command=Ventana_Pisos_CasaE,
                            image=Casa_Estudio, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_CasaE.place(x=710, y=355, width=200, height=49)


def Ventana_Explicacion():
    # Destruye o resetea todo lo que se encuentra en la ventana anterior
    for ele in ventana.winfo_children():
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz_Explicacion = tk.Canvas(ventana)
    interfaz_Explicacion.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz_Explicacion, image=Explicacion)
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    Boton_Regreso = tk.Button(ventana, text="", command=MainMenu, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Regreso.place(x=-3, y=467, width=74, height=70)


def Ventana_Pisos_BloqueB():
    # Destruye o resetea todo lo que se encuentra en la ventana anterior
    for ele in ventana.winfo_children():
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Fondo_Pisos)
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    Boton_Piso1 = tk.Button(ventana, text="",  width=7, height=1, font=Fuente_principal, command=Ventana_Disponibilidad_B_1,
                            image=Piso1, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Piso1.place(x=150, y=355, width=200, height=49)
    Boton_Piso2 = tk.Button(ventana, text="",  width=7, height=1, font=Fuente_principal, command=Ventana_Disponibilidad_B_2,
                            image=Piso2, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Piso2.place(x=480, y=355, width=200, height=49)


def Ventana_Pisos_CasaE():
    # Destruye o resetea todo lo que se encuentra en la ventana anterior
    for ele in ventana.winfo_children():
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Fondo_Pisos)
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    Boton_Piso1 = tk.Button(ventana, text="",  width=7, height=1, font=Fuente_principal, command=Ventana_Disponibilidad_CasaE_1,
                            image=Piso1, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Piso1.place(x=98, y=345, width=200, height=49)
    Boton_Piso2 = tk.Button(ventana, text="",  width=7, height=1, font=Fuente_principal, command=Ventana_Disponibilidad_CasaE_2,
                            image=Piso2, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Piso2.place(x=328, y=345, width=200, height=49)
    Boton_Piso3 = tk.Button(ventana, text="",  width=7, height=1, font=Fuente_principal, command=Ventana_Disponibilidad_CasaE_3,
                            image=Piso3, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Piso3.place(x=558, y=345, width=200, height=49)


MainMenu()
# El mainloop lleva el registro de todo lo que está sucediendo en la ventana:
ventana.mainloop()