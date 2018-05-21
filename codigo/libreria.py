from random import randint, gauss
from multiprocessing import Pool
import numpy as np
from shared import *
import os
import time
import threading
import multiprocessing
import resource
import fcntl
import shutil

# ============================================== INDICACIONES GENERALES ===============================================
# Este documento define las funciones requeridas para construir el programa.
# Toda función de primer nivel, se debe documentar en este archivo y
# actualizarla en el documento de análisis del proyecto. Esto con la finalidad
# de llevar la documentación "en tiempo real".

# En la medida de lo posible, se debe mantener las funciones y variables en español
# =====================================================================================================================

# ===================================================== GLOSARIO ======================================================
# Variables:
#   - direcciones: arreglo con los posibles tókens de direcciones
#   - poblacion: Una lista de individuos
#   - problema: tablero con conejo y zanahorias leido de la entrada
# Métodos:
#   - archivoSalida: Este archivo se refiere a la salida del algoritmo en consola que detalla los pasos que toma el
#     conejo, no al tablero en cada uno de ellos. También se puede ver como las indicaciones.
# =====================================================================================================================

ARRIBA      = 'A'
IZQUIERDA = '<'
DERECHA      =  '>'
ABAJO     =   'V'
PUNTOSMIN = -99999
paso  = 0
direcciones = [ IZQUIERDA, DERECHA, ABAJO, ARRIBA ]
problema = []
N = 15
M = 20


c = {
    'ENDC'    : '\033[0m',
    'RED'     : '\033[1;31m',
    'YELLOW'  : '\033[1;33m',
    'BLUE'    : '\033[1;34m',
    'BINBACK' : '\x1b'
}


def crearArchivoSalida():
    # Crear el archivo de salida y retornar el puntero
    pass


def documentarPaso(archivoSalida, cadena):
    # Agregar la cadena al final de archivoSalida
    # Imprimir la misma cadena a la consola print(cadena)
    pass


def cerrarArchivoSalida(archivoSalida):
    # close(archivoSalida)
    pass


def imprimirTablero(tablero):
    # nombre = obtenerNombreArchivo()
    # Crear archivo crearArchivo(nombre, 'w') en modo escritura
    # Imprimir tablero en el archivo
    # Cerrar el archivo
    pass


def obtenerNombreArchivo(paso):
    nombre = '0000' + str(paso)
    return nombre[-5:]


def leerProblema(nombre):
    # Lee el archivo con el tablero a solucionar
    pass

# =====================================================================================================================
# ============================================== Algoritmo A* =========================================================
# =====================================================================================================================
def calcularCostoPasos():
    # global direcciones
    # for direccion in direcciones:
    #     costos.append(calcularCosto(direccion))
    # return costos
    pass


def calcularCosto(direccion):
    # De manera oscura calcular esta carajada. Es un heurístico
    # return costo
    pass

# =====================================================================================================================
# =========================================== Algoritmo Genético ======================================================
# =====================================================================================================================

DIRECCION = ""
GENERACION = 1

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      pass

class Individuo:
    # tablero solo tiene las flechas
    # puntaje es un entero
    def __init__(self, tablero, puntaje):
        self.tablero = tablero
        self.puntaje = puntaje

    def __str__(self):
        toPrt = "Puntaje: " + str(self.puntaje) + "\n"
        toPrt += imprimirTablero(self.tablero)
        return toPrt



class Puntaje:
    # correcto dice si este acomodo conlleva a una solución
    # pasos: total de pasos para acabar en solución o error
    # flechas: total de flechas del tablero
    totalZanahoriasProblema = -1
    def __init__(self, correcto, pasos, zanahorias, flechas = -1):
        self.correcto = correcto
        self.pasos = pasos
        self.flechas = flechas
        self.zanahorias = zanahorias

    def obtenerPuntaje(self):
        # puntaje es una tupla (bool, int) donde el bool es si el tablero
        #   es una solución y el int la cantidad de pasos.
        # Puntuar si la función es una solución y la cantidad de pasos que toma
        return ((10000 if self.correcto else 0) -
                (self.pasos * 5) -
                (self.flechas * 100) +
                (1000 * (Puntaje.totalZanahoriasProblema - self.zanahorias)))

    def __str__(self):
        toPrt = "\nCorrecto: " + str(self.correcto)
        toPrt += "\nPasos: " + str(self.pasos)
        toPrt += "\nFlechas: " + str(self.flechas)
        toPrt += "\nZanahorias: " + str(self.zanahorias)
        return toPrt


def imprimirTablero(tablero, archivo = False):
    if (len(tablero) == 0):
        return "┌Tablero:─┐\n└─────────┘"
    tb = "┌Tablero:"
    toPrt = tb
    unders = ""
    while(len(tb)+len(unders) <= len(tablero[0])):
        unders += "─"
    unders += "┐\n"
    toPrt += unders
    for i in tablero:
        toPrt += "│"
        if archivo:
            for j in i:
                toPrt += j
        else:
            for j in i:
                if j == "C":
                    toPrt += c['RED'] + j
                elif j == "Z":
                    toPrt += c['YELLOW'] + j
                else:
                    toPrt += c['BLUE'] + j
                toPrt += c['ENDC']
        toPrt += "│\n"
    toPrt += "└────────" + unders[:-2] + "┘"
    return toPrt


def get_open_fds():
    fds = []
    soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    for fd in range(0, soft):
        try:
            flags = fcntl.fcntl(fd, fcntl.F_GETFD)
        except IOError:
            continue
        fds.append(fd)
    return fds

def get_file_names_from_file_number(fds):
    names = []
    for fd in fds:
        names.append(os.readlink('/proc/self/fd/%d' % fd))
    return names


def imprimirIndividuo(tablero, consecutivo):
    # Imprimir tablero
    global c
    directory = "../output/" + str(DIRECCION) + "/" + obtenerNombreArchivo(GENERACION) + "/"
    name = obtenerNombreArchivo(consecutivo) + ".txt"
    if not os.path.exists(directory):
        os.makedirs(directory)
    strTablero = imprimirTablero(tablero, True)
    with open(directory + name, "w") as file:
        file.write(strTablero)


def obtenerEstadoTablero(tablero):
    # Cuenta la cantidad de zanahorias en el tablero
    global direcciones
    result = 0
    for i, fil in enumerate(tablero):
        for j, col in enumerate(fil):
            if( tablero[i][j] == 'Z' ):
                result += 1
    return result


def contarFlechas(tablero):
    # Cuenta la cantidad de flechas en el tablero
    global direcciones
    flechas = 0
    for i, fil in enumerate(tablero):
        for j, col in enumerate(fil):
            if( tablero[i][j] in direcciones ):
                flechas += 1
    return flechas


def mezclarTableroConDirecciones(tablero, direcciones, forzar = False):
    # tablero y direcciones son arerglos de nxm
    # Ubica las direcciones dentro del tablero
    # retorna un solo tablero con las direcciones, el conejo y las zanahorias
    # print("mezcl",imprimirTablero(tablero), imprimirTablero(direcciones))
    for i, fil in enumerate(tablero):
        for j, col in enumerate(fil):
            if( ( (tablero[i][j] == "C") or (tablero[i][j] == "Z") ) and (direcciones[i][j] != " ") ):
                if forzar:
                    tablero[i][j] = direcciones[i][j]
                    continue
                return []
            if(direcciones[i][j] != " "):
                tablero[i][j] = direcciones[i][j]
    return tablero


def isConejoVivo(tablero):
    return obtenerPosicionConejo(tablero) != (-1,-1)


def obtenerNuevaDireccion(tablero, direccion):
    pos = obtenerPosicionConejo(tablero)
    if (direccion == ARRIBA):
        pos = (pos[0]-1, pos[1])
    if (direccion == ABAJO):
        pos = (pos[0]+1, pos[1])
    if (direccion == DERECHA):
        pos = (pos[0], pos[1]+1)
    if (direccion == IZQUIERDA):
        pos = (pos[0], pos[1]-1)
    try:
        val = tablero[pos[0]][pos[1]]
        if ((val != " ") and (val != "C") and (val != "Z")):
            return tablero[pos[0]][pos[1]]
    except Exception as e:
        None
    return direccion


def alistar(tablero):
    nuTab = []
    for fil in tablero:
        tmp = []
        nuTab.append(list(fil))#tmp)
    return nuTab


def correrTablero(tablero, direccion, consecutivo = -1):
    # recibe un tablero con una dirección y lo ejecuta
    global problema
    global DIRECCION
    global GENERACION
    flechas = contarFlechas(tablero)
    tablero = mezclarTableroConDirecciones(tablero, problema)
    if (tablero == []):
        return Puntaje(False, PUNTOSMIN)
    resultado = correrTableroAux(tablero, direccion)
    resultado.flechas = flechas
    return resultado


def correrTableroAux(tablero, direccion):
    direccionActual = direccion
    totalPasos = 0
    while(isConejoVivo(tablero)):
        zanahorias = obtenerEstadoTablero(tablero)
        if (obtenerEstadoTablero(tablero) == 0):
            return Puntaje(True, totalPasos, zanahorias)
        nuevaDireccion = obtenerNuevaDireccion(tablero, direccionActual)
        tablero = darPaso(tablero, direccionActual)
        if (tablero == []):
            break
        #print("================================boopsi2", imprimirTablero(tableroNuevo))
        direccionActual = nuevaDireccion
        totalPasos += 1
        # time.sleep(0.3)
        copiaTablero = tablero
    return Puntaje(False, totalPasos, zanahorias)


def obtenerPosicionConejo(tablero):
    for i, fil in enumerate(tablero):
        for j, col in enumerate(fil):
            if( tablero[i][j] == 'C' ):
                return (i, j)
    #print("DEBUG: Conejo no encontrado en:", tablero)
    return (-1, -1)


def darPaso(tablero, direccion):
    global N
    global M
    def pasoValido(tablero, pos, direccion):
        if ( (direccion == ARRIBA) and (pos[0] == 0) ):
            return False
        if ( (direccion == ABAJO) and (pos[0] == len(tablero)-1) ):
            return False
        if ( (direccion == DERECHA) and (pos[1] == len(tablero[0])-1) ):
            return False
        if ( (direccion == IZQUIERDA) and (pos[1] == 0) ):
            return False
        return True
    pos = obtenerPosicionConejo(tablero)  # (x,y)
    if( (not pasoValido(tablero, pos, direccion)) or (pos == (-1,-1))):
        return []
    tablero[pos[0]][pos[1]] = ' '
    if (direccion == ARRIBA):
        tablero[pos[0]-1][pos[1]] = 'C'
    if (direccion == ABAJO):
        tablero[pos[0]+1][pos[1]] = 'C'
    if (direccion == DERECHA):
        tablero[pos[0]][pos[1]+1] = 'C'
    if (direccion == IZQUIERDA):
        tablero[pos[0]][pos[1]-1] = 'C'
    return tablero


def funcionAjusteOld(tablero, direccion, consecutivo):
    # Verifica cuan correcta es una solucion
    if (
        (len(tablero) != len(problema)) or
        (len(tablero[0]) != len(problema[0]))):
        raise Exception("El problema y el tamaño de tablero de los tableros tienen tamaños diferentes: (" +
                        str(len(problema)) + "x" + str(len(problema[0])) + ") != (" +
                        str(len(tablero)) + "x" + str(len(tablero[0])) + ")")
    res = correrTablero(tablero, direccion, consecutivo)
    return res.obtenerPuntaje()


def funcionAjuste(tablero, direccion, consecutivo):
    # Verifica cuan correcta es una solucion
    res = correrTablero(tablero, direccion, consecutivo)
    return res.obtenerPuntaje()


def probarSolucion(tablero, direccion):
    res = correrTablero(tablero, direccion)
    return res.correcto


def crearPoblacion(n):
    poblacion = []
    for i in range(n):
        poblacion.append(individuoRandom())
    return poblacion


def piezaAleatoria():
    v = randint(0,5)
    return  (' '        if v > 4 else (
            (ARRIBA     if v > 3 else (
            (ABAJO      if v > 2 else (
            (DERECHA    if v > 1 else
            IZQUIERDA) )) )) ))


def individuoRandom():
    tablero = []
    for fil in range(N):
        fila = []
        for col in range(M):
            fila.append(' ')#piezaAleatoria())
        tablero.append(tuple(fila))
    return Individuo(tablero, PUNTOSMIN)


def obtenerIndividuosAleatorios(poblacion):
    # Dist. gaussiana centrada al principio de la población ordenada
    # Elige más a menudo los individuos al principio de la lista
    maximo = len(poblacion)
    mu, sigma = 0, maximo/3
    idx1 = abs(int(np.random.normal(mu, sigma, 1)[0])) % maximo
    idx2 = abs(int(np.random.normal(mu, sigma, 1)[0])) % maximo
    return  poblacion[idx1], poblacion[idx2]


def ordenarPuntuados(arr):
    # Recibe una poblacion puntuada y la ordena de mayor a menor
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j].puntaje > arr[j-1].puntaje:
            arr[j], arr[j-1] = arr[j-1], arr[j]  #swap
            j = j-1
        imprimirIndividuo(arr[i-1].tablero, i)
    return arr


def cruce(padre1, padre2):
    division = randint(1,len(padre1.tablero)-2)
    hijo = Individuo(padre1.tablero[:division] + padre2.tablero[division:], PUNTOSMIN)
    hijo = mutar(hijo)
    return hijo


def mutar(individuo):
    v = randint(0,1800)
    mutar = 3 if (v < 50) else 2 if (v < 300) else 1 if (v < 1000) else 0
    while (mutar > 0):
        #print(imprimirTablero(individuo.tablero))
        #print("mutacion....")
        randFil = randint(0,len(individuo.tablero))
        randCol = randint(0,len(individuo.tablero[0]))
        tablero = []
        for fil in range(len(individuo.tablero)):
            fila = []
            for col in range(len(individuo.tablero[0])):
                if ( (fil == randFil) and (col == randCol) ):
                    fila.append(piezaAleatoria())
                else:
                    fila.append(individuo.tablero[fil][col])
            tablero.append(tuple(fila))
        individuo = Individuo(tablero, PUNTOSMIN)
        mutar -= 1
        #print(imprimirTablero(individuo.tablero))
    return individuo


def paralelo(poblacion):
    global DIRECCION
    poblacionPuntuada = []
    startIdx = poblacion[1]
    poblacion = poblacion[0]
    for idx, individuo in enumerate(poblacion):
        if individuo.tablero == []:
            continue
        poblacion[idx].puntaje = funcionAjuste(alistar(individuo.tablero), DIRECCION, startIdx + idx)
        poblacionPuntuada.append( individuo )
    return poblacionPuntuada

def puntuar(poblacion, direccion):
    threads = multiprocessing.cpu_count()
    pool = Pool(processes=threads)
    poblacionFragmentada = []
    divisor = len(poblacion) / threads
    for i in range(threads):
        poblacionFragmentada.append((poblacion[ int(i * divisor) : int((i+1) * divisor)], i))
    results = pool.map(paralelo, poblacionFragmentada)
    puntuado = []
    for r in results:
        puntuado += r
    return puntuado


def vaciarCarpetaDireccion():
    folder = "../output/" + str(DIRECCION)
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)


def buscarSolucion(direccion, tope, individuos):
    global N
    global M
    N = len(problema)
    M = len(problema[0])
    Puntaje.totalZanahoriasProblema = obtenerEstadoTablero(problema)
    vaciarCarpetaDireccion()
    # Retorna al individuo más apto
    # --- Crear población inicial ---
    poblacion = crearPoblacion(individuos)
    global DIRECCION
    global GENERACION
    DIRECCION = direccion
    multi = False

    while(True):  #not probarSolucion(alistar(poblacion[0].tablero), DIRECCION)):
        # --- Puntuar individuos ---
        if (not multi):  # Single thread
            poblacionPuntuada = []
            for idx, individuo in enumerate(poblacion):
                if individuo.tablero == []:
                    continue
                poblacion[idx].puntaje = funcionAjuste(alistar(individuo.tablero), DIRECCION, idx)
                poblacionPuntuada.append( individuo )
        else:  # MULTITHREAD
            poblacionPuntuada = puntuar(poblacion, DIRECCION)

        poblacionOrdenada = ordenarPuntuados(poblacionPuntuada)  # Puntajes más altos de primero

        # --- Reproducción y selección ---
        nuevaGeneracion = []
        # 5% viejos, 60% cruzados, 35% nuevos
        idxCruce = int(len(poblacion) * 0.05)
        idxNuevos = int(len(poblacion) * 0.65)
        for i in range(len(poblacionOrdenada[:idxCruce])):
            nuevaGeneracion.append(poblacionOrdenada[i])
        for i in range(len(poblacionOrdenada[idxCruce:idxNuevos])):
            padre1, padre2 = obtenerIndividuosAleatorios(poblacionOrdenada)
            nuevaGeneracion.append( cruce( padre1, padre2 ) )
        for i in crearPoblacion(len(poblacionOrdenada[idxNuevos:])):
            nuevaGeneracion.append(i)

        poblacion = nuevaGeneracion
        GENERACION += 1
        if GENERACION % 100 == 0:
            print("Top de generacion", str(GENERACION) + ":")
            print(poblacion[0])
        if ( GENERACION + 1 > tope ):
            break
    print("Generaciones totales:", GENERACION)
    return poblacion[0]


# start = time.time()
# top = buscarSolucion(ABAJO)
# print("=============== RESULTADOS ===============")
# print("Solución", top)
# print(imprimirTablero(mezclarTableroConDirecciones(alistar(top.tablero), problema)))
# end = time.time()
# print(end - start)

def algoritmoGenetico(tableroInicial, direccionConejo, individuos, generaciones):
    global problema
    problema = leerTablero(tableroInicial)
    direccion = {
        0: IZQUIERDA,
        1: DERECHA,
        2: ARRIBA,
        3: ABAJO
    }.get(direccionConejo, IZQUIERDA)
    mejor = buscarSolucion(direccion, generaciones, individuos)
    mezcla = mezclarTableroConDirecciones(problema, alistar(mejor.tablero), True)
    print(imprimirTablero(mezcla))
    return mejor


## ANOTAR EN ANÁLISIS
# El algoritmo tiene problemas con las zanahorias en los bordes, ya que requiere de una
# ruta alternativa muy costosa de generar, y por "más vale pájaro en mano..." no encuentra nuevos caminos.
