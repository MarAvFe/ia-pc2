import random
import shutil
import os
from random import randint


# Busca y encuentra las coordenadas de todas las zanahorias en el tablero visible
def encontrarZanahorias(tablero):
	posicionZanahorias=[]
	for y in range(len(tablero)):
		for x in range(len(tablero[y])):
			if (tablero[y][x] == "Z"):
				posicionZanahorias.append([y, x])	
	return posicionZanahorias

# Encuentra las coordenadas del conejo
def encontrarConejo(tablero):
	for y in range(len(tablero)):
		for x in range(len(tablero[y])):
			if tablero[y][x] == "C":
				return (y,x)
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
def moverConejoTablero(posicionConejo, movimientoGanador, tablero):
	f, c = posicionConejo
	print("posicion del conejo: "+","+ str(f)+ ","+ str(c))
	tablero[f][c] = " " # Elimina al conejo de la posición en la que se encontraba
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
	return comioZanahoria, tablero

def getMejorMovimiento(listaF):
    movimientos = ["IZQUIERDA", "DERECHA", "ARRIBA", "ABAJO"]

    minimoValor = min(listaF)
    apareceEnLista = listaF.count(minimoValor)
    
    if(apareceEnLista>1):
        r = random.randint(0,3)
        while ( minimoValor != listaF[r] ):
            r = random.randint(0,3)                    
        return movimientos[r]
    else:
        return movimientos[listaF.index(min(listaF))]

def imprimirCostosDeCadaMovimiento(paso, costoPorMovimiento, movimientoGanador):
	print("PASO: "+ str(paso).zfill(5) + " IZQUIERDA: "+ str(costoPorMovimiento[0]) +
										" DERECHA: " + str(costoPorMovimiento[1]) +
										" ARRIBA: " + str(costoPorMovimiento[2]) +
										" ABAJO: "+ str(costoPorMovimiento[3])  + 
										" MOVIMIENTO: "+ str( movimientoGanador))
	#PASO: 00001 IZQUIERDA: 5 DERECHA: 3 ARRIBA: 8 ABAJO: 9 MOVIMIENTO: DERECHA

def getTableroVisible(tablero, rangoVision, posicionConejo):
	tableroVisible = []
	izquierda = False
	derecha = False
	arriba = False
	abajo = False
	x_ConejoVisible=-1
	y_ConejoVisible=-1
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
	nFilas = 0
	nColumnas = 0
	for i in tableroVisible:
		for j in i:
			if j=="C":
				x_ConejoVisible=nFilas
				y_ConejoVisible=nColumnas
			nColumnas+=1
		nColumnas=0
		nFilas+=1

	print("posicionConejoVisible_x: "+ str(x_ConejoVisible)+", posicionConejoVisible_y: "+ str(y_ConejoVisible))
	return (x_ConejoVisible,y_ConejoVisible), tableroVisible,  izquierda, derecha, arriba, abajo

def imprimirTablero(tablero):
	for f in range(len(tablero)):
		tmp=""
		for c in range(len(tablero[f])):
			if (tablero[f][c]==" "):
				tmp+=" · "
			else:
                                
				tmp+=' '+tablero[f][c]+' '
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
	print("Posición del conejo: "+ str( posicionConejo[0])+", "+str(posicionConejo[1]))
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
			listaVecinos.append([_x, _y])
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

# total de zanahorias - zanahorias encontradas en la sección. Penaliza si en la sección no hay suficientes zanahorias juntas.
def grupoZanahorias(tablero, v, zanahorias):
	totalZanahorias = len(zanahorias)
	conta = 0
	pesos = []
	tAncho = len(tablero[0])
	tAlto = len(tablero)
	print(str(tAlto)+","+str(tAncho))
	tmpZanahorias = 0
	x_v, y_v = v[0]
	#print("x_v: "+ str(x_v))
	#print("y_v: "+ str(y_v))
	for f in tablero: # Izquierda
		for c in f:
			
			if (conta <= y_v ):
				#print ("C:"+str(c))
				if (c=="Z"):
					tmpZanahorias+=1
			conta+=1
		print("\n")
		conta=0
	print("total zanahorias: "+ str(totalZanahorias)+"tmpzanahorias: "+str(tmpZanahorias))
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
		conta=0
	pesos.append(totalZanahorias-tmpZanahorias)
	#conta = 0

	tmpZanahorias=0
	print("arriba 2: ")
	x_v, y_v = v[2] # Arriba
	print("x_v: "+ str(x_v))
	print("y_v: "+ str(y_v))
	conta = x_v
	print("conta: "+str(conta))
	for f in tablero: 
		#print("iteración")
		for c in f:
			if (conta <= x_v and conta >=0):
				#print ("C:"+str(c)+", contador: "+str(conta))
				if (c=="Z"):
					tmpZanahorias+=1
			else:
				break
		conta-=1
	pesos.append(totalZanahorias-tmpZanahorias)

	tmpZanahorias=0
	print("abajo: ")
	x_v, y_v = v[3] # Abajo
	print("x_v: "+ str(x_v))
	print("y_v: "+ str(y_v))
	conta = 0
	print("conta: "+str(conta))
	for f in tablero: 
		#print("iteración")
		for c in f:
			if (conta >= x_v):
				#print ("C:"+str(c)+", contador: "+str(conta))
				if (c=="Z"):
					tmpZanahorias+=1
			else:
				break
		conta+=1
	pesos.append(totalZanahorias-tmpZanahorias)
	return pesos

def penalidadPared(paredIzq,paredDer, paredArr, paredAba):
	peso = 15
	print(">>>>>>>>>>>>>>>>>> penalidad por chocar con pared <<<<<<<<<<<<<<<<< ")
	penalidades = []
	if (paredIzq==True):
		penalidades.append(peso)
	else:
		penalidades.append(0)
	if (paredDer==True):
		penalidades.append(peso)
	else:
		penalidades.append(0)	
	if (paredArr==True):
		penalidades.append(peso)
	else:
		penalidades.append(0)	
	if (paredAba==True):
		penalidades.append(peso)
	else:
		penalidades.append(0)	
	return penalidades

def penalizarEstadoAnterior(ultimoMovimientoGanador, vecinos):
	peso=15
	penalizacion = [0,0,0,0]
	if (ultimoMovimientoGanador=="IZQUIERDA"):
		return [0,peso,0,0]#Penalizar DERECHA
	elif (ultimoMovimientoGanador=="DERECHA"):
		return [peso,0,0,0]#Penalizar IZQUIERDA	
	elif (ultimoMovimientoGanador=="ARRIBA"):
		return [0,0,0, peso]#Penalizar ABAJO	
	elif (ultimoMovimientoGanador=="ABAJO"):
		return [0,0,peso,0]#Penalizar ARRIBA	
	return penalizacion


def main_function(rangoVision , zanahoriasPorComer , nombreTableroInicial="tableroInforme.txt"):
	borrarResultadosPrevios()
	abierta = []
	cerrada = []
	f = [0,0,0,0]
	lG = [0,0,0,0]
	g = 0
	h = 0
	ultimoMovimientoGanador=""
	zanahoriasComidas = 0
	costoAcumulado = 0
	estadoAnterior=[-1, -1]
	#costoRegular = 1.0
	borrarResultadosPrevios() # Borra carpeta que contiene resultados de la corrida anterior
	paso = 0
	print("********** Tablero inicial **********")
	tablero = leerTableroInicial(nombreTableroInicial)	
	imprimirTablero(tablero)
	posicionConejo = encontrarConejo(tablero)
	cantidadInicialZanahorias = cantidadZanahoriasTablero (tablero)
	posicionAnterior = posicionConejo # Inicial, en este caso
	zanahoraisComidas = 0
	# Revisa si es que las condiciones son válidas, si se puede iniciar.
	if ((cantidadInicialZanahorias < zanahoriasPorComer) or (posicionConejo[0]==-1 and posicionConejo[1]==-1)):
		print ("Error al ingresar los parámetros")
	else:
		while(zanahoriasPorComer != zanahoriasComidas):
			lH = [0,0,0,0]
			paso+=1
			posicionConejo = encontrarConejo(tablero)
			# Busca los espacios visibles
			posicionConejoVisible, tableroVisible, paredIzq, paredDer, paredArr, paredAba = getTableroVisible(tablero, rangoVision, posicionConejo)
			vecinos = getVecinos(posicionConejoVisible, tableroVisible)

			print("-------------------- Tablero visible --------------------")
			imprimirTablero(tableroVisible)
			lG = [x+g for x in lG] # Suma g a cada uno de los futuros estados
			coordenadasZanahorias = encontrarZanahorias(tableroVisible) # Obtiene las coordenadas de las zanahorias

			# Penalizar para que no regrese a posición a la posición de donde viene
# **** NO BORRAR			
#			if (ultimoMovimientoGanador!=""):
#				p0 = penalizarEstadoAnterior(ultimoMovimientoGanador, vecinos)
#				print("PENALIDAD ESTADO ANTERIOR "+"IZQUIERDA: " + str(p0[0])+ "DERECHA: " + 
#				str(p0[1]) +"ARRIBA: " + str(p0[2])+"ABAJO: " + str(p0[3]))
#				lH = [x + y for x, y in zip(lH, p0)]
# **** FIN DE NO BORRAR

			# Penalizar para que no choque con la pared
##			p3 = penalidadPared(paredIzq,paredDer, paredArr, paredAba) #falta revisar
##			print("PENALIDAD PARED:  "+"IZQUIERDA: " + str(p3[0])+ ", DERECHA: " + 
##			str(p3[1]) +", ARRIBA: " + str(p3[2])+", ABAJO: " + str(p3[3]))				
##			lH = [x + y for x, y in zip(lH, p3)]

			# Revisa si hay zanahorias en el tablero visible
			if (len(coordenadasZanahorias)!= 0):
				# Hay zanahorias a la vista
				# Sacar costo de la distancia del conejo a la zanahoria más cercana
				
				p1 = zanahoriaMasCercana(coordenadasZanahorias, vecinos)
				lH = [x + y for x, y in zip(lH, p1)] #suma la penalidad anterior al heurístico
				
##				print("* COORDENADAS VECINOS: "+ str(vecinos[0][0])+","+str(vecinos[0][1])+", "
##					+str(vecinos[1][0])+","+str(vecinos[1][1])+
##					","+str(vecinos[2][0])+ ","+str(vecinos[2][1])+
##					","+str(vecinos[3][0])+","+str(vecinos[3][1]))
##				
				print("PENALIDAD zanahoria cercana: "+"IZQUIERDA: " + str(p1[0])+ ", DERECHA: " + 
				str(p1[1]) +", ARRIBA: " + str(p1[2])+", ABAJO: " + str(p1[3]))		
				# Calcula la penalidad según grupo de zanahorias que tenga cerca		
				p2 = grupoZanahorias(tableroVisible, vecinos, coordenadasZanahorias)
				lH = [x + y for x, y in zip(lH, p2)]
				print("PENALIDAD Grupo zanahorias:  "+"IZQUIERDA: " + str(p2[0])+ ", DERECHA: " + 
				str(p2[1]) +", ARRIBA: " + str(p2[2])+", ABAJO: " + str(p2[3]))

				f = [x + y for x, y in zip(lH, lG)]
				print("F:  "+"IZQUIERDA: " + str(f[0])+ ", DERECHA: " + 
				str(f[1]) +", ARRIBA: " + str(f[2])+", ABAJO: " + str(f[3]))		
				mejorMovimiento = getMejorMovimiento(f)
				ultimoMovimientoGanador=mejorMovimiento
				# Imprimir todos los costos y mejro movimiento
				imprimirCostosDeCadaMovimiento(paso, f, mejorMovimiento)
#				posicionAnterior= encontrarConejo(tablero)
				print("********** tablero antes de movimiento")
				imprimirTablero(tablero)
				dd,gg = encontrarConejo(tablero)
				print("posicion conejo tablero original antes de moverlo: "+"-->" +str(dd)+","+str(gg))
				comioZanahoria, tablero = moverConejoTablero(encontrarConejo(tablero), mejorMovimiento, tablero)
				# Revisa si se comió una zanahoria en el movimiento
				if (comioZanahoria== True):
					zanahoriasComidas+=1

			# No hay zanahorias en el tablero visible	
			else:
				print("**************** NO HAY ZANAHORIAS VISIBLES, SE HACE UN MOVIMIENTO ALEATORIO ***************************")
				#ultimoMovimientoGanador=
				f = [x + y for x, y in zip(lH, lG)]
				print("F:  "+"IZQUIERDA: " + str(f[0])+ ", DERECHA: " + 
				str(f[1]) +", ARRIBA: " + str(f[2])+", ABAJO: " + str(f[3]))	
				mejorMovimiento = getMejorMovimiento(f)
				ultimoMovimientoGanador=mejorMovimiento				
				comioZanahoria, tablero = moverConejoTablero(encontrarConejo(tablero), mejorMovimiento, tablero)
				# No se ven zanahorias en el tablero. Movimiento aleatorio, pero no regresar a la posición anterior

			g+=1
			print("*********** TABLERO VISIBLE")
			imprimirTablero(tableroVisible)
			print("-> CANTIDAD DE ZANAHORIAS COMIDAS: " + str(zanahoriasComidas))
			print("-> CANTIDAD DE ZANAHORIAS POR COMER: " + str(zanahoriasPorComer))	
			input("PRESIONAR UNA TECLA PARA EL SIGUIENTE MOVIMIENTO") 
			guardarArchivo(tablero, str(paso).zfill(5))
			
	print("PASO: "+ str(paso).zfill(5) + " FINAL")


main_function(5,3)
