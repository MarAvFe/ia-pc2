# ============================================== INDICACIONES GENERALES ===============================================
 ## Este documento define las funciones requeridas para construir el programa.
 ## Toda función de primer nivel, se debe documentar en este archivo y
 ## actualizarla en el documento de análisis del proyecto. Esto con la finalidad
 ## de llevar la documentación "en tiempo real".

 ## En la medida de lo posible, se debe mantener las funciones y variables en español
# =====================================================================================================================

# ===================================================== GLOSARIO ======================================================
# Variables:
#   - paso: variable global que lleva el consecutivo del paso que se está desarrollando
#   - direcciones: arreglo con los posibles tókens de direcciones
# Métodos:
#   - archivoSalida: Este archivo se refiere a la salida del algoritmo en consola que detalla los pasos que toma el
#     conejo, no al tablero en cada uno de ellos. También se puede ver como las indicaciones.
# =====================================================================================================================

IZQUIERDA = '<'
DERECHA = '>'
ABAJO = 'V'
ARRIBA = 'A'
paso = 0
direcciones = [ IZQUIERDA, DERECHA, ABAJO, ARRIBA ]

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

def obtenerEstadoTablero(tablero):
    # Cuenta la cantidad de zanahorias en el tablero
    pass

def mezclarTableroConDirecciones(tablero, direcciones):
    # tablero y direcciones son arerglos de nxm
    # Ubica las direcciones dentro del tablero
    # retorna un solo tablero con las direcciones
    pass

def correrTablero(tablero):
    # global direcciones
    # recibe un tablero con direcciones y lo ejecuta
    # soluciones = []
    # for direccion in direcciones:
    #     soluciones.append(correrTableroAux(tablero, direccion))
    # return soluciones
    pass

def correrTableroAux(tablero, direccion):
    # direccionActual = direccion
    # totalPasos = 0
    # while(isConejoVivo(tablero)):
    #     if (obtenerEstadoTablero(tablero) > 0):
    #         return True, totalPasos
    #     tablero = darPaso(tablero, direccionActual)
    #     totalPasos += 1
    # return False, totalPasos
    pass

def funcionAjuste(soluciones):
    # Verifica cuan correcta es una solucion
    # true = correrTablero(solucion)
    pass

def generarSolucion():
    pass
