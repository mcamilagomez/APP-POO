lugar_seleccionado = "Casa Estudio"
piso_seleccionado = "1"
sw = int
sw = 1
fila = []
with open ("file/dispo.txt") as file:
    readfile = file.readlines()
    
for string in readfile:
    fila = string.split(",")
    lugar = fila[0]
    piso = fila[1]
    disponibilidad = fila[2]
    cantidad = fila[3]
    print(lugar+piso+disponibilidad+cantidad)
	    






