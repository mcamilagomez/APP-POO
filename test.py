
lugar_seleccionado = "Biblioteca"
piso_seleccionado = "1"
fila = []
a=open("file/dispo.txt")
print(a.readlines)
readfile = a.readlines()
newfile = ""

for string in readfile:
    fila = string.strip().split(",")
    lugar = fila[0]
    piso = fila[1]
    disponibilidad = fila[2]
    cantidad = int(fila[3])
    if (lugar == lugar_seleccionado)and(piso == piso_seleccionado)and(disponibilidad=="true"):
        nuevacantidad = cantidad - 1
        newfile += f"{lugar},{piso},{disponibilidad},{nuevacantidad}\n"
    else:
        newfile += f"{lugar},{piso},{disponibilidad},{cantidad}\n"
        
a.close()

a=open("file/dispo.txt", "w")
a.write(newfile)
a.close()