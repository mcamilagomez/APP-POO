lugar_seleccionado = "Biblioteca"
piso_seleccionado = "1"
fila = []

with open ("file/dispo.txt") as file:
    readfile = file.readlines()
     
for string in readfile:
    fila = string.split(",")
    lugar = fila[0]
    piso = fila[1]
    disponibilidad = fila[2]
    cantidad = fila[3]
    if ((lugar == lugar_seleccionado)and(piso == piso_seleccionado)):
        if (disponibilidad=="true"):
            print(cantidad)
    


        