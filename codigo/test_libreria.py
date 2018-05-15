from libreria import *


# =====================================================================================================================
# ============================================== Algoritmo A* =========================================================
# =====================================================================================================================

def test_calcularCostoPasos():
    # assert calcularCostoPasos() == True
    pass


def test_calcularCosto():
    # assert calcularCosto(direccion) == True
    pass

# =====================================================================================================================
# =========================================== Algoritmo Genético ======================================================
# =====================================================================================================================

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


def test_ordenarPuntuados():
    poblacion = crearPoblacion(50)
    for i in poblacion:
        i.puntaje = gauss(30,30)
    #    print(i.tablero)
    #print("---")
    poblacion = ordenarPuntuados(poblacion)
    #for i in poblacion:
    #    print(i.puntaje)
    assert poblacion[0].puntaje > poblacion[1].puntaje
    assert poblacion[0].puntaje > poblacion[2].puntaje
    assert poblacion[0].puntaje > poblacion[-1].puntaje
    assert poblacion[-2].puntaje > poblacion[-1].puntaje


def test_crearArchivoSalida():
    # assert crearArchivoSalida() == True
    pass


def test_documentarPaso():
    # assert documentarPaso(archivoSalida, cadena) == True
    pass


def test_cerrarArchivoSalida():
    # assert cerrarArchivoSalida(archivoSalida) == True
    pass


def test_obtenerNombreArchivo():
    # assert obtenerNombreArchivo(paso) == True
    pass


def test_leerProblema():
    # assert leerProblema(nombre) == True
    pass


def test_imprimirIndividuo():
    # assert imprimirIndividuo(tablero, consecutivo) == True
    pass


def test_obtenerEstadoTablero():
    # assert obtenerEstadoTablero(tablero) == True
    pass


def test_contarFlechas():
    tablero5Flechas = [
        [' ','A',' ',' '],
        [' ','A',' ',' '],
        [' ',' ','>',' '],
        [' ',' ',' ',' '],
        ['<',' ',' ','V'],
        [' ',' ',' ',' ']
    ]
    tablero2Flechas = [
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        ['<',' ',' ','V'],
        [' ',' ',' ',' ']
    ]
    assert contarFlechas(tablero5Flechas) == 5
    assert contarFlechas(tablero2Flechas) == 2
    pass


def test_mezclarTableroConDirecciones():
    tablero = [
        [' ',' ','C',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ','Z'],
        ['Z',' ',' ',' '],
        [' ',' ',' ',' '],
        ['Z',' ',' ',' ']
    ]
    tableroConChoque = [
        [' ','C',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ','Z'],
        ['Z',' ',' ',' '],
        [' ',' ',' ',' '],
        ['Z',' ',' ',' ']
    ]
    direcciones = [
        [' ','A',' ',' '],
        [' ','A',' ',' '],
        [' ',' ','>',' '],
        [' ',' ',' ',' '],
        ['<',' ',' ','V'],
        [' ',' ',' ',' ']
    ]
    assert mezclarTableroConDirecciones(tablero, direcciones) == [
        [' ','A','C',' '],
        [' ','A',' ',' '],
        [' ',' ','>','Z'],
        ['Z',' ',' ',' '],
        ['<',' ',' ','V'],
        ['Z',' ',' ',' ']
    ]
    assert mezclarTableroConDirecciones(tableroConChoque, direcciones) == []


def test_obtenerNuevaDireccion():
    global IZQUIERDA
    global ARRIBA
    global DERECHA
    global ABAJO
    tab1 = [
        [' ','A','C',' '],
        [' ','A',' ',' '],
        [' ',' ','>','Z'],
        ['Z',' ',' ',' '],
        ['<',' ',' ','V'],
        ['Z',' ',' ',' ']
    ]
    tab2 = [
        [' ','A','C',' '],
        [' ','A',' ',' '],
        [' ',' ','>','Z'],
        ['Z',' ',' ',' '],
        ['<',' ',' ','V'],
        ['Z',' ',' ',' ']
    ]
    tab3 = [
        [' ','A',' ',' '],
        [' ','A','C',' '],
        [' ',' ','>','Z'],
        ['Z',' ',' ',' '],
        ['<',' ',' ','V'],
        ['Z',' ',' ',' ']
    ]
    assert obtenerNuevaDireccion(tab1, IZQUIERDA) == ARRIBA
    assert obtenerNuevaDireccion(tab2, DERECHA) == DERECHA
    assert obtenerNuevaDireccion(tab3, ABAJO) == DERECHA


def test_correrTablero():
    global ABAJO
    global problema
    problema = [
        [' ',' ','C',' '],
        [' ',' ',' ',' '],
        [' ','Z',' ','Z'],
        ['Z',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' ']
    ]
    tablero = [
        [' ','A',' ',' '],
        [' ','A',' ',' '],
        ['V',' ','<',' '],
        [' ',' ',' ',' '],
        ['>',' ',' ','A'],
        [' ',' ',' ',' ']
    ]
    res = correrTablero(tablero, ABAJO, 1)
    assert type(res[0]) == Puntaje
    assert type(res[0].obtenerPuntaje()) == int
    assert type(res[1]) == list
    assert type(res[1][0]) == list
    assert res[1] == [
        [' ','A',' ',' '],
        [' ','A',' ',' '],
        [' ',' ',' ','C'],
        [' ',' ',' ',' '],
        [' ',' ',' ',' '],
        [' ',' ',' ',' ']
    ]


def test_funcionAjuste():
    # assert funcionAjuste(individuo, direccion, consecutivo) == True
    pass

def test_obtenerIndividuosAleatorios():
    assert len(obtenerIndividuosAleatorios(crearPoblacion(5))) == 2
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
test_funcionAjuste()
test_obtenerIndividuosAleatorios()
test_buscarSolucion()
test_ordenarPuntuados()
test_obtenerNuevaDireccion()
