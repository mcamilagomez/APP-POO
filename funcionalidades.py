from tkinter import *
import tkinter as tk

class Estudiantes():
    
        def __init__(self, text):
            self.text = text

        def validate_code(text: str):
            return text.isdecimal()

class Disponibilidad(Frame):

    def __init__(self):
        file = open("file\dispo.txt", "r+")
        self.readfile = file.readlines()

    def disponible(self, ventana, fuente, pisoBloque, Bloque):
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
                    label3 = tk.Label(text=cantidad, bg="#FFFFFF",
                                      font=fuente)
                    label3.place(x=254, y=340, width=50, height=75)
    
    def Reserva(self, ventana, fuente, pisoBloque, Bloque):        
        for string in self.readfile:
            fila = string.split(",")
            lugar = fila[0]
            piso = fila[1]
            disponibilidad = fila[2]
            cantidad = int(fila[3])
            self.pisoBloque = pisoBloque
            self.Bloque = Bloque
            if (lugar == Bloque and piso == pisoBloque):
                if (disponibilidad == "true"):
                    nuevacantidad = cantidad-1
                