def leerTablero(ruta):
    with open(ruta, "r") as f:
        tablero = []
        for line in f:
            linea = []
            for campo in line.split(","):
                linea.append(campo.split("\n")[0] if campo != "\n" else " ")
            tablero.append(linea)
        return tablero
