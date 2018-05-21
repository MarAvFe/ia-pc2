import random
import shutil
import os

class Estado(object):
	g = 0
	h = 0
	f = 0

	def __init__(self, g, h, f):
		self.g = g
		self.h = h
		self.f = f

def getEstado(g, h, f):
	estado = Estado(g, h, f)
	return estado

# Busca y encuentra las coordenadas de todas las zanahorias en el tablero visible
def encontrarZanahorias(tablero):
	posicionZanahorias=[]
	for y in range(len(tablero)):
		for x in range(len(tablero[y])):
			if (tablero[y][x] == "Z"):
				posicionZanahoriasappend([x, y])	
	return posicionZanahorias

# Encuentra las coordenadas del conejo
def encontrarConejo(tablero):
	for y in range(len(tablero)):
		for x in range(len(tablero[y])):
			if tablero[y][x] == "C":
				return (x,y)
	return (-1,-1)

# Leer tablero inicial
def leerTableroInicial(nombreArchivo):
	tablero = []
	with open(nombreArchivo) as archivo:
		for fila in archivo.readlines():
			tmp = []
			for columna in fila[:-1]:
				if (columna!=","):
					if (columna == "Z" or columna =="C" or columna ==" " ):
						tmp.append(columna)
					else:
						break
			tablero.append(tmp)
	return tablero


# Guarda en un archivo de texto el tablero después de dar un paso
def guardarArchivoOriginalBORRAR(tablero, nombre):
	if not os.path.exists("resultados"):
		os.makedirs("resultados")
	with open("resultados/"+nombre+".txt", 'w') as archivo:
		for y in range(len(tablero)):
			lTmp=""
			for x in range(len(tablero[y])):
				if tablero[y][x] == "":
					lTmp+="·"
				else:
					lTmp+=str(tablero[y][x])
			lTmp+="\n"
			archivo.write(lTmp)

# Guarda en un archivo de texto el tablero después de dar un paso
def guardarArchivo(tablero, nombre):
	if not os.path.exists("resultados"):
		os.makedirs("resultados")
	with open("resultados/"+nombre+".txt", 'w') as archivo:
		for y in range(len(tablero)):
			lTmp=""
			for x in range(len(tablero[y])):
				if tablero[y][x] == " ":
					lTmp+=" "
				else:
					lTmp+=str(tablero[y][x])
				lTmp+=","
			lTmp=lTmp[:-1]
			lTmp+="\n"
			archivo.write(lTmp)

# Mueve al conejo al conejo en el tablero según el resultado ganador
def movimiento(posicionConejo, movimientoGanador, tablero):
	f, c = posicionConejo
	tablero[f][c] = "" # Elimina al conejo de la posición en la que se encontraba
	comioZanahoria = False
	if movimientoGanador == "IZQUIERDA":
		c-=1
	elif movimientoGanador == "DERECHA":
		c+=1
	elif movimientoGanador == "ARRIBA":
		f-=1
	elif movimientoGanador == "ABAJO":
		f+=1
	# Revisa si comió una zanahoria
	if (tablero[f][c]=="Z"):
		comioZanahoria = True
	# Coloca al conejo en la posición nueva.
	tablero[f][c] = "C"
	# Devuelve: nueva coordenada del conejo, si comió una zanahoria, 
	return (f,c), comioZanahoria, posicionConejo

#def moverConejo(tablero, posicionConejo, nuevaPosicion):
#	f_c, c_c = posicionConejo
#	f_n, c_n = nuevaPosicion
#	tablero [x_c][y_c]=""
#	tablero [x_n][y_n]="C"
#	return tablero

# Según el g y el h, devuelve el mejor movimiento.
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


def imprimirCostosDeCadaMovimiento(paso, costoPorMovimiento, movimientoGanador):
	print("PASO: "+ str(paso).zfill(5) + " IZQUIERDA: "+ costoPorMovimiento[0] +
										" DERECHA: " + costoPorMovimiento[1] +
										" ARRIBA: " + costoPorMovimiento[2] +
										" ABAJO: "+ costoPorMovimiento[3]  + 
										" MOVIMIENTO: "+ movimientoGanador)
	#PASO: 00001 IZQUIERDA: 5 DERECHA: 3 ARRIBA: 8 ABAJO: 9 MOVIMIENTO: DERECHA



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

def imprimirTableroOriginal(tablero):
	for f in range(len(tablero)):
		tmp=""
		for c in range(len(tablero[f])):
			if (tablero[f][c]==""):
				tmp+="·"
			else:
				tmp+=tablero[f][c]
		print(tmp)

def imprimirTablero(tablero):
	for f in range(len(tablero)):
		tmp=""
		for c in range(len(tablero[f])):
			if (tablero[f][c]==" "):
				tmp+="·"
			else:
				tmp+=tablero[f][c]
		print(tmp)

def borrarResultadosPrevios():
	shutil.rmtree("resultados", ignore_errors=True)

def cantidadZanahoriasTablero(tablero):
	totalZanahorias = 0
	for f in range(len(tablero)):
		for c in range(len(tablero[f])):
			if tablero[f][c] == "Z":
				totalZanahorias+=1	
	return totalZanahorias

def getVecinos(posicionConejo, tablero):
	listaVecinos = []
	costoMovimiento=[]
	coordenadas =[(0,-1),(0,1),(-1,0),(1,0)]
	numeroFilas = len(tablero)-1
	numeroColumnas = len(tablero[0])-1
	x, y = posicionConejo
	for i in coordenadas:
		_x = x + i[0]
		_y = y + i[1]
		if (_x>=0 and _y >= 0 and _x <= numeroFilas and _y <= numeroColumnas):
			listaVecinos.append[_x, _y]
	return listaVecinos

def main(rangoVision = 1, zanahoriasPorComer = 3):
	abierta = []
	cerrada = []
	g, h = 0
	zanahoriasComidas = 0
	costoAcumulado = 0
	#costoRegular = 1.0
	borrarResultadosPrevios() # Borra carpeta que contiene resultados de la corrida anterior
	paso = 0
	print("********** Tablero inicial **********")
	tablero = leerTableroInicial("tableroInicial.txt")	
	imprimirTablero(tablero)
	cerrada.append(posicionConejo = encontrarConejo(tablero))
	cantidadInicialZanahorias = cantidadZanahoriasTablero (tablero)
	posicionAnteriorConejo = posicionConejo # Inicial, en este caso
	zanahoraisComidas = 0
	# Revisa si es que las condiciones son válidas, si se puede iniciar.
	if ((cantidadInicialZanahorias < zanahoriasPorComer) or (posicionConejo[0]==-1 and posicionConejo[1]==-1)):
		print ("Error al ingresar los parámetros")
	else:
		#guardarArchivo(tablero, str(paso).zfill(5))
		abierta = getVecinos(posicionConejo, tableroVisible)
		while(zanahoriasPorComer != zanahoraisComidas):
			paso+=1
			# Busca los espacios visibles
			tableroVisible = getTableroVisible(tablero, rangoVision, posicionConejo)
			print("-------------------- Tablero visible --------------------")
			imprimirTablero(tableroVisible)
			print("\n\n")
			#coordenadasZanahorias = encontrarZanahorias(tableroVisible)

			# Calcular el costo de cada movimiento
			calcularMejorMovimiento(posicionConejo, tableroVisible, posicionAnterior, tablero)
			# Imprime resultado
			imprimirCostosDeCadaMovimiento(paso , "FALTA", "FALTA")
			


		print("PASO: "+ getNumeroPaso+ " FINAL")


main(2, 2)
