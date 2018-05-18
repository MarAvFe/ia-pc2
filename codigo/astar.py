import random
def encontrarZanahorias(tablero):
	posicionZanahorias=[]
	for y in range(len(tablero)):
		for x in range(len(tablero[y])):
			if (tablero[y][x] == "Z"):
				posicionZanahoriasappend([x, y])	
	return posicionZanahorias

def encontrarConejo(tablero):
	for y in range(len(tablero)):
		for x in range(len(tablero[y])):
			if tablero[y][x] == "C":
				return (x,y)
	return (-1,-1)

def guardarArchivo(tablero, nombre):
	with open(nombre+".txt", 'w') as archivo:
		for y in range(len(tablero)):
			lTmp=""
			for x in range(len(tablero[y])):
				if tablero[y][x] == "":
					lTmp+="·"
				else:
					lTmp+=str(tablero[y][x])
			lTmp+="\n"
			archivo.write(lTmp)

def movimiento(posicionConejo, movimientoGanador, tablero):
	f, c = posicionConejo
	tablero[f][c] = ""
	comioZanahoria = False
	if movimientoGanador == "IZQUIERDA":
		c-=1
	elif movimientoGanador == "DERECHA":
		c+=1
	elif movimientoGanador == "ARRIBA":
		f-=1
	elif movimientoGanador == "ABAJO":
		f+=1
	if (tablero[f][c]=="Z"):
		comioZanahoria = True
	tablero[f][c] = "C"
	return (f,c), comioZanahoria, posicionConejo


def calcularMejorMovimiento(posicionConejo, tableroVisible, posicionAnterior, tablero):
	f,c = posicionConejo
	f_p, c_p = posicionAnterior
	movimientos = ["IZQUIERDA", "DERECHA", "ARRIBA", "ABAJO"]
	costoMovimiento=[]
	coordenadas =[(0,-1),(0,1),(-1,0),(1,0)]
	# Revisa si hay zanahorias
	if (cantidadZanahoriasTablero(tableroVisible)==0):
		# Mover aleatoriamente al conejo, pero que no vuelva a la posicion anterior
		f_r, c_r = random.choice(coordenadas)
		while (f_r== f_p and c_r ==c_p):
			f_r, c_r = random.choice(coordenadas)
#imprimir los costos para cada movimiento
	else:
		# Calcular costos de cada movimiento
		mejorMovimiento, costoMovimiento, movimientos = calcularCostoTotal(posicionConejo, tableroVisible)

		# Mover conejo
		
		posicionConejo, comioZanahoria, posicionAnterior = movimiento(posicionConejo, movimientoGanador, tablero)
	return mejorMovimiento


def calcularCostoTotal(posicionConejo, tableroVisible):
# Falta poner la restricción que se muevasolo si existe el casillero en la tabla
	f,c = posicionConejo
	movimientos = ["IZQUIERDA", "DERECHA", "ARRIBA", "ABAJO"]
	costoMovimiento=[]
	coordenadas =[(0,-1),(0,1),(-1,0),(1,0)]
	f,c = posicionConejo
	for i in range(len(coordenadas)):
		c_f,c_c = i
		f+=c_f
		c+=c_c
		costoMovimiento.append(calcularHeuristico((f,c) + calcularCosto((f,c))))
	valorMayor=0
	indice=0
# FALTA que si es un empate de costos menores, seleccionar el movimiento aleatoriamenet
	for i in range(len(costoMovimiento)):
		if (valorMayor < i):
			valorMayor = costoMovimiento[i]
			indice = i
	# Imprimir costo de cada coordenada
	# 

	return movimientos[indice], costoMovimiento, movimientos



def calcularHeuristico():
	pass

def encontrarZanahoria():
	pass
def calcularCosto():
	# Espacio vacío = 0
	# Zanahoria = 1
	pass

def moverConejo(tablero, posicionConejo, nuevaPosicion):
	f_c, c_c = posicionConejo
	f_n, c_n = nuevaPosicion
	tablero [x_c][y_c]=""
	tablero [x_n][y_n]="C"
	return tablero

def getTableroVisible(tablero, rangoVision, posicionConejo):
	tableroVisible = []
	f_c, c_c = posicionConejo
	c_min = c_c - rangoVision
	f_min = f_c - rangoVision
	c_max = c_c + rangoVision
	f_max = f_c + rangoVision
	largo = len(tablero) - 1
	if f_min < 0:
		f_min = 0
	if c_min < 0:
		c_min = 0
	if c_max > largo:
		c_max = largo
	if f_max > largo:
		f_max = largo
	for f in range(f_min,f_max+1):
		lTemp=[]
		for c in range(c_min,c_max+1):
			lTemp.append (tablero [f][c])
		tableroVisible.append(lTemp)
	return tableroVisible

def imprimirTablero(tablero):
	for f in range(len(tablero)):
		tmp=""
		for c in range(len(tablero[f])):
			if (tablero[f][c]==""):
				tmp+="·"
			else:
				tmp+=tablero[f][c]
		print(tmp)


def cantidadZanahoriasTablero(tablero):
	totalZanahorias = 0
	for f in range(len(tablero)):
		for c in range(len(tablero[f])):
			if tablero[f][c] == "Z":
				totalZanahorias+=1	
	return totalZanahorias

def main(rangoVision = 1, zanahoriasPorComer = 3):
	tablero = [
		['','','','','','',''],
		['','Z','','C','','','Z'],
		['','','','Z','','',''],
		['','','','','','',''],
		['','','','','','',''],
		['','Z','','','Z','',''],
		['','','','','','',''],
		['','','','','','','Z']
	]	
	zanahoriasComidas = 0
	costoAcumulado = 0
	#costoRegular = 1.0
	paso = 0
	print("--- Tablero inicial ---")
	imprimirTablero(tablero)
	print("\n\n")
	posicionConejo = encontrarConejo(tablero)
	cantidadInicialZanahorias = cantidadZanahoriasTablero (tablero)
	posicionAnteriorConejo = posicionConejo # Inicial, en este caso
	zanahoraisComidas = 0

	# Revisa si es que las condiciones son válidas, si se puede iniciar.
	if ((cantidadInicialZanahorias < zanahoriasPorComer) or (posicionConejo[0]==-1 and posicionConejo[1]==-1)):
		print ("Error al ingresar los parámetros")
	else:
		guardarArchivo(tablero, str(paso).zfill(5))
		while(zanahoriasPorComer != zanahoraisComidas):
			paso+=1
			# Busca los espacios visibles
			tableroVisible = getTableroVisible(tablero, rangoVision, posicionConejo)
			print("--- Tablero visible ---")
			imprimirTablero(tableroVisible)
			print("\n\n")
			#coordenadasZanahorias = encontrarZanahorias(tableroVisible)

			# Calcular el costo de cada movimiento
			calcularMejorMovimiento(posicionConejo, tableroVisible, posicionAnterior, tablero)
			# Imprime resultado
			print("PASO: "+ str(paso).zfill(5) + " IZQUIERDA: "+ " DERECHA: " + " ARRIBA: " + " ABAJO: "+" MOVIMIENTO: ")
			#PASO: 00001 IZQUIERDA: 5 DERECHA: 3 ARRIBA: 8 ABAJO: 9 MOVIMIENTO: DERECHA



		print("PASO: "+ getNumeroPaso+ " FINAL")


main(2, 2)
