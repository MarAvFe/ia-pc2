import argparse
from aEstrella import *










def usage():
    print("""Usage:
    --tablero-inicial <direccion/archivo.txt> --a-estrella --vision <n> --zanahorias <n>
    --tablero-inicial <direccion/archivo.txt> --genetico [--derecha|--izquierda|--arriba|--abajo] --individuos <n>
    """)

def getArgumentos():
    parser = argparse.ArgumentParser(description='Search Algorithms')
    #General
    parser.add_argument('--tablero-inicial', nargs = 1, type = str, dest="direccion")
    #A*
    parser.add_argument('--a-estrella', action='store_true', dest="a_estrella")
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
        
    #python main.py --tablero-inicial entrada.txt --a-estrella --vision 2 --zanahorias 5    
    #python main.py --tablero-inicial entrada.txt --genetico --derecha --individuos 3 --generaciones 1000
    return parser

def main():
    #usage()
    parser = getArgumentos()
    args = parser.parse_args()

    if args.a_estrella:
        if( (args.zanahorias==None) or (args.vision==None) or (args.direccion ==None)):
            print("Faltan comandos!, Error!")
        else:
            print("||||||| ALGORITMO A ESTRELLA |||||||")
            print("Direccion del txt:" + args.direccion[0])
            print("Vision de:")
            print(args.vision[0])
            print("Zanahorias:")
            print(args.zanahorias[0])        

    elif args.genetico:
        if(args.individuos==None or args.generaciones==None):
            print("Faltan comandos!, Error!")
        else:
            direccion_conejo = ""
            if args.izquierda:
                direccion_conejo = "izquierda"
            elif args.derecha:
                direccion_conejo = "derecha"
            elif args.arriba:
                direccion_conejo = "arriba"
            elif args.abajo:
                direccion_conejo = "abajo"            

            print("||||||| GENETICO |||||||")
            print("Direccion del txt:" + args.direccion[0])
            print("Direccion conejo:" + args.direccion[0])
            print("Individuos:")
            print(args.individuos[0])
            print("Generaciones:")
            print(args.generaciones[0])  

    else:
        print("Error en los comandos, agregue --a-estrella o --geneticos")
        



main()
    
    
