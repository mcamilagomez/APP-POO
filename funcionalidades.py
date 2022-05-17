from tkinter import *
import tkinter as tk
from re import A


class Estudiantes():

    def __init__(self, text):
        self.text = text

    def validate_code(text: str):
        return text.isdecimal()


class Disponibilidad(Frame):

    def __init__(self):
        file = open("file\dispo.txt", "r+")
        self.readfile = file.readlines()

    def disponible(self, ventana, fuente, pisoBloque, Bloque, fuente2):
        for string in self.readfile:
            fila = string.split(",")
            lugar = fila[0]
            piso = fila[1]
            disponibilidad = fila[2]
            cantidad = fila[3]
            self.pisoBloque = pisoBloque
            self.Bloque = Bloque
            if (lugar == Bloque and piso == pisoBloque):
                if (disponibilidad == "true"):
                    ventana
                    label3 = tk.Label(text=cantidad, bg="#FFFEFF",
                                      font=fuente)
                    label3.place(x=254, y=340, width=50, height=75)
                else:
                    ventana
                    quitarBoton = tk.Label(text="Lo sentimos, no hay computadores\n disponibles el día de hoy", bg="#FFFEFF",
                                           font=fuente2)
                    quitarBoton.place(x=450, y=400, width=300, height=50)
                    label3 = tk.Label(text=cantidad, bg="#FFFFFF",
                                      font=fuente)
                    label3.place(x=254, y=340, width=50, height=75)


class Reserva(Frame):
    def __init__(self, lugar, piso):
        self.lugar_seleccionado = lugar
        self.piso_seleccionado = piso
        self.fila = []
        a = open("file/dispo.txt")
        self.readfile = a.readlines()
        self.newfile = ""

    def Comp(self, imagen, lugar, fecha, hora, fuente, codigo, n):
        global ventanaC
        ventanaC = tk.Toplevel()
        ventanaC.geometry("346x512+500+130")
        ventanaC.title("Comprobante de reserva")
        ventanaC.resizable(width=0, height=0)
        label8 = tk.Label(ventanaC, image=imagen)
        label8.pack()
        label12 = tk.Label(ventanaC, text=codigo, font=fuente, bg="#FFFFFF")
        label12.place(x=22, y=240)
        label9 = tk.Label(ventanaC, text=lugar, font=fuente, bg="#FFFFFF")
        label9.place(x=22, y=289)
        label10 = tk.Label(ventanaC, text=fecha, font=fuente, bg="#FFFFFF")
        label10.place(x=22, y=338)
        label11 = tk.Label(ventanaC, text=hora, font=fuente, bg="#FFFFFF")
        label11.place(x=22, y=387)
        label13 = tk.Label(ventanaC, text=n, font=fuente, bg="#FFFFFF")
        label13.place(x=150, y=171)
        ventanaC.mainloop()

    def Res(self, ventana, fuente1, imagen, lugar, fecha, hora, fuente, codigo, num):
        for string in self.readfile:
            fila = string.strip().split(",")
            lugar = fila[0]
            piso = fila[1]
            disponibilidad = fila[2]
            cantidad = int(fila[3])
            if (lugar == self.lugar_seleccionado) and (piso == self.piso_seleccionado) and (disponibilidad == "true") and (cantidad > 0) :
                nuevacantidad = cantidad - 1
                self.newfile += f"{lugar},{piso},{disponibilidad},{nuevacantidad}\n"
                ventana
                label3 = tk.Label(text=nuevacantidad, bg="#FFFFFF",
                                  font=fuente1)
                label3.place(x=254, y=320, width=50, height=75)
                comprobante = Reserva(lugar, piso)
                comprobante.Comp(imagen, lugar, fecha, hora, fuente, codigo, num)
            else:
                self.newfile += f"{lugar},{piso},{disponibilidad},{cantidad}\n"
        a = open("file/dispo.txt", "w")
        a.write(self.newfile)
        a.close()


class Nreferencia():
    def __init__(self):
        self.archivo = open("file/reser.txt", "a")

    def Referencia(self, codigo, num):
        self.archivo.write(num + "," + codigo + "\n")
        self.archivo.close()
