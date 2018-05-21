import sys
import argparse
#import a_estrella as ae
import libreria as lib


def usage():
    print("""Usage:
    python3 main.py --tablero_inicial <direccion/archivo.txt> --a_estrella --vision <n> --zanahorias <n>
    python3 main.py --tablero_inicial <direccion/archivo.txt> --genetico [--derecha|--izquierda|--arriba|--abajo] --individuos <n> --generaciones <n>
    """)

def getArgumentos():
    parser = argparse.ArgumentParser(description='Search Algorithms')
    #General
    parser.add_argument('--tablero_inicial', nargs = 1, type = str, dest="tablero_inicial")
    #A*
    parser.add_argument('--a_estrella', action='store_true', dest="a_estrella")
    parser.add_argument('--vision', nargs = 1, type = int, dest="vision")
    parser.add_argument('--zanahorias', nargs = 1, type = int, dest = "zanahorias")

    #Genetico
    parser.add_argument('--genetico', action='store_true',dest="genetico")
    parser.add_argument('--derecha', action='store_true',dest="derecha")
    parser.add_argument('--izquierda', action='store_true',dest="izquierda")
    parser.add_argument('--arriba', action='store_true', dest = "arriba")
    parser.add_argument('--abajo', action='store_true', dest="abajo")
    parser.add_argument('--individuos', nargs = 1, type = int, dest="individuos")
    parser.add_argument('--generaciones', nargs = 1, type = int, dest= "generaciones")

    #python main.py --tablero_inicial entrada.txt --a-estrella --vision 2 --zanahorias 5
    #python main.py --tablero_inicial entrada.txt --genetico --derecha --individuos 3 --generaciones 1000
    return parser

def main():
    #usage()
    parser = getArgumentos()
    args = parser.parse_args()
    if(args.tablero_inicial == None):
        raise("No ha proporcionado un tablero inicial")
    tableroInicial = args.tablero_inicial[0]
    if args.a_estrella:
        if( (args.zanahorias==None) or (args.vision==None) or (args.direccion ==None)):
            print("Faltan comandos!, Error!")
        else:
            print("======= ALGORITMO A ESTRELLA =======")
            print("Direccion del txt:" + args.direccion[0])
            print("Vision de:")
            print(args.vision[0])
            print("Zanahorias:")
            print(args.zanahorias[0])
            ##Llama la funcion de a estrella
            ae.main_function(arg.vision[0],args.zanahorias[0])

    elif args.genetico:
        if(args.individuos==None):
            print("Definiendo 50 generaciones por defecto.")
            individuos = 50
        else:
            individuos = args.individuos[0]
        if(args.generaciones==None):
            print("Definiendo 200 generaciones por defecto.")
            generaciones = 200
        else:
            generaciones = args.generaciones[0]
        if args.izquierda:
            direccionConejo = 0
        elif args.derecha:
            direccionConejo = 1
        elif args.arriba:
            direccionConejo = 2
        elif args.abajo:
            direccionConejo = 3

        print("======= GENÉTICO =======")
        print("Direccion del txt:", tableroInicial)
        print("Direccion conejo:", direccionConejo)
        print("Individuos:")
        print(individuos)
        print("Generaciones:")
        print(generaciones)
        solucion = lib.algoritmoGenetico(tableroInicial, direccionConejo, individuos, generaciones)
        print(solucion)
    else:
        raise("Error en los comandos, agregue --a-estrella o --geneticos")




main()
