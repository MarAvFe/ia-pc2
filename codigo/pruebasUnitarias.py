from aEstrella import *

def test_getMejorMovimiento():
	funcion =  getMejorMovimiento([12,56,2,19])
	assert funcion == "ARRIBA"

def test_cantidadZanahorias():
	funcion = cantidadZanahoriasTablero([["Z","","Z"],["Z","","Z"]])
	assert funcion == 4

def test_movimiento():
	funcion = movimiento(0,-1)
	assert funcion == ("IZQUIERDA", 0)

def test_penalidadPared():
	funcion = penalidadPared(True, False, False, False)	
	assert funcion[0] == 15

def test_penalizarEstadoAnterior():
	funcion = penalizarEstadoAnterior("IZQUIERDA",[])
	assert funcion[1] == 15

