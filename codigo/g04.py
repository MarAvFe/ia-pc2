# -*- coding: utf-8 -*-
import sys
import argparse
import os
import aEstrella as ae
#import libreria as lib
#import matplotlib.pyplot as plt
import time

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

    parser.add_argument('--benchmark', action = 'store_true', dest= "benchmark")

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
        if( (args.zanahorias==None) or (args.vision==None)):
            print("Faltan comandos!, Error!")
        else:
            print("  ALGORITMO A ESTRELLA ")
            #print(getStarTitle())
            ##Llama la funcion de a estrella
            ae.main_function(args.vision[0],args.zanahorias[0])

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

        print("  GENETICO ")
        print("Se imprime el mejor individuo cada 100 generaciones.")
        if args.benchmark == None:
            print(getGeneticTitle())
            solucion = lib.algoritmoGenetico(tableroInicial, direccionConejo, individuos, generaciones)
            print(solucion)
        else:
            tiemposIndividuos = []
            tiemposGeneraciones = []
            correctitudIndividuos = []
            correctitudGeneraciones = []
            valoresArbitrarios = [100,250,1000]  #,5000,10000]
            for i in valoresArbitrarios:
                start = time.time()
                solucion = lib.algoritmoGenetico(tableroInicial, direccionConejo, i, int(i*0.05))
                end = time.time()
                duracion = end-start
                tiemposIndividuos.append(duracion)
                correctitudIndividuos.append(solucion.puntaje)
                print("Individuos:", i, "Duracion:", duracion)
            for i in valoresArbitrarios:
                start = time.time()
                solucion = lib.algoritmoGenetico(tableroInicial, direccionConejo, int(i*0.05), i)
                end = time.time()
                duracion = end-start
                tiemposGeneraciones.append(duracion)
                correctitudGeneraciones.append(solucion.puntaje)
                print("Generaciones:", i, "Duracion:", duracion)
            print(tiemposIndividuos, tiemposGeneraciones)
            print(correctitudIndividuos, correctitudGeneraciones)

            plt.plot(valoresArbitrarios, tiemposIndividuos, '-bo')
            plt.plot(valoresArbitrarios, tiemposGeneraciones, '-ro')
            plt.axis([0, valoresArbitrarios[-1]*1.1, 0, high(tiemposIndividuos, tiemposGeneraciones)*1.1])
            plt.xlabel('Ind (Azul) / Gen (Rojo)')
            plt.ylabel('Duracion (s)')
            plt.show()

            plt.plot(valoresArbitrarios, correctitudIndividuos, '-bo')
            plt.plot(valoresArbitrarios, correctitudGeneraciones, '-ro')
            plt.plot([-10]+valoresArbitrarios[1:-1]+[valoresArbitrarios[-1]*2], [0 for i in valoresArbitrarios], '-g')
            plt.axis([0, valoresArbitrarios[-1]*1.1, minimum(correctitudIndividuos, correctitudGeneraciones), high(correctitudIndividuos, correctitudGeneraciones)*1.1])
            plt.xlabel('Ind (Azul) / Gen (Rojo)')
            plt.ylabel('Puntaje')
            plt.show()

    else:
        raise("Error en los comandos, agregue --a-estrella o --geneticos")


def high(lista1, lista2):
    return max(lista1[-1],lista2[-1])


def minimum(lista1, lista2):
    return min(lista1[0],lista2[0])


##def getStarTitle():
##    return """
##  .                 .         ____      .                           .                      .
##                             /    \            .          .         .                      ;
##            .               /      \                                :                  - --+- -
##                    .      /   /\   \ .      .      .         .     !           .          !
##   .                      /   /__\   \                              |        .             .
##            .            /            \               .            _|_         +
##
## .       .             /____/      \____\   .              
##                 .               .    .          .               `._|_,'
##               _________________      ____         __________       T
## .       .    /                 |    /    \    .  |          \      |
##     .       /    ______   _____| . /      \      |    ___    |     !
##             \    \    |   |       /   /\   \     |   |___>   |     :         . :
##           .  \    \   |   |      /   /__\   \  . |         _/      .       *
## .     ________>    |  |   | .   /            \   |   |\    \_______    .
##      |            /   |   |    /    ______    \  |   | \           |
##      |___________/    |___|   /____/      \____\ |___|  \__________|    .
##
## """


def getGeneticTitle():
    return """
                              ....
                           ,;;'''';;,                    ,;;;;,
                 ,        ;;'      `;;,               .,;;;'   ;
              ,;;;       ;;          `;;,';;;,.     ,&;;'     '
            ,;;,;;       ;;         ,;`;;;, `;::.  %%;'
           ;;;,;;;       `'       ,;;; ;;,;;, `::,%%;'
           ;;;,;;;,          .,%%%%%'% ;;;;,;;   %;;;
 ,%,.      `;;;,;;;,    .,%%%%%%%%%'%; ;;;;;,;;  %;;;
;,`%%%%%%%%%%`;;,;;'%%%%%%%%%%%%%'%%'  `;;;;;,;, %;;;
;;;,`%%%%%%%%%%%,; ..`%%%%%%%%;'%%%'    `;;;;,;; %%;;
 `;;;;;,`%%%%%,;;/, .. `""*'',%%%%%      `;;;;;; %%;;,
    `;;;;;;;,;;/////,.    ,;%%%%%%%        `;;;;,`%%;;
           ;;;/%%%%,%///;;;';%%%%%%,          `;;;%%;;,
          ;;;/%%%,%%%%%/;;;';;'%%%%%,             `%%;;
         .;;/%%,%%%%%//;;'  ;;;'%%%%%,             %%;;,
         ;;//%,%%%%//;;;'   `;;;;'%%%%             `%;;;
         ;;//%,%//;;;;'      `;;;;'%%%              %;;;,
         `;;//,/;;;'          `;;;'%%'              `%;;;
           `;;;;'               `;'%'                `;;;;
                                  '      .,,,.        `;;;;
                                      ,;;;;;;;;;;,     `;;;;
                                     ;;;'    ;;;,;;,    `;;;;
                                     ;;;      ;;;;,;;.   `;;;;
                                      `;;      ;;;;;,;;   ;;;;
                                        `'      `;;;;,;;  ;;;;
                                                   `;;,;, ;;;;
                                                      ;;, ;;;;
                                                        ';;;;;
                                                         ;;;;;
                                                        .;;;;'
                                                       .;;;;'
                                                      ;;;;;'
                                                     ,;;;;'"""

main()
