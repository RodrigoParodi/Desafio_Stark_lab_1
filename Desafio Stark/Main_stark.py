from Funciones_stark import *
from data_stark import lista_personajes
from os import system


TAM = len(lista_personajes)
menu_opciones = ["\n        *** MENU DE OPCIONES ***\n","1)Mostrar Nombres","2)Mostrar Nombres y Alturas",
                "3)Superheroe mas alto","4)Superheroe mas bajo","5)Calcular Promedio Altura",
                "6)Superheroe mas y menos pesado","7)Salir"]

try:
    superheroes = cargar_datos(lista_personajes, TAM)

    while True:
        system("cls")
        match mostrar_menu(menu_opciones):
            case "1":
                mostrar_nombres_superheroes(superheroes)
            case "2":
                mostrar_nombre_altura(superheroes)
            case "3":
                superheroe_maximo(superheroes,"altura")
            case "4":
                superheroe_minimo(superheroes,"altura")
            case "5":
                calcular_promedio(superheroes, "altura")
            case "6":
                superheroe_maximo(superheroes,"peso")
                superheroe_minimo(superheroes,"peso")
            case "7":
                break
            case other:
                print("OPCION INCORRECTA!!!!")
        system("pause")

except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
