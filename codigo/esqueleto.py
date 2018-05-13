# ============================================== INDICACIONES GENERALES ===============================================
# Este documento define las funciones requeridas para construir el programa.
# Toda función de primer nivel, se debe documentar en este archivo y
# actualizarla en el documento de análisis del proyecto. Esto con la finalidad
# de llevar la documentación "en tiempo real".

# En la medida de lo posible, se debe mantener las funciones y variables en español
# =====================================================================================================================

# ===================================================== GLOSARIO ======================================================
# Variables:
#   - paso: variable global que lleva el consecutivo del paso que se está desarrollando
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


def obtenerNombreArchivo():
    # global paso
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

class Individuo:
    # tablero solo tiene las flechas
    # puntaje es un entero
    def __init__(self, tablero, puntaje):
        self.tablero = tablero
        self.puntaje = puntaje


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


def correrTablero(tablero):
    # global direcciones
    # recibe un tablero con direcciones y lo ejecuta
    # flechas = contarFlechas(tablero)
    # tablero = mezclarTableroConDirecciones(tablero, problema)
    # soluciones = []
    # for direccion in direcciones:
    #     soluciones.append( correrTableroAux(tablero, direccion) )
    # resultado = min(soluciones)
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


def funcionAjuste(individuo):
    # Verifica cuan correcta es una solucion
    # rubros = correrTablero(individuo.tablero)
    # individuo.puntaje = rubros.obtenerPuntaje()
    # return individuo
    pass


def crearPoblacion(n):
    # poblacion
    # for i in range(n):
    #     poblacion.append(individuoRandom())
    # return poblacion
    pass


def individuoRandom():
    # return Individuo(tableroRandom, -1)
    pass


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
    # generaciones = 0
    #
    # while(poblacion[0].puntaje < 100):  # Por definir segun la funcion de puntaje
    #     --- Puntuar individuos ---
    #     poblacionPuntuada = []
    #     for individuo in poblacion:
    #         poblacionPuntuada.append( funcionAjuste(individuo) )
    #     poblacion = ordenarPuntuados(poblacionPuntuada)  # Puntajes más altos de primero
    #
    #     --- Reproducción y selección ---
    #     nuevaGeneracion = []
    #     for i in range(len(poblacion)):
    #         padre1, padre2 = obtenerIndividuoAleatorio(poblacion)
    #         nuevaGeneracion.append( cruce( padre1, padre2 ) )
    #     poblacion = nuevaGeneracion
    #     generaciones += 1
    #     print("Generacion:", generaciones) if ( generaciones % 10 == 0 ) else None
    #     break if ( generaciones > 100 ) else None
    # return poblacion[0]
    pass
