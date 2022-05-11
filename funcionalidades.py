
from tkinter import *
import tkinter as tk

class Estudiantes():
        def __init__(self, text):
            self.text = text

        def validate_code(text: str):
            return text.isdecimal()

class Disponibilidad(Frame):

    def __init__(self):
        file = open("file\dispo.txt")
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
                if (disponibilidad == "true"):  # aqui se coloca lo del boton
                    # print(cantidad)
                    # 1. Estabas tratando de abrir una ventan en un label, so k mor?
                    # 2. Para la ubicación es .place
                    # Solución, primero abro la ventana y luego mando el label
                    # Segundo pues pongo el place JAJAJJAJA, Mira lo que me mostraste
                    ventana
                    label3 = tk.Label(text=cantidad, bg="#FFFFFF",
                                      font=fuente)
                    label3.place(x=254, y=340, width=50, height=75)
            else:
                if (lugar!="Bloque G" and piso!=pisoBloque):
                    ventana
                    label4 = tk.Label(text="0", bg="#FFFFFF",
                                      font=fuente)
                    label4.place(x=254, y=340, width=50, height=75)

    
