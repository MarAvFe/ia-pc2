
from random import randint

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
paso  = 0
direcciones = [ IZQUIERDA, DERECHA, ABAJO, ARRIBA ]
problema = []
N = 15
M = 20

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
    # nombre = '0000' + str(paso)
    # return nombre[-5]
    pass


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
GENERACION = 0

class Individuo:
    # tablero solo tiene las flechas
    # puntaje es un entero
    def __init__(self, tablero, puntaje):
        self.tablero = tablero
        self.puntaje = puntaje

    def __str__(self):
        tb = "|Tablero:"
        toPrt = "Puntaje: " + str(self.puntaje) + "\n"
        toPrt += tb
        unders = ""
        while(len(tb)+len(unders) <= len(self.tablero[0])):
            unders += "─"
        unders += "|\n"
        toPrt += unders
        for i in self.tablero:
            toPrt += "|"
            for j in i:
                toPrt += j
            toPrt += "|\n"
        toPrt += "└────────" + unders
        return toPrt



class Puntaje:
    # correcto dice si este acomodo conlleva a una solución
    # pasos: total de pasos para acabar en solución o error
    # flechas: total de flechas del tablero
    def __init__(self, correcto, pasos, flechas = -1):
        self.correcto = correcto
        self.pasos = pasos
        self.flechas = flechas

    def obtenerPuntaje(self):
        # puntaje es una tupla (bool, int) donde el bool es si el tablero
        #   es una solución y el int la cantidad de pasos.
        # Puntuar si la función es una solución y la cantidad de pasos que toma
        # return int
        pass

    def __str__(self):
        toPrt = "Correcto: " + str(self.correcto)
        toPrt += "\nPasos: " + str(self.pasos)
        toPrt += "\nFlechas: " + str(self.flechas)
        return toPrt


def imprimirIndividuo(tablero, consecutivo):
    # Imprimir tablero
    # name = "./output/" + DIRECCION + "/" + GENERACION + "/" + obtenerNombreArchivo(consecutivo) + ".txt"
    pass


def obtenerEstadoTablero(tablero):
    # Cuenta la cantidad de zanahorias en el tablero
    pass


def contarFlechas(tablero):
    # Cuenta la cantidad de flechas en el tablero
    pass


def mezclarTableroConDirecciones(tablero, direcciones):
    # tablero y direcciones son arerglos de nxm
    # Ubica las direcciones dentro del tablero
    # retorna un solo tablero con las direcciones, el conejo y las zanahorias
    pass


def correrTablero(tablero, direccion, consecutivo):
    # recibe un tablero con direcciones y lo ejecuta
    # flechas = contarFlechas(tablero)
    # tablero = mezclarTableroConDirecciones(tablero, problema)
    # imprimirIndividuo(tablero, consecutivo)
    # resultado = correrTableroAux(tablero, direccion)
    # resultado.flechas = flechas
    # return resultado
    pass


def correrTableroAux(tablero, direccion):
    # direccionActual = direccion
    # totalPasos = 0
    # while(isConejoVivo(tablero)):
    #     if (obtenerEstadoTablero(tablero) > 0):
    #         return Puntaje(True, totalPasos)
    #     tablero = darPaso(tablero, direccionActual)
    #     totalPasos += 1
    # return Puntaje(False, totalPasos)
    pass

def obtenerPosicionConejo(tablero):
    for i, fil in enumerate(tablero):
        for j, col in enumerate(fil):
            if( tablero[i][j] == 'C' ):
                return (i, j)
    print("DEBUG: Conejo no encontrado en:", tablero)
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



def funcionAjuste(individuo, direccion, consecutivo):
    # Verifica cuan correcta es una solucion
    # rubros = correrTablero(individuo.tablero, direccion, consecutivo)
    # individuo.puntaje = rubros.obtenerPuntaje()
    # return individuo
    pass


def crearPoblacion(n):
    poblacion = []
    for i in range(n):
        poblacion.append(individuoRandom())
    return poblacion


def individuoRandom():
    def piezaAleatoria():
        v = randint(0,100)
        return  (' '        if v > 4 else (
                (ARRIBA     if v > 3 else (
                (ABAJO      if v > 2 else (
                (DERECHA    if v > 1 else
                IZQUIERDA) )) )) ))
    tablero = []
    for fil in range(N):
        fila = []
        for col in range(M):
            fila.append(piezaAleatoria())
        tablero.append(fila)
    return Individuo(tablero, -1)


def obtenerIndividuoAleatorio(poblacion):
    # X^2 para elegir más a menudo a los individuos con mayor puntaje
    # idx1 = int( chi2( 0, len(poblacion) ) )
    # idx2 = int( chi2( 0, len(poblacion) ) )
    # return poblacion[idx1], poblacion[idx2]
    pass


def buscarSolucion():
    # Retorna al individuo más apto
    # --- Crear población inicial ---
    # poblacion = crearPoblacion(n)
    # global DIRECCION
    # global GENERACION
    #
    # while(poblacion[0].puntaje < 100):  # Por definir segun la funcion de puntaje
    #     --- Puntuar individuos ---
    #     poblacionPuntuada = []
    #     for individuo in poblacion:
    #         poblacionPuntuada.append( funcionAjuste(individuo, DIRECCION, poblacion.indexOf(individuo)) )
    #     poblacion = ordenarPuntuados(poblacionPuntuada)  # Puntajes más altos de primero
    #
    #     --- Reproducción y selección ---
    #     nuevaGeneracion = []
    #     for i in range(len(poblacion)):
    #         padre1, padre2 = obtenerIndividuoAleatorio(poblacion)
    #         nuevaGeneracion.append( cruce( padre1, padre2 ) )
    #     poblacion = nuevaGeneracion
    #     GENERACION += 1
    #     print("Generacion:", GENERACION) if ( GENERACION % 10 == 0 ) else None
    #     break if ( GENERACION > 100 ) else None
    # return poblacion[0]
    pass


# =====================================================================================================================
# =========================================== Sección de Pruebas ======================================================
# =====================================================================================================================
