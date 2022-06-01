# En esta parte del código se importan las librerías a utilizar
# Librería que lanza un el número de referencia al azar
import random
# GUI de python que utilizaremos para la interfaz
import tkinter as tk
# Esta librería nos permite cambiar el tipo de fuente en los
# label y botones
import tkinter.font as tkFont
# no se q es esto xd
from cgitb import text
# Esta librería nos permite obtener el tiempo y fecha actual,
# la cual es necesaria para mostrarla en el comprobante
from datetime import datetime
# Importamos las librerías para la GUI
# Entry y StringVar son de Tkinter y es un cuadro de texto en que el usuario
# ingresa su codigo para después poder validarlo
from tkinter import Entry, StringVar
# no c q es esto
from turtle import color
# Importamos el archivo de funcionalidades para poder obtener
# todas las clases necesarias que son utilizadas en el código
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
# Tipo de letra de las preguntas de disponibilida en los label
Fuente_Disponibilidad_Preguntas = tkFont.Font(family="Lucida Bright", size=16)
# Tipo de letra y tamaño de estas en el comprobante en los label
Fuente_Comprobante = tkFont.Font(family="Lucida Bright", size=11)
# Tipo de letra cuando no hay computadores disponibles en un lugar
Fuente_No_Disponible = tkFont.Font(family="Lucida Bright", size=11)
# Tipo de letra del botón que redirige al mapa de los bloques
Fuente_mapa = tkFont.Font(family="Lucida Bright", size=10)
# Cargamos todas las imagenes que vamos a necesitar en el trabajo
# Las guardamos en una variable de tipo PhotoImage
imagen = tk.PhotoImage(file="pp.png")  # Imagen de la pantalla principal
# Esta imagen la ubicamos en el label principal que será nuestro fondo
fondo = tk.Label(ventana, image=imagen).place(x=0, y=0)
credits = tk.PhotoImage(file="credits.png")  # Imagen de los créditos
# Fondo de interfaz de las opciones
opciones = tk.PhotoImage(file="opciones.png")
# Fondo de la interfaz de explicación
Explicacion = tk.PhotoImage(file="como funciona.png")
# Imagen del boton regresar a la pág anterior
Imagen_Regresar = tk.PhotoImage(file="boton regresar.png")
# Imagen del boton regresar de los créditos
Imagen_Regresar_Creditos = tk.PhotoImage(file="regresar Creditos.png")
# Fondo de la interfaz de los pisos
Fondo_Pisos = tk.PhotoImage(file="pisos.png")
Bloque_B = tk.PhotoImage(file="bloqueb.png")  # Foto del Boton del Bloque B
Bloque_C = tk.PhotoImage(file="bloquec.png")  # Foto del Boton del Bloque C
Bloque_D = tk.PhotoImage(file="bloqued.png")  # Foto del Boton del Bloque D
Bloque_K = tk.PhotoImage(file="bloqueK.png")  # Foto del Boton del Bloque K
Bloque_G = tk.PhotoImage(file="bloqueg.png")  # Foto del Boton del Bloque G
# Foto del Boton de Biblioteca
Biblioteca = tk.PhotoImage(file="biblioteca.png")
# Foto del Boton de CasaEstudio
Casa_Estudio = tk.PhotoImage(file="casaestudio.png")
# Boton de los pisos del Bloque B y Casa Estudio
Piso1 = tk.PhotoImage(file="piso1.png")
# Boton de los pisos del Bloque B y Casa Estudio
Piso2 = tk.PhotoImage(file="piso2.png")
# Boton de los pisos del Bloque B y Casa Estudio
Piso3 = tk.PhotoImage(file="piso3.png")
# Fondo de disponibilidad del bloque G
Disponibles_G = tk.PhotoImage(file="disponibles.png")
# Fondo de disponibilidad del bloque D
Disponibles_D = tk.PhotoImage(file="disD.png")
# Fondo de disponibilidad del bloque K
Disponibles_K = tk.PhotoImage(file="disK.png")
# Fondo de disponibilidad del bloque C
Disponibles_C = tk.PhotoImage(file="disC.png")
# Fondo de disponibilidad de Biblioteca
Disponibles_Biblioteca = tk.PhotoImage(file="disbib.png")
# Fondo de disponibilidad de CasaEstudio piso 1
Disponibles_CasaE_1 = tk.PhotoImage(file="disCasa1.png")
# Fondo de disponibilidad de CasaEstudio piso 2
Disponibles_CasaE_2 = tk.PhotoImage(file="disCasa2.png")
# Fondo de disponibilidad de CasaEstudio piso 3
Disponibles_CasaE_3 = tk.PhotoImage(file="disCasa3.png")
map = tk.PhotoImage(file="bloques.png")
# Fondo de disponibilidad de Bloque B piso 1
Bloque_B_1 = tk.PhotoImage(file="disB1.png")
# Fondo de disponibilidad de Bloque B piso 2
Bloque_B_2 = tk.PhotoImage(file="disB2.png")
# Comprobante = tk.PhotoImage(file="reserva.png") #Fondo de la reserva de los computadores
# Fondo de la reserva de los computadores
Comprobante = tk.PhotoImage(file="com.png")
# datetime es una función de python que genera la fecha, hora, minutos y segundos actuales.
now = datetime.now()
# Convertimos en str la hora generada por la función de python.
hora = str(now.hour)
# Convertimos en str los minutos generados por la función de python.
minuto = str(now.minute)
# Convertimos en str los segundos generados por la función de python.
segundo = str(now.second)

# PARA CREAR LAS DEMÁS VENTANAS
# Cada función es un menú

# este es el método del menú principal, todo lo que se encuentra aquí es lo
# que se muestra en la pantalla principal de la aplicación.


def MainMenu():
    # Este for es el encargado de resetear la pantalla en la que el usuario
    # se encuentra cuando uno se devuelva al menu principal
    for ele in ventana.winfo_children():
        # Quiere decir que se destruye la imagen
        ele.destroy()
    # Label que muestra la imagen de la pantalla principal
    label2 = tk.Label(ventana, image=imagen)
    # .pack() quiere decir que el label tendrá el mismo tamaño de la ventana
    label2.pack()
    # Botón creditos que hace que se cambie a la ventana de créditos
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, ancho, alto, fuente de la letra,
    # el comando del botón, color de fondo del botón, borde 1 para desaparecerlo.
    Boton_Creditos = tk.Button(ventana, text="Créditos", width=8, height=1, font=Fuente_principal,
                               command=Ventana_creditos, bg="#FFFFFF",  bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón
    Boton_Creditos.place(x=618, y=65)
    # Botón explicacion que hace que se cambie a la ventana de "¿Cómo funciona?"
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, ancho, alto, fuente de la letra,
    # el comando del botón, color de fondo del botón, borde 1 para desaparecerlo.
    Boton_Explicacion = tk.Button(ventana, text="¿Cómo funciona?", width=20, height=1, font=Fuente_principal,
                                  command=Ventana_Explicacion, bg="#FFFFFF",  bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón
    Boton_Explicacion.place(x=160, y=65)
    # Para crear el textfile en el que el usuario ingresará su código
    codigo = StringVar()
    # Aquí se valida lo que el usuario ingresa, Entry es el cuadro de diálogo
    # Orden de parámetros: Ventana a mostrar el cuadro de texto, indicamos cual es la StringVar donde
    # queremos que deje el texto escrito por el usuario, Color de fondo, ancho,  validate le indica a la caja qué
    # tipo de validación estamos buscando: "key" corresponde al ingreso de texto, Comando a validar, cadena que denota
    # qué información queremos recibir como argumento en dicha función ("%S" representa el texto ingresado por el usuario)
    codigoEntry = Entry(ventana, textvariable=codigo, bg="#ECE7E6", width=35, validate="key",
                        validatecommand=(ventana.register(Estudiantes.validate_code), "%S"))
    # Ubicación (x,y) y ancho alto del cuadro de texto
    codigoEntry.place(x=473, y=385, width=100, height=30)

    # Función que Valida el código del usuario
    def login():
        # Comvertimos esta variable en global para poder usar su contenido fuera de este método
        global Validar_codigo
        # Con .get obtenemos lo que el usuario ingresó.
        Validar_codigo = codigoEntry.get()
        # Creamos una condición para validar que el usuario si ingresó algo
        if(Validar_codigo == ""):
            # En caso de que el usuario dio en el boton acceder pero sin ningun campo, entonces aparecerá un label
            # que diga que no puede ingresar sino que debe ingresar algo.
            # Los parámetros de este label son los mismos que los anteriores.
            Error = tk.Label(ventana, text="Error, campos vacíos, intente de nuevo.",
                             font=Fuente_principal, disabledforeground=None, bg="#FFFFFF")
            # Ubicación (x,y) del label
            Error.place(x=600, y=385)
        else:  # si no esta vacío entonces se mira para ver si el valor es menor que la cantidad de dígitos necesaria
            # de un código estudiantil, pero antes este valor se convierte en int ya que esta en str
            if (int(Validar_codigo) < 1000000):
                # Aparecerá un label
                # que diga que no puede ingresar sino que debe ingresar algo.
                # Los parámetros de este label son los mismos que los anteriores.
                Error = tk.Label(ventana, text="Error, código no encontrado.",
                                 font=Fuente_principal, disabledforeground=None, bg="#FFFFFF")
                # Ubicación (x,y) del label
                Error.place(x=600, y=385)
            else:  # Por último se busca que el código este en el archivo txt
                if(Validar_codigo in readfile):
                    # Si está entonces se despliega la ventana de los bloques
                    Ventana_Opciones()
                else:
                    # Aparecerá un label
                    # que diga que no puede ingresar sino que debe ingresar algo.
                    # Los parámetros de este label son los mismos que los anteriores.
                    Error = tk.Label(ventana, text="Error, código no encontrado.",
                                     font=Fuente_principal, disabledforeground=None, bg="#FFFFFF")
                    # Ubicación (x,y) del label
                    Error.place(x=600, y=385)
        return Validar_codigo

    # Abrimos el archivo txt que contiene los códigos estudiantiles
    filename = ("file/codigos.txt")
    # read() lee todos los códigos del txt
    with open(filename) as file:
        readfile = file.read()

    # boton para ingresar o acceder
    # Los parámetros de este label son los mismos que los anteriores.
    Button_login = tk.Button(ventana, text="Acceder", width=7,
                             height=1, command=login, font=Fuente_principal)
    # Ubicación (x,y) de los botones
    Button_login.place(x=500, y=430)

# En este método se encuentra todo lo relacionado a las reservas realizadas en el
# Bloque B piso 2


def Reserva_Bloque_B_2():
    # Generamos un número random que sería el número de referencia del comprobante de reserva
    numero = random.randint(100000, 999999)
    # Como necesitamos guardar este número en un txt se debe convertir en string
    nreserva = str(numero)
    # Creamos un objeto de la clase Nreferencia que es la encargada de guardar este número en el txt
    numeroR = Nreferencia()
    # Los parámetros: Nombre de la variable que tiene el código a validar y el numero de reserva
    numeroR.Referencia(Validar_codigo, nreserva)
    # Cremoa un objeto de la clase Reserva, cuyos parámetros son el bloque y el piso
    reserva = Reserva("Bloque B", "2")
    # Método de la clase reserva cuyos parámetros son la ventana, tipo de fuente, nombre imagen del comprobante, nombre del lugar,
    # fecha, hora, tipo de fuente del comprobante, código del estudiante y el número de la reserva
    reserva.Res(Ventana_Disponibilidad_B_2, Fuente_Disponibilidad, Comprobante, "Bloque B, segundo piso", now.date(
    ), hora + ":" + minuto + ":" + segundo, Fuente_Comprobante, Validar_codigo, nreserva)

# En este método se encuentra todo lo relacionado con el Bloque B piso 2, ya sea interfaz o disponibilidad


def Ventana_Disponibilidad_B_2():
    # Este for es el encargado de resetear la pantalla en la que el usuario
    # se encontraba anteriormente y poder mostrar la actual
    for ele in ventana.winfo_children():
        # Quiere decir que se destruye la imagen
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    # El lugar será en toda la interfaz
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Bloque_B_2)
    # Posición en toda la pantalla
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra,
    # imagen del botón, color de fondo del botón, borde 1 para desaparecerlo
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    # Label en el que se mostrará un mensaje al usuario sobre las reservas
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el label,
    # color de fondo, fuente de la letra
    label4 = tk.Label(interfaz, text="¿Deseas reservar un computador?",
                      bg="#FFFFFF", font=Fuente_Disponibilidad_Preguntas)
    # Ubicación (x,y) del label
    label4.place(x=420, y=340)
    # Boton para ver el mapa de la u
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra, comando,
    # color de fondo del botón, borde 1 para desaparecerlo
    Boton_Mapa = tk.Button(ventana, text="Ver Ubicación\n en el mapa", font=Fuente_mapa, command=Ventana_Mapa,
                           bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Mapa.place(x=188, y=55, width=110, height=50)
    # Boton para realizar reserva
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra, comando,
    # color de fondo del botón, borde 1 para desaparecerlo
    Boton_Reserva = tk.Button(ventana, text="Hacer reserva", font=Fuente_principal, command=Reserva_Bloque_B_2,
                              bg="#FFFFFF", disabledforeground=None)
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Reserva.place(x=560, y=400, width=110, height=50)
    # Creamos un obejto de la clase de disponibilidad que muestra la disponibilidad de los computadores
    # en el lugar que el usuario escoja
    computadores = Disponibilidad()
    # Parámetros del método disponible: Ventana a mostrar, fuente de la letra, piso, lugar, fuente si no llega
    # a tener computadores disponibles
    computadores.disponible(Ventana_Disponibilidad_B_2,
                            Fuente_Disponibilidad, "2", "Bloque B", Fuente_No_Disponible)

# En este método se encuentra todo lo relacionado a las reservas realizadas en el
# Bloque B piso 1


def Reserva_BLoque_B_1():
    # Generamos un número random que sería el número de referencia del comprobante de reserva
    numero = random.randint(100000, 999999)
    # Como necesitamos guardar este número en un txt se debe convertir en string
    nreserva = str(numero)
    # Creamos un objeto de la clase Nreferencia que es la encargada de guardar este número en el txt
    numeroR = Nreferencia()
    # Los parámetros: Nombre de la variable que tiene el código a validar y el numero de reserva
    numeroR.Referencia(Validar_codigo, nreserva)
    # Cremoa un objeto de la clase Reserva, cuyos parámetros son el bloque y el piso
    reserva = Reserva("Bloque B", "1")
    # Método de la clase reserva cuyos parámetros son la ventana, tipo de fuente, nombre imagen del comprobante, nombre del lugar,
    # fecha, hora, tipo de fuente del comprobante, código del estudiante y el número de la reserva
    reserva.Res(Ventana_Disponibilidad_B_1, Fuente_Disponibilidad, Comprobante, "Bloque B, primer piso", now.date(
    ), hora + ":" + minuto + ":" + segundo, Fuente_Comprobante, Validar_codigo, nreserva)

# En este método se encuentra todo lo relacionado con el Bloque B piso 1, ya sea interfaz o disponibilidad


def Ventana_Disponibilidad_B_1():
    # Este for es el encargado de resetear la pantalla en la que el usuario
    # se encontraba anteriormente y poder mostrar la actual
    for ele in ventana.winfo_children():
        # Quiere decir que se destruye la imagen
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    # El lugar será en toda la interfaz
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Bloque_B_1)
    # Posición en toda la pantalla
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra,
    # imagen del botón, color de fondo del botón, borde 1 para desaparecerlo
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    # Label en el que se mostrará un mensaje al usuario sobre las reservas
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el label,
    # color de fondo, fuente de la letra
    label4 = tk.Label(interfaz, text="¿Deseas reservar un computador?",
                      bg="#FFFFFF", font=Fuente_Disponibilidad_Preguntas)
    # Ubicación (x,y) del label
    label4.place(x=420, y=340)
    # Boton para ver el mapa de la u
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra, comando,
    # color de fondo del botón, borde 1 para desaparecerlo
    Boton_Mapa = tk.Button(ventana, text="Ver Ubicación\n en el mapa", width=7, height=10, font=Fuente_mapa, command=Ventana_Mapa,
                           bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Mapa.place(x=188, y=55, width=110, height=50)
    # Boton para realizar reserva
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra, comando,
    # color de fondo del botón, borde 1 para desaparecerlo
    Boton_Reserva = tk.Button(ventana, text="Hacer reserva", width=7, height=10, font=Fuente_principal, command=Reserva_BLoque_B_1,
                              bg="#FFFFFF", disabledforeground=None)
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Reserva.place(x=560, y=400, width=110, height=50)
    # Creamos un obejto de la clase de disponibilidad que muestra la disponibilidad de los computadores
    # en el lugar que el usuario escoja
    computadores = Disponibilidad()
    # Parámetros del método disponible: Ventana a mostrar, fuente de la letra, piso, lugar, fuente si no llega
    # a tener computadores disponibles
    computadores.disponible(Ventana_Disponibilidad_B_1,
                            Fuente_Disponibilidad, "1", "Bloque B", Fuente_No_Disponible)

# En este método se encuentra todo lo relacionado a las reservas realizadas en
# Casa Estudio piso 3


def Reserva_Casa_E_3():
    # Generamos un número random que sería el número de referencia del comprobante de reserva
    numero = random.randint(100000, 999999)
    # Como necesitamos guardar este número en un txt se debe convertir en string
    nreserva = str(numero)
    # Creamos un objeto de la clase Nreferencia que es la encargada de guardar este número en el txt
    numeroR = Nreferencia()
    # Los parámetros: Nombre de la variable que tiene el código a validar y el numero de reserva
    numeroR.Referencia(Validar_codigo, nreserva)
    # Cremoa un objeto de la clase Reserva, cuyos parámetros son el bloque y el piso
    reserva = Reserva("Casa estudio", "3")
    # Método de la clase reserva cuyos parámetros son la ventana, tipo de fuente, nombre imagen del comprobante, nombre del lugar,
    # fecha, hora, tipo de fuente del comprobante, código del estudiante y el número de la reserva
    reserva.Res(Ventana_Disponibilidad_CasaE_3, Fuente_Disponibilidad, Comprobante, "Casa Estudio, tercer piso", now.date(
    ), hora + ":" + minuto + ":" + segundo, Fuente_Comprobante, Validar_codigo, nreserva)

# En este método se encuentra todo lo relacionado con Casa Estudio piso 3, ya sea interfaz o disponibilidad


def Ventana_Disponibilidad_CasaE_3():
    # Este for es el encargado de resetear la pantalla en la que el usuario
    # se encontraba anteriormente y poder mostrar la actual
    for ele in ventana.winfo_children():
        # Quiere decir que se destruye la imagen
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    # El lugar será en toda la interfaz
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Disponibles_CasaE_3)
    # Posición en toda la pantalla
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra,
    # imagen del botón, color de fondo del botón, borde 1 para desaparecerlo
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
   # Label en el que se mostrará un mensaje al usuario sobre las reservas
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el label,
    # color de fondo, fuente de la letra
    label4 = tk.Label(interfaz, text="¿Deseas reservar un computador?",
                      bg="#FFFFFF", font=Fuente_Disponibilidad_Preguntas)
    # Ubicación (x,y) del label
    label4.place(x=420, y=340)
    # Boton para ver el mapa de la u
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra, comando,
    # color de fondo del botón, borde 1 para desaparecerlo
    Boton_Mapa = tk.Button(ventana, text="Ver Ubicación\n en el mapa", width=7, height=10, font=Fuente_mapa, command=Ventana_Mapa,
                           bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Mapa.place(x=188, y=55, width=110, height=50)
    # Boton para realizar reserva
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra, comando,
    # color de fondo del botón, borde 1 para desaparecerlo
    Boton_Reserva = tk.Button(ventana, text="Hacer reserva", width=7, height=10, font=Fuente_principal, command=Reserva_BLoque_B_1,
                              bg="#FFFFFF", disabledforeground=None)
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Reserva.place(x=560, y=400, width=110, height=50)
    # Creamos un obejto de la clase de disponibilidad que muestra la disponibilidad de los computadores
    # en el lugar que el usuario escoja
    computadores = Disponibilidad()
    # Parámetros del método disponible: Ventana a mostrar, fuente de la letra, piso, lugar, fuente si no llega
    # a tener computadores disponibles
    computadores.disponible(Ventana_Disponibilidad_CasaE_3,
                            Fuente_Disponibilidad, "3", "Casa estudio", Fuente_No_Disponible)

# En este método se encuentra todo lo relacionado a las reservas realizadas en
# Casa Estudio piso 2


def Reserva_Casa_E_2():
    # Generamos un número random que sería el número de referencia del comprobante de reserva
    numero = random.randint(100000, 999999)
    # Como necesitamos guardar este número en un txt se debe convertir en string
    nreserva = str(numero)
    # Creamos un objeto de la clase Nreferencia que es la encargada de guardar este número en el txt
    numeroR = Nreferencia()
    # Los parámetros: Nombre de la variable que tiene el código a validar y el numero de reserva
    numeroR.Referencia(Validar_codigo, nreserva)
    # Cremoa un objeto de la clase Reserva, cuyos parámetros son el bloque y el piso
    reserva = Reserva("Casa estudio", "2")
    # Método de la clase reserva cuyos parámetros son la ventana, tipo de fuente, nombre imagen del comprobante, nombre del lugar,
    # fecha, hora, tipo de fuente del comprobante, código del estudiante y el número de la reserva
    reserva.Res(Ventana_Disponibilidad_CasaE_2, Fuente_Disponibilidad, Comprobante, "Casa Estudio, segundo piso", now.date(
    ), hora + ":" + minuto + ":" + segundo, Fuente_Comprobante, Validar_codigo, nreserva)

# En este método se encuentra todo lo relacionado con Casa Estudio piso 2, ya sea interfaz o disponibilidad


def Ventana_Disponibilidad_CasaE_2():
    # Este for es el encargado de resetear la pantalla en la que el usuario
    # se encontraba anteriormente y poder mostrar la actual
    for ele in ventana.winfo_children():
        # Quiere decir que se destruye la imagen
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    # El lugar será en toda la interfaz
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Disponibles_CasaE_2)
    # Posición en toda la pantalla
    label1.pack()
   # Boton para regresarte al menú principal y para quitarle los bordes
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra,
    # imagen del botón, color de fondo del botón, borde 1 para desaparecerlo
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    # Label en el que se mostrará un mensaje al usuario sobre las reservas
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el label,
    # color de fondo, fuente de la letra
    label4 = tk.Label(interfaz, text="¿Deseas reservar un computador?",
                      bg="#FFFFFF", font=Fuente_Disponibilidad_Preguntas)
    # Ubicación (x,y) del label
    label4.place(x=420, y=340)
    # Boton para ver el mapa de la u
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra, comando,
    # color de fondo del botón, borde 1 para desaparecerlo
    Boton_Mapa = tk.Button(ventana, text="Ver Ubicación\n en el mapa", width=7, height=10, font=Fuente_mapa, command=Ventana_Mapa,
                           bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Mapa.place(x=188, y=55, width=110, height=50)
    # Boton para realizar reserva
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra, comando,
    # color de fondo del botón, borde 1 para desaparecerlo
    Boton_Reserva = tk.Button(ventana, text="Hacer reserva", width=7, height=10, font=Fuente_principal, command=Reserva_BLoque_B_1,
                              bg="#FFFFFF", disabledforeground=None)
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Reserva.place(x=560, y=400, width=110, height=50)
    # Creamos un obejto de la clase de disponibilidad que muestra la disponibilidad de los computadores
    # en el lugar que el usuario escoja
    computadores = Disponibilidad()
    # Parámetros del método disponible: Ventana a mostrar, fuente de la letra, piso, lugar, fuente si no llega
    # a tener computadores disponibles
    computadores.disponible(Ventana_Disponibilidad_CasaE_2,
                            Fuente_Disponibilidad, "2", "Casa estudio", Fuente_No_Disponible)

# En este método se encuentra todo lo relacionado a las reservas realizadas en
# Casa Estudio piso 1


def Reserva_Casa_E_1():
    # Generamos un número random que sería el número de referencia del comprobante de reserva
    numero = random.randint(100000, 999999)
    # Como necesitamos guardar este número en un txt se debe convertir en string
    nreserva = str(numero)
    # Creamos un objeto de la clase Nreferencia que es la encargada de guardar este número en el txt
    numeroR = Nreferencia()
    # Los parámetros: Nombre de la variable que tiene el código a validar y el numero de reserva
    numeroR.Referencia(Validar_codigo, nreserva)
    # Cremoa un objeto de la clase Reserva, cuyos parámetros son el bloque y el piso
    reserva = Reserva("Casa estudio", "1")
    # Método de la clase reserva cuyos parámetros son la ventana, tipo de fuente, nombre imagen del comprobante, nombre del lugar,
    # fecha, hora, tipo de fuente del comprobante, código del estudiante y el número de la reserva
    reserva.Res(Ventana_Disponibilidad_CasaE_1, Fuente_Disponibilidad, Comprobante, "Casa Estudio, primer piso", now.date(
    ), hora + ":" + minuto + ":" + segundo, Fuente_Comprobante, Validar_codigo, nreserva)

# En este método se encuentra todo lo relacionado con Casa Estudio piso 1, ya sea interfaz o disponibilidad


def Ventana_Disponibilidad_CasaE_1():
    # Este for es el encargado de resetear la pantalla en la que el usuario
    # se encontraba anteriormente y poder mostrar la actual
    for ele in ventana.winfo_children():
        # Quiere decir que se destruye la imagen
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    # El lugar será en toda la interfaz
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Disponibles_CasaE_1)
    # Posición en toda la pantalla
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra,
    # imagen del botón, color de fondo del botón, borde 1 para desaparecerlo
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    # Label en el que se mostrará un mensaje al usuario sobre las reservas
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el label,
    # color de fondo, fuente de la letra
    label4 = tk.Label(interfaz, text="¿Deseas reservar un computador?",
                      bg="#FFFFFF", font=Fuente_Disponibilidad_Preguntas)
    # Ubicación (x,y) del label
    label4.place(x=420, y=340)
    # Boton para ver el mapa de la u
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra, comando,
    # color de fondo del botón, borde 1 para desaparecerlo
    Boton_Mapa = tk.Button(ventana, text="Ver Ubicación\n en el mapa", width=7, height=10, font=Fuente_mapa, command=Ventana_Mapa,
                           bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Mapa.place(x=188, y=55, width=110, height=50)
    # Boton para realizar reserva
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra, comando,
    # color de fondo del botón, borde 1 para desaparecerlo
    Boton_Reserva = tk.Button(ventana, text="Hacer reserva", width=7, height=10, font=Fuente_principal, command=Reserva_Casa_E_1,
                              bg="#FFFFFF", disabledforeground=None)
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Reserva.place(x=560, y=400, width=110, height=50)
    # Creamos un obejto de la clase de disponibilidad que muestra la disponibilidad de los computadores
    # en el lugar que el usuario escoja
    computadores = Disponibilidad()
    # Parámetros del método disponible: Ventana a mostrar, fuente de la letra, piso, lugar, fuente si no llega
    # a tener computadores disponibles
    computadores.disponible(Ventana_Disponibilidad_CasaE_1,
                            Fuente_Disponibilidad, "1", "Casa estudio", Fuente_No_Disponible)

# En este método se encuentra todo lo relacionado a las reservas realizadas en
# Biblioteca piso 1


def Reserva_Biblioteca():
   # Generamos un número random que sería el número de referencia del comprobante de reserva
    numero = random.randint(100000, 999999)
    # Como necesitamos guardar este número en un txt se debe convertir en string
    nreserva = str(numero)
    # Creamos un objeto de la clase Nreferencia que es la encargada de guardar este número en el txt
    numeroR = Nreferencia()
    # Los parámetros: Nombre de la variable que tiene el código a validar y el numero de reserva
    numeroR.Referencia(Validar_codigo, nreserva)
    # Cremoa un objeto de la clase Reserva, cuyos parámetros son el bloque y el piso
    reserva = Reserva("Biblioteca", "1")
    # Método de la clase reserva cuyos parámetros son la ventana, tipo de fuente, nombre imagen del comprobante, nombre del lugar,
    # fecha, hora, tipo de fuente del comprobante, código del estudiante y el número de la reserva
    reserva.Res(Ventana_Disponibilidad_Biblioteca, Fuente_Disponibilidad, Comprobante, "Biblioteca, primer piso", now.date(
    ), hora + ":" + minuto + ":" + segundo, Fuente_Comprobante, Validar_codigo, nreserva)

# En este método se encuentra todo lo relacionado con la Biblioteca piso 1, ya sea interfaz o disponibilidad


def Ventana_Disponibilidad_Biblioteca():
    # Este for es el encargado de resetear la pantalla en la que el usuario
    # se encontraba anteriormente y poder mostrar la actual
    for ele in ventana.winfo_children():
        # Quiere decir que se destruye la imagen
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    # El lugar será en toda la interfaz
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Disponibles_Biblioteca)
    # Posición en toda la pantalla
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra,
    # imagen del botón, color de fondo del botón, borde 1 para desaparecerlo
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    # Label en el que se mostrará un mensaje al usuario sobre las reservas
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el label,
    # color de fondo, fuente de la letra
    label4 = tk.Label(interfaz, text="¿Deseas reservar un computador?",
                      bg="#FFFFFF", font=Fuente_Disponibilidad_Preguntas)
    # Ubicación (x,y) del label
    label4.place(x=420, y=340)
    # Boton para ver el mapa de la u
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra, comando,
    # color de fondo del botón, borde 1 para desaparecerlo
    Boton_Mapa = tk.Button(ventana, text="Ver Ubicación\n en el mapa", width=7, height=10, font=Fuente_mapa, command=Ventana_Mapa,
                           bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Mapa.place(x=188, y=55, width=110, height=50)
    # Boton para realizar reserva
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra, comando,
    # color de fondo del botón, borde 1 para desaparecerlo
    Boton_Reserva = tk.Button(ventana, text="Hacer reserva", width=7, height=10, font=Fuente_principal, command=Reserva_Biblioteca,
                              bg="#FFFFFF", disabledforeground=None)
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Reserva.place(x=560, y=400, width=110, height=50)
    # Creamos un obejto de la clase de disponibilidad que muestra la disponibilidad de los computadores
    # en el lugar que el usuario escoja
    computadores = Disponibilidad()
    # Parámetros del método disponible: Ventana a mostrar, fuente de la letra, piso, lugar, fuente si no llega
    # a tener computadores disponibles
    computadores.disponible(
        Ventana_Disponibilidad_Biblioteca, Fuente_Disponibilidad, "1", "Biblioteca", Fuente_No_Disponible)

# En este método se encuentra todo lo relacionado a las reservas realizadas en el
# Bloque C piso 1


def Reserva_Bloque_C_1():
    # Generamos un número random que sería el número de referencia del comprobante de reserva
    numero = random.randint(100000, 999999)
    # Como necesitamos guardar este número en un txt se debe convertir en string
    nreserva = str(numero)
    # Creamos un objeto de la clase Nreferencia que es la encargada de guardar este número en el txt
    numeroR = Nreferencia()
    # Los parámetros: Nombre de la variable que tiene el código a validar y el numero de reserva
    numeroR.Referencia(Validar_codigo, nreserva)
    # Cremoa un objeto de la clase Reserva, cuyos parámetros son el bloque y el piso
    reserva = Reserva("Bloque C", "1")
    # Método de la clase reserva cuyos parámetros son la ventana, tipo de fuente, nombre imagen del comprobante, nombre del lugar,
    # fecha, hora, tipo de fuente del comprobante, código del estudiante y el número de la reserva
    reserva.Res(Ventana_Disponibilidad_C, Fuente_Disponibilidad, Comprobante, "Bloque C, primer piso", now.date(
    ), hora + ":" + minuto + ":" + segundo, Fuente_Comprobante, Validar_codigo, nreserva)

# En este método se encuentra todo lo relacionado con el Bloque C piso 1, ya sea interfaz o disponibilidad


def Ventana_Disponibilidad_C():
    # Este for es el encargado de resetear la pantalla en la que el usuario
    # se encontraba anteriormente y poder mostrar la actual
    for ele in ventana.winfo_children():
        # Quiere decir que se destruye la imagen
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    # El lugar será en toda la interfaz
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Disponibles_C)
    # Posición en toda la pantalla
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra,
    # imagen del botón, color de fondo del botón, borde 1 para desaparecerlo
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    # Label en el que se mostrará un mensaje al usuario sobre las reservas
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el label,
    # color de fondo, fuente de la letra
    label4 = tk.Label(interfaz, text="¿Deseas reservar un computador?",
                      bg="#FFFFFF", font=Fuente_Disponibilidad_Preguntas)
    # Ubicación (x,y) del label
    label4.place(x=420, y=340)
    # Boton para ver el mapa de la u
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra, comando,
    # color de fondo del botón, borde 1 para desaparecerlo
    Boton_Mapa = tk.Button(ventana, text="Ver Ubicación\n en el mapa", width=7, height=10, font=Fuente_mapa, command=Ventana_Mapa,
                           bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Mapa.place(x=188, y=55, width=110, height=50)
    # Boton para realizar reserva
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra, comando,
    # color de fondo del botón, borde 1 para desaparecerlo
    Boton_Reserva = tk.Button(ventana, text="Hacer reserva", width=7, height=10, font=Fuente_principal, command=Reserva_Bloque_C_1,
                              bg="#FFFFFF", disabledforeground=None)
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Reserva.place(x=560, y=400, width=110, height=50)
    # Creamos un obejto de la clase de disponibilidad que muestra la disponibilidad de los computadores
    # en el lugar que el usuario escoja
    computadores = Disponibilidad()
    # Parámetros del método disponible: Ventana a mostrar, fuente de la letra, piso, lugar, fuente si no llega
    # a tener computadores disponibles
    computadores.disponible(Ventana_Disponibilidad_C,
                            Fuente_Disponibilidad, "1", "Bloque C", Fuente_No_Disponible)

# En este método se encuentra todo lo relacionado a las reservas realizadas en el
# Bloque K piso 4


def Reserva_Bloque_K_4():
    # Generamos un número random que sería el número de referencia del comprobante de reserva
    numero = random.randint(100000, 999999)
    # Como necesitamos guardar este número en un txt se debe convertir en string
    nreserva = str(numero)
    # Creamos un objeto de la clase Nreferencia que es la encargada de guardar este número en el txt
    numeroR = Nreferencia()
    # Los parámetros: Nombre de la variable que tiene el código a validar y el numero de reserva
    numeroR.Referencia(Validar_codigo, nreserva)
    # Cremoa un objeto de la clase Reserva, cuyos parámetros son el bloque y el piso
    reserva = Reserva("Bloque K", "4")
    # Método de la clase reserva cuyos parámetros son la ventana, tipo de fuente, nombre imagen del comprobante, nombre del lugar,
    # fecha, hora, tipo de fuente del comprobante, código del estudiante y el número de la reserva
    reserva.Res(Ventana_Disponibilidad_k, Fuente_Disponibilidad, Comprobante, "Bloque K, cuarto piso", now.date(
    ), hora + ":" + minuto + ":" + segundo, Fuente_Comprobante, Validar_codigo, nreserva)

# En este método se encuentra todo lo relacionado con el Bloque K piso 4, ya sea interfaz o disponibilidad


def Ventana_Disponibilidad_k():
    # Este for es el encargado de resetear la pantalla en la que el usuario
    # se encontraba anteriormente y poder mostrar la actual
    for ele in ventana.winfo_children():
        # Quiere decir que se destruye la imagen
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    # El lugar será en toda la interfaz
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Disponibles_K)
    # Posición en toda la pantalla
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra,
    # imagen del botón, color de fondo del botón, borde 1 para desaparecerlo
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    # Label en el que se mostrará un mensaje al usuario sobre las reservas
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el label,
    # color de fondo, fuente de la letra
    label4 = tk.Label(interfaz, text="¿Deseas reservar un computador?",
                      bg="#FFFFFF", font=Fuente_Disponibilidad_Preguntas)
    # Ubicación (x,y) del label
    label4.place(x=420, y=340)
    # Boton para ver el mapa de la u
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra, comando,
    # color de fondo del botón, borde 1 para desaparecerlo
    Boton_Mapa = tk.Button(ventana, text="Ver Ubicación\n en el mapa", width=7, height=10, font=Fuente_mapa, command=Ventana_Mapa,
                           bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Mapa.place(x=188, y=55, width=110, height=50)
    # Boton para realizar reserva
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra, comando,
    # color de fondo del botón, borde 1 para desaparecerlo
    Boton_Reserva = tk.Button(ventana, text="Hacer reserva", width=7, height=10, font=Fuente_principal, command=Reserva_Bloque_K_4,
                              bg="#FFFFFF", disabledforeground=None)
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Reserva.place(x=560, y=400, width=110, height=50)
    # Creamos un obejto de la clase de disponibilidad que muestra la disponibilidad de los computadores
    # en el lugar que el usuario escoja
    computadores = Disponibilidad()
    # Parámetros del método disponible: Ventana a mostrar, fuente de la letra, piso, lugar, fuente si no llega
    # a tener computadores disponibles
    computadores.disponible(Ventana_Disponibilidad_k,
                            Fuente_Disponibilidad, "4", "Bloque K", Fuente_No_Disponible)

# En este método se encuentra todo lo relacionado a las reservas realizadas en el
# Bloque G piso 5


def Reserva_Bloque_G_5():
    # Generamos un número random que sería el número de referencia del comprobante de reserva
    numero = random.randint(100000, 999999)
    # Como necesitamos guardar este número en un txt se debe convertir en string
    nreserva = str(numero)
    # Creamos un objeto de la clase Nreferencia que es la encargada de guardar este número en el txt
    numeroR = Nreferencia()
    # Los parámetros: Nombre de la variable que tiene el código a validar y el numero de reserva
    numeroR.Referencia(Validar_codigo, nreserva)
    # Cremoa un objeto de la clase Reserva, cuyos parámetros son el bloque y el piso
    reserva = Reserva("Bloque G", "5")
    # Método de la clase reserva cuyos parámetros son la ventana, tipo de fuente, nombre imagen del comprobante, nombre del lugar,
    # fecha, hora, tipo de fuente del comprobante, código del estudiante y el número de la reserva
    reserva.Res(Ventana_Disponibilidad_G, Fuente_Disponibilidad, Comprobante, "Bloque G, quinto piso", now.date(
    ), hora + ":" + minuto + ":" + segundo, Fuente_Comprobante, Validar_codigo, nreserva)

# En este método se encuentra todo lo relacionado con el Bloque G piso 5, ya sea interfaz o disponibilidad


def Ventana_Disponibilidad_G():
    # Este for es el encargado de resetear la pantalla en la que el usuario
    # se encontraba anteriormente y poder mostrar la actual
    for ele in ventana.winfo_children():
        # Quiere decir que se destruye la imagen
        ele.destroy()
    # Se crea la nueva Interfaz
    interfazG = tk.Canvas(ventana)
    # El lugar será en toda la interfaz
    interfazG.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfazG, image=Disponibles_G)
    # Posición en toda la pantalla
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra,
    # imagen del botón, color de fondo del botón, borde 1 para desaparecerlo
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    # Label en el que se mostrará un mensaje al usuario sobre las reservas
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el label,
    # color de fondo, fuente de la letra
    label4 = tk.Label(interfazG, text="¿Deseas reservar un computador?",
                      bg="#FFFFFF", font=Fuente_Disponibilidad_Preguntas)
    # Ubicación (x,y) del label
    label4.place(x=420, y=340)
    # Boton para ver el mapa de la u
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra, comando,
    # color de fondo del botón, borde 1 para desaparecerlo
    Boton_Mapa = tk.Button(ventana, text="Ver Ubicación\n en el mapa", width=7, height=10, font=Fuente_mapa, command=Ventana_Mapa,
                           bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Mapa.place(x=188, y=55, width=110, height=50)
    # Boton para realizar reserva
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra, comando,
    # color de fondo del botón, borde 1 para desaparecerlo
    Boton_Reserva = tk.Button(ventana, text="Hacer reserva", width=7, height=10, font=Fuente_principal, command=Reserva_Bloque_G_5,
                              bg="#FFFFFF", disabledforeground=None)
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Reserva.place(x=560, y=400, width=110, height=50)
    # Creamos un obejto de la clase de disponibilidad que muestra la disponibilidad de los computadores
    # en el lugar que el usuario escoja
    computadores = Disponibilidad()
    # Parámetros del método disponible: Ventana a mostrar, fuente de la letra, piso, lugar, fuente si no llega
    # a tener computadores disponibles
    computadores.disponible(Ventana_Disponibilidad_G,
                            Fuente_Disponibilidad, "5", "Bloque G", Fuente_No_Disponible)

# En este método se encuentra todo lo relacionado a las reservas realizadas en el
# Bloque D piso 1


def Reserva_Bloque_D_1():
    # Generamos un número random que sería el número de referencia del comprobante de reserva
    numero = random.randint(100000, 999999)
    # Como necesitamos guardar este número en un txt se debe convertir en string
    nreserva = str(numero)
    # Creamos un objeto de la clase Nreferencia que es la encargada de guardar este número en el txt
    numeroR = Nreferencia()
    # Los parámetros: Nombre de la variable que tiene el código a validar y el numero de reserva
    numeroR.Referencia(Validar_codigo, nreserva)
    # Cremoa un objeto de la clase Reserva, cuyos parámetros son el bloque y el piso
    reserva = Reserva("Bloque D", "1")
    # Método de la clase reserva cuyos parámetros son la ventana, tipo de fuente, nombre imagen del comprobante, nombre del lugar,
    # fecha, hora, tipo de fuente del comprobante, código del estudiante y el número de la reserva
    reserva.Res(Ventana_Disponibilidad_D, Fuente_Disponibilidad, Comprobante, "Bloque D, primer piso", now.date(
    ), hora + ":" + minuto + ":" + segundo, Fuente_Comprobante, Validar_codigo,  nreserva)

# En este método se encuentra todo lo relacionado con el Bloque D piso 1, ya sea interfaz o disponibilidad


def Ventana_Disponibilidad_D():
    # Este for es el encargado de resetear la pantalla en la que el usuario
    # se encontraba anteriormente y poder mostrar la actual
    for ele in ventana.winfo_children():
        # Quiere decir que se destruye la imagen
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    # El lugar será en toda la interfaz
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Disponibles_D)
    # Posición en toda la pantalla
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra,
    # imagen del botón, color de fondo del botón, borde 1 para desaparecerlo
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    # Label en el que se mostrará un mensaje al usuario sobre las reservas
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el label,
    # color de fondo, fuente de la letra
    label4 = tk.Label(interfaz, text="¿Deseas reservar un computador?",
                      bg="#FFFFFF", font=Fuente_Disponibilidad_Preguntas)
    # Ubicación (x,y) del label
    label4.place(x=420, y=340)
    # Boton para ver el mapa de la u
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra, comando,
    # color de fondo del botón, borde 1 para desaparecerlo
    Boton_Mapa = tk.Button(ventana, text="Ver Ubicación\n en el mapa", width=7, height=10, font=Fuente_mapa, command=Ventana_Mapa,
                           bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Mapa.place(x=188, y=55, width=110, height=50)
    # Boton para realizar reserva
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra, comando,
    # color de fondo del botón, borde 1 para desaparecerlo
    Boton_Reserva = tk.Button(ventana, text="Hacer reserva", width=7, height=10, font=Fuente_principal, command=Reserva_Bloque_D_1,
                              bg="#FFFFFF", disabledforeground=None)
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Reserva.place(x=560, y=400, width=110, height=50)
    # Creamos un obejto de la clase de disponibilidad que muestra la disponibilidad de los computadores
    # en el lugar que el usuario escoja
    computadores = Disponibilidad()
    # Parámetros del método disponible: Ventana a mostrar, fuente de la letra, piso, lugar, fuente si no llega
    # a tener computadores disponibles
    computadores.disponible(Ventana_Disponibilidad_D,
                            Fuente_Disponibilidad, "1", "Bloque D", Fuente_No_Disponible)

# En este método se encuentra todo lo relacionado con la interfaz de los créditos


def Ventana_creditos():
    # Este for es el encargado de resetear la pantalla en la que el usuario
    # se encontraba anteriormente y poder mostrar la actual
    for ele in ventana.winfo_children():
        # Quiere decir que se destruye la imagen
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    # El lugar será en toda la interfaz
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=credits)
    # Posición en toda la ventana
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra,
    # imagen del botón, color de fondo del botón, borde 1 para desaparecerlo
    Boton_Regreso = tk.Button(ventana, text="", command=MainMenu, font=Fuente_principal,
                              image=Imagen_Regresar_Creditos, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Regreso.place(x=847, y=449, width=63, height=64)

# En esta ventaba se mostrará todas las opciones disponibles para que el usuario escoja


def Ventana_Opciones():
    # Este for es el encargado de resetear la pantalla en la que el usuario
    # se encontraba anteriormente y poder mostrar la actual
    for ele in ventana.winfo_children():
        # Quiere decir que se destruye la imagen
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz_opciones = tk.Canvas(ventana)
    # El lugar será en toda la interfaz
    interfaz_opciones.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz_opciones, image=opciones)
    # Posición en toda la ventana
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra,
    # imagen del botón, color de fondo del botón, borde 1 para desaparecerlo
    Boton_Regreso = tk.Button(ventana, text="", command=MainMenu, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Regreso.place(x=830, y=445, width=74, height=70)
    # Cada uno de estos botones son los que llevan al usuario a las diferentes interfaces
    # Y así poder ver su disponibilidad.
    # los parámetros son los mismos que los anteriores
    # .Place para todos quiere decir la ubicación (x,y) y ancho, alto
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

# En esta ventana se encuentra todo lo relacionado a la ventana de explicación
# es decir, donde se le explicará al usuario como usar la aplicación.


def Ventana_Explicacion():
    # Este for es el encargado de resetear la pantalla en la que el usuario
    # se encontraba anteriormente y poder mostrar la actual
    for ele in ventana.winfo_children():
        # Quiere decir que se destruye la imagen
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz_Explicacion = tk.Canvas(ventana)
    # El lugar será en toda la interfaz
    interfaz_Explicacion.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz_Explicacion, image=Explicacion)
    # Posición en toda la ventana
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra,
    # imagen del botón, color de fondo del botón, borde 1 para desaparecerlo
    Boton_Regreso = tk.Button(ventana, text="", command=MainMenu, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Regreso.place(x=3, y=450, width=74, height=70)

# En este método se encuentra las opciones de piso del bloque B, para que
# el usuario escoja lo que desee


def Ventana_Pisos_BloqueB():
    # Este for es el encargado de resetear la pantalla en la que el usuario
    # se encontraba anteriormente y poder mostrar la actual
    for ele in ventana.winfo_children():
        # Quiere decir que se destruye la imagen
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    # El lugar será en toda la interfaz
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Fondo_Pisos)
    # Posición en toda la ventana
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra,
    # imagen del botón, color de fondo del botón, borde 1 para desaparecerlo
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    # Este botón te dirige a la ventana piso 1 bloque B
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra,
    # imagen del botón, color de fondo del botón, borde 1 para desaparecerlo
    Boton_Piso1 = tk.Button(ventana, text="", font=Fuente_principal, command=Ventana_Disponibilidad_B_1,
                            image=Piso1, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    #Ubicación (x,y), ancho, alto
    Boton_Piso1.place(x=150, y=355, width=200, height=49)
    # Este botón te dirige a la ventana piso 2 bloque B
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra,
    # imagen del botón, color de fondo del botón, borde 1 para desaparecerlo
    Boton_Piso2 = tk.Button(ventana, text="", font=Fuente_principal, command=Ventana_Disponibilidad_B_2,
                            image=Piso2, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    #Ubicación (x,y), ancho, alto
    Boton_Piso2.place(x=480, y=355, width=200, height=49)

#En este método se encuentra las opciones de pisos de Casa Estudio, para que
#el usuario escoja lo que desee

def Ventana_Pisos_CasaE():
    # Este for es el encargado de resetear la pantalla en la que el usuario
    # se encontraba anteriormente y poder mostrar la actual
    for ele in ventana.winfo_children():
        # Quiere decir que se destruye la imagen
        ele.destroy()
    # Se crea la nueva Interfaz
    interfaz = tk.Canvas(ventana)
    # El lugar será en toda la interfaz
    interfaz.pack()
    # En el label se carga la imagen
    label1 = tk.Label(interfaz, image=Fondo_Pisos)
    #Posición en toda la ventana
    label1.pack()
    # Boton para regresarte al menú principal y para quitarle los bordes
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra,
    # imagen del botón, color de fondo del botón, borde 1 para desaparecerlo
    Boton_Regreso = tk.Button(ventana, text="", command=Ventana_Opciones, width=7, height=1, font=Fuente_principal,
                              image=Imagen_Regresar, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    # Ubicación (x,y) del botón y ancho, alto                 
    Boton_Regreso.place(x=830, y=430, width=74, height=70)
    # Este botón te dirige a la ventana piso 1 de Casa Estudio
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra,
    # imagen del botón, color de fondo del botón, borde 1 para desaparecerlo
    Boton_Piso1 = tk.Button(ventana, text="",  width=7, height=1, font=Fuente_principal, command=Ventana_Disponibilidad_CasaE_1,
                            image=Piso1, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    #Ubicación (x,y), ancho, alto
    Boton_Piso1.place(x=98, y=345, width=200, height=49)
    # Este botón te dirige a la ventana piso 2 de Casa Estudio
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra,
    # imagen del botón, color de fondo del botón, borde 1 para desaparecerlo
    Boton_Piso2 = tk.Button(ventana, text="",  width=7, height=1, font=Fuente_principal, command=Ventana_Disponibilidad_CasaE_2,
                            image=Piso2, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    #Ubicación (x,y), ancho, alto
    Boton_Piso2.place(x=328, y=345, width=200, height=49)
    # Este botón te dirige a la ventana piso 3 de Casa Estudio
    # EL orden de los parámetros es: Ventana a mostrar, texto que va en el botón, comando, fuente de la letra,
    # imagen del botón, color de fondo del botón, borde 1 para desaparecerlo
    Boton_Piso3 = tk.Button(ventana, text="",  width=7, height=1, font=Fuente_principal, command=Ventana_Disponibilidad_CasaE_3,
                            image=Piso3, bg="#FFFFFF", bd=1, disabledforeground=None,  relief="flat")
    #Ubicación (x,y), ancho, alto
    Boton_Piso3.place(x=558, y=345, width=200, height=49)


def Ventana_Mapa():
    mapa = tk.Toplevel()
    mapa.geometry("346x512+500+130")
    mapa.title("Mapa")
    mapa.resizable(width=0, height=0)
    label8 = tk.Label(mapa, image=map)
    label8.pack()
    mapa.mainloop()


MainMenu()
# El mainloop lleva el registro de todo lo que está sucediendo en la ventana:
ventana.mainloop()
