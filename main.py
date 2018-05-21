import argparse










def usage():
    print("""Usage:
    --tablero-inicial <direccion/archivo.txt> --a-estrella --vision <n> --zanahorias <n>
    --tablero-inicial <direccion/archivo.txt> --genetico [--derecha|--izquierda|--arriba|--abajo] --individuos <n>
    """)

def getArgumentos():
    parser = argparse.ArgumentParser(description='Search Algorithms')
    #General
    parser.add_argument('--tablero-inicial', nargs = 1, type = str)
    #A*
    parser.add_argument('--a-estrella', action='store_true')
    parser.add_argument('--vision', nargs = 1, type = int)
    parser.add_argument('--zanahorias', nargs = 1, type = int)
    #Genetico
    parser.add_argument('--genetico', action='store_true')
    parser.add_argument('--derecha', action='store_true')
    parser.add_argument('--izquierda', action='store_true')
    parser.add_argument('--arriba', action='store_true')
    parser.add_argument('--abajo', action='store_true')
    parser.add_argument('--individuos', nargs = 1, type = int)
    parser.add_argument('--generaciones', nargs = 1, type = int)
        
    #python main.py --tablero-inicial entrada.txt --a-estrella --vision 2 --zanahorias 5    
    #python main.py --tablero-inicial entrada.txt --genetico --derecha --individuos 3 --generaciones 1000
    return parser

def main():
    #usage()
    parser = getArgumentos()
    args = parser.parse_args()
    print(args)


main()
    
    
