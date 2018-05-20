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

def getMejorMovimiento(listaF):
	movimientos = ["IZQUIERDA", "DERECHA", "ARRIBA", "ABAJO"]
	indice = 0
	return movimientos[listaF.index(min(listaF))]

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
	izquierda, derecha, arriba, abajo = False
	f_c, c_c = posicionConejo
	c_min = c_c - rangoVision
	f_min = f_c - rangoVision
	c_max = c_c + rangoVision
	f_max = f_c + rangoVision
	alto = len(tablero) - 1
	largo = len(tablero[0]) - 1
	if f_min < 0:
		arriba=True
		f_min = 0
	if c_min < 0:
		izquierda = True
		c_min = 0
	if c_max > largo:
		derecha = True
		c_max = largo
	if f_max > alto:
		abajo = True
		f_max = alto
	for f in range(f_min,f_max+1):
		lTemp=[]
		for c in range(c_min,c_max+1):
			lTemp.append (tablero [f][c])
		tableroVisible.append(lTemp)
	return tableroVisible,  izquierda, derecha, arriba, abajo

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

def zanahoriaMasCercana(zanahorias, vecinos):
	# Calcula la menor distancia entre un estado y una zanahoria
	distancias = []
	for posibleEstado in vecinos:
		x_e, y_e = posibleEstado
		tmp =[]
		for zanahoria in zanahorias:
			x_z, y_z = zanahoria
			tmp.append(abs(x_e-x_z) + abs(y_e-y_z))
		distancias.append(min(tmp))
	return distancias # Retorna la distancia menor desde el conejo hasta una zanahoria.


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

def penalizarAnterior(eAnterior, eActual):
	movimiento = eAnterior-eActual
	_d, _n = movimiento
	return _n


def movimiento(x,y):
	if (x == 0 and y == -1): # Izquierda
		return "IZQUIERDA", 0
	elif(x == 0 and y == -1): # Derecha
		return "DERECHA", 1
	elif(x == -1 and y == 0): # Arriba
		return "ARRIBA", 1	
	elif(x == 1 and y == 0): # Abajo
		return "ABAJO", 1		

def grupoZanahorias(tablero, vecinos):
	totalZanahorias = len(zanahorias)
	conta = 0
	pesos = []
	tmpZanahorias = 0
	x_v, y_v = v[0]
	for f in tablero: # Izquierda
		for c in f:
			if (conta <= y_v ):
				if (c=="Z"):
					tmpZanahorias+=1
			conta+=1
	pesos.append(totalZanahorias-tmpZanahorias)
	conta = 0
	tmpZanahorias=0
	x_v, y_v = v[1] # Derecha
	for f in tablero: 
		for c in f:
			if (conta >= y_v ):
				if (c=="Z"):
					tmpZanahorias+=1
			conta+=1
	pesos.append(totalZanahorias-tmpZanahorias)
	conta = 0
	tmpZanahorias=0
	x_v, y_v = v[2] # Arriba
	for f in tablero: 
		for c in f:
			if (conta <= x_v ):
				if (c=="Z"):
					tmpZanahorias+=1
			conta+=1
	pesos.append(totalZanahorias-tmpZanahorias)
	conta = 0
	tmpZanahorias=0
	x_v, y_v = v[3] # Abajo
	for f in tablero: 
		for c in f:
			if (conta >= x_v ):
				if (c=="Z"):
					tmpZanahorias+=1
			conta+=1
	pesos.append(totalZanahorias-tmpZanahorias)
	return pesos
def penalidadPared(paredIzq,paredDer, paredArr, paredAba):
	penalidades = []
	if (paredIzq==True):
		penalidades.append(15)
	else:
		penalidades.append(0)
	if (paredDer==True):
		penalidades.append(15)
	else:
		penalidades.append(0)	
	if (paredArr==True):
		penalidades.append(15)
	else:
		penalidades.append(0)	
	if (paredAba==True):
		penalidades.append(15)
	else:
		penalidades.append(0)	





def main(rangoVision = 1, zanahoriasPorComer = 3):
	abierta = []
	cerrada = []
	f, lG = [0,0,0,0]
	g, h = 0
	zanahoriasComidas = 0
	costoAcumulado = 0
	estadoAnterior=[-1, -1]
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
			lH = [0,0,0,0]
			paso+=1
			# Busca los espacios visibles
			tableroVisible, paredIzq, paredDer, paredArr, paredAba = getTableroVisible(tablero, rangoVision, posicionConejo)
			print("-------------------- Tablero visible --------------------")
			imprimirTablero(tableroVisible)
			lG = [x+g for x in lG] # Suma g a cada uno de los futuros estados
			coordenadasZanahorias = encontrarZanahorias(tableroVisible) # Obtiene las coordenadas de las zanahorias
			if (estadoAnterior[0]!= -1 and estadoAnterior[1] != -1):
				lH[penalizarEstadoAnterior(estadoAnterior, posicionConejo)] = 15 #penaliza el estado anterior
			print("PENALIDAD ESTADO ANTERIOR "+"IZQUIERDA: " + lH[0]+ "DERECHA: " + lH[1] +"ARRIBA: " + lH[2]+"ABAJO: " + lH[3])
			# Revisa si hay zanahorias en el tablero visible
			if (len(coordenadasZanahorias)!= 0):
				# Hay zanahorias a la vista
				# Sacar costo de la distancia del conejo a la zanahoria más cercana
				p1 = zanahoriaMasCercana(zanahorias, vecinos)
				lH = [x + y for x, y in zip(lH, p1)]
				print("PENALIDAD ZANAHORIA CERDA: "+"IZQUIERDA: " + lH[0]+ "DERECHA: " + lH[1] +"ARRIBA: " + lH[2]+"ABAJO: " + lH[3])
				p2 = grupoZanahorias(tableroVisible, vecinos)
				lH = [x + y for x, y in zip(lH, p2)]
				print("PENALIDAD GRUPO ZANAHORIAS"+"IZQUIERDA: " + lH[0]+ "DERECHA: " + lH[1] +"ARRIBA: " + lH[2]+"ABAJO: " + lH[3])
				p3 = penalidadPared(paredIzq,paredDer, paredArr, paredAba)
				lH = [x + y for x, y in zip(lH, p2)]
				print("PENALIDAD PARED: "+"IZQUIERDA: " + lH[0]+ "DERECHA: " + lH[1] +"ARRIBA: " + lH[2]+"ABAJO: " + lH[3])

				f = [x + y for x, y in zip(lH, lG)]
				mejorMovimiento = getMejorMovimiento(f)
				# Imprimir todos los costos y mejro movimiento
				imprimirCostosDeCadaMovimiento(paso, f, mejorMovimiento)
				# Guardar posición actual como posición anterior
				# Hacer el movimiento

			else:

				# No se ven zanahorias en el tablero.



			# Calcular el costo de cada movimiento
			calcularMejorMovimiento(posicionConejo, tableroVisible, posicionAnterior, tablero)
			# Imprime resultado
			imprimirCostosDeCadaMovimiento(paso , "FALTA", "FALTA")
			
		print("PASO: "+ getNumeroPaso+ " FINAL")


main(2, 2)
