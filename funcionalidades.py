#Importamos el GUI de python para acceder a sus métodos
from tkinter import *
import tkinter as tk
from re import A

#Con esta clase se valida el código del estudiante
class Estudiantes():
    #En el constructor inicializamos los atributos, en este caso solo text 
    #text es lo que el usuario ingresa
    def __init__(self, text):
        self.text = text
    #este es el método que válida que lo ingresado sean números
    def validate_code(text: str):
        return text.isdecimal()

#Gracias a esta clase el usuario podrá ver la disponibilidad de los computadores en la interfaz
class Disponibilidad(Frame):
    #En el constructor abrimos el archivo txt donde se encuentran la disponibilidad de los computadores
    def __init__(self):
        file = open("file\dispo.txt", "r+")  #r se significa que se abre en modo lectura
        self.readfile = file.readlines() #readlines quiere decir que va a leer todo lo que se encuentra dentro del txt
        
    #Este método muestra en pantalla la disponibilidad de los computadores.
    #Parámetros: Ventana a mostrar, tipo de fuente de la letra de disponibilidad, piso, nombre del bloque y tipo de fuente 
    #para cuando no hayan computadores disponibles.
    def disponible(self, ventana, fuente, pisoBloque, Bloque, fuente2):
        #Con este for leemos y separamos las líneas para así poder buscar la que necesitamos
        for string in self.readfile:
            #Aquí separamos los string entre comas (,)
            fila = string.split(",")
            #la primera palabra de la fila será el lugar
            lugar = fila[0]
            #la segunda palabra de la fila será el piso
            piso = fila[1]
            #la tercera palabra de la fila será la disponibilidad (Falso o verdadero)
            disponibilidad = fila[2]
            #la cuarta palabra de la fila será la cantidad de computadores
            cantidad = fila[3]
            #Estos son los parámetros, dependiendo de esto se busca en el txt
            self.pisoBloque = pisoBloque #piso
            self.Bloque = Bloque    #bloque
            #Aquí comparamos cada fila con el parámetro, para ubicarnos en el que necesitamos
            if (lugar == Bloque and piso == pisoBloque):
                #Si en esa fila hay disponibilidad
                if (disponibilidad == "true"):
                    #Entonces en la ventana que deseamos (parámetro) se mostrará un label con el número
                    ventana
                    #Este es el label del número
                    #Parámetros: texto label, fondo, tipo de fuente
                    label3 = tk.Label(text=cantidad, bg="#FFFEFF",
                                      font=fuente)
                    #Ubicacion x,y y ancho, alto
                    label3.place(x=254, y=340, width=50, height=75)
                else: #si esto no ocurre, es decir, es false, se mostrará un label encima del botón de reserva, como para "quitarlo"
                    ventana
                    #Parámetros: texto, color fondo, fuente
                    quitarBoton = tk.Label(text="Lo sentimos, no hay computadores\n disponibles el día de hoy", bg="#FFFEFF",
                                           font=fuente2)
                    #Ubicacion x,y y ancho, alto
                    quitarBoton.place(x=450, y=400, width=300, height=50)
                    #En la parte de disponibilidad se mostrará un 0 representando que no hay computadores disponibles
                    label3 = tk.Label(text=cantidad, bg="#FFFFFF",
                                      font=fuente)

#Esta clase es la encargada de realizar las reservas y mostrar el comprobante
class Reserva(Frame):
    #En el constructor inicializamos los atributos
    def __init__(self, lugar, piso): 
        self.lugar_seleccionado = lugar #lugar
        self.piso_seleccionado = piso  #piso
        a = open("file/dispo.txt")  #Abrimos el txt de disponibilidades
        self.readfile = a.readlines()  #Para leer todo
        self.newfile = ""  #Agregaremos o quitaremos filas en el archivo

    #este método es el encargado de mostrar el comprobante por pantalla
    #Parámetros: Imagen comprobante, lugar, fecha actual, hora actual, fuente de la letra, código del 
    #estudiante y número de la reserva
    def Comp(self, imagen, lugar, fecha, hora, fuente, codigo, n): 
        #Ventana c es la nueva interfaz que se va a mostrar
        ventanaC = tk.Toplevel()
        ventanaC.geometry("346x512+500+130") #Tamaño de la ventana y posición en la ventana
        ventanaC.title("Comprobante de reserva")  #titulo de la ventana
        ventanaC.resizable(width=0, height=0)  #Para que no se pueda ampliar
        label8 = tk.Label(ventanaC, image=imagen) #fondo, es decir, imagen
        label8.pack() #tamaño en toda la ventana
        label12 = tk.Label(ventanaC, text=codigo, font=fuente, bg="#FFFFFF") #Label que muestra el código del estudiante
        label12.place(x=22, y=240) #Ubicación x, y
        label9 = tk.Label(ventanaC, text=lugar, font=fuente, bg="#FFFFFF") #Label que muestra el lugar del estudiante
        label9.place(x=22, y=289)  #Ubicación x, y
        label10 = tk.Label(ventanaC, text=fecha, font=fuente, bg="#FFFFFF") #Label que muestra la fehca del estudiante
        label10.place(x=22, y=338) #Ubicación x, y
        label11 = tk.Label(ventanaC, text=hora, font=fuente, bg="#FFFFFF") #Label que muestra la hora del estudiante
        label11.place(x=22, y=387) #Ubicación x, y
        label13 = tk.Label(ventanaC, text=n, font=fuente, bg="#FFFFFF") #Label que muestra el numero de reserva del estudiante
        label13.place(x=150, y=171) #Ubicación x, y
        ventanaC.mainloop() #Lleva registro de todo lo que sucede en la ventana

    #este método es el encargado de cambiar la disponibilidad en el txt de disponibilidad
    def Res(self, ventana, fuente1, imagen, lugar, fecha, hora, fuente, codigo, num):
        #Con este for leemos y separamos las líneas para así poder buscar la que necesitamos
        for string in self.readfile:
            #Aquí separamos los string entre comas (,)
            fila = string.strip().split(",")
            #la primera palabra de la fila será el lugar
            lugar = fila[0]
            #la segunda palabra de la fila será el piso
            piso = fila[1]
            #la tercera palabra de la fila será la disponibilidad (Falso o verdadero)
            disponibilidad = fila[2]
            #la cuarta palabra de la fila será la cantidad de computadores
            cantidad = int(fila[3])
            #si el luagar de la fila es igual al seleccionado y el piso es igual al seleccionado y si hay disponibilidad de computadores (mayor a 0)
            if (lugar == self.lugar_seleccionado) and (piso == self.piso_seleccionado) and (disponibilidad == "true") and (cantidad > 0) :
                #La nueva cantidad se le restará 1
                nuevacantidad = cantidad - 1
                #Se reescribe la linea con la nueva disponibilidad
                self.newfile += f"{lugar},{piso},{disponibilidad},{nuevacantidad}\n"
                #Se muestra el nuevo número de disponibilidad con los mismos parámetros que el anterior
                label3 = tk.Label(text=nuevacantidad, bg="#FFFFFF",
                                  font=fuente1)
                #ubicacion x, y y ancho, alto
                label3.place(x=254, y=320, width=50, height=75)
                #creamo un objeto de la clase reserva
                comprobante = Reserva(lugar, piso) #agregamos los parámetros necesarios
                #y con el método comp se crea la imagen del comprobante
                comprobante.Comp(imagen, lugar, fecha, hora, fuente, codigo, num)
            else: #si no se encuentra o no hay disponibilidad entonces que quede lo mismo que antes
                self.newfile += f"{lugar},{piso},{disponibilidad},{cantidad}\n"
        a = open("file/dispo.txt", "w") #para poder rescribir la linea se debe abrir el archivo txt en forma de escritura 
        a.write(self.newfile) #se escribe la nueva fila
        a.close()  #se cierra el archivo

#Esta clase ingresa el codigo y el número de reserva en un txt para que el encargado pueda verificar que tenga una reserva el estudiante
class Nreferencia():
    def __init__(self):
        self.archivo = open("file/reser.txt", "a") #Abrimos el archivo para agregar filas

    def Referencia(self, codigo, num): #En este metodo ingresamos el codigo y el número de reserva
        self.archivo.write(num + "," + codigo + "\n")  #Se escribe una línea con el número de reserva y el código
        self.archivo.close()  #Se cierra el archivo