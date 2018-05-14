from libreria import *


def test_crearPoblacion():
    pob = crearPoblacion(5)
    # print(pob)
    assert len(pob) == 5
    assert type(pob[0]) == Individuo


def test_individuoRandom():
    ind = individuoRandom()
    # print(ind)
    assert type(ind) == Individuo
    assert type(ind.tablero) == list
    assert type(ind.tablero[0]) == list

def test_darPaso():
    tablero = [
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ','C',' '],
        [' ',' ',' ',' ']
    ]
    tablero2 = [
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ','C']
    ]
    tablero3 = [
        ['C',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' ']
    ]
    unbunnied = [
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' ']
    ]
    # print(darPaso(tablero, ABAJO))
    # print(darPaso(tablero2, DERECHA))
    assert darPaso(tablero, ABAJO) == [
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ','C',' ']
    ]
    assert darPaso(tablero2, DERECHA) == []
    assert darPaso(tablero2, ABAJO) == []
    assert darPaso(tablero3, ARRIBA) == []
    assert darPaso(tablero3, IZQUIERDA) == []
    assert darPaso(unbunnied, DERECHA) == []


def test_crearArchivoSalida():
    # assert crearArchivoSalida() == True
    pass


def test_documentarPaso():
    # assert documentarPaso(archivoSalida, cadena) == True
    pass


def test_cerrarArchivoSalida():
    # assert cerrarArchivoSalida(archivoSalida) == True
    pass


def test_imprimirTablero():
    # assert imprimirTablero(tablero) == True
    pass


def test_obtenerNombreArchivo():
    # assert obtenerNombreArchivo(paso) == True
    pass


def test_leerProblema():
    # assert leerProblema(nombre) == True
    pass


def test_calcularCostoPasos():
    # assert calcularCostoPasos() == True
    pass


def test_calcularCosto():
    # assert calcularCosto(direccion) == True
    pass


def test_imprimirIndividuo():
    # assert imprimirIndividuo(tablero, consecutivo) == True
    pass


def test_obtenerEstadoTablero():
    # assert obtenerEstadoTablero(tablero) == True
    pass


def test_contarFlechas():
    # assert contarFlechas(tablero) == True
    pass


def test_mezclarTableroConDirecciones():
    # assert mezclarTableroConDirecciones(tablero, direcciones) == True
    pass


def test_correrTablero():
    # assert correrTablero(tablero, direccion, consecutivo) == True
    pass


def test_correrTableroAux():
    # assert correrTableroAux(tablero, direccion) == True
    pass


def test_funcionAjuste():
    # assert funcionAjuste(individuo, direccion, consecutivo) == True
    pass

def test_obtenerIndividuoAleatorio():
    # assert obtenerIndividuoAleatorio(poblacion) == True
    pass


def test_buscarSolucion():
    # assert buscarSolucion() == True
    pass


test_crearPoblacion()
test_individuoRandom()
test_darPaso()
test_crearArchivoSalida()
test_documentarPaso()
test_cerrarArchivoSalida()
test_imprimirTablero()
test_obtenerNombreArchivo()
test_leerProblema()
test_calcularCostoPasos()
test_calcularCosto()
test_imprimirIndividuo()
test_obtenerEstadoTablero()
test_contarFlechas()
test_mezclarTableroConDirecciones()
test_correrTablero()
test_correrTableroAux()
test_funcionAjuste()
test_obtenerIndividuoAleatorio()
test_buscarSolucion()
