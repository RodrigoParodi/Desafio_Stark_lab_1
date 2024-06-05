from data_stark import lista_personajes
from Funciones_stark import *
from os import system

TAM = len(lista_personajes)
menu_opciones = ["       *** MENU OPCIONES ***\n","1)Superheroes genero M","2)Superheroes genero F",
                "3)Superheroe Masculino mas alto","4)Superheroes Masculino mas bajo",
                "5)Superheroe Femenino mas alto","6)Superheroe Femenino mas bajo","7)Altura Promedio genero M",
                "8)Altura promedio genero F","9)Agrupar por color de pelo","10)Agrupar por colro de ojos",
                "11)Agrupar por inteligencia","12)SALIR"]

try:
    superheroes = cargar_datos(lista_personajes, TAM)

    while True:
        system("cls")
        match mostrar_menu(menu_opciones):
            case "1":
                mostrar_heroes_genero(superheroes,"M")
            case "2":
                mostrar_heroes_genero(superheroes,"F")
            case "3":
                buscar_heroe_altura_max_min(superheroes,"genero","M")
            case "4":
                buscar_heroe_altura_max_min(superheroes,"genero","M",False)
            case "5":
                buscar_heroe_altura_max_min(superheroes,"genero","F")
            case "6":
                buscar_heroe_altura_max_min(superheroes,"genero","F",False)
            case "7":
                promedio_altura_genero(superheroes,"M")
            case "8":
                promedio_altura_genero(superheroes,"F")
            case "9":
                mostrar_superheroes_por_dato(superheroes,"color_pelo")
            case "10":
                mostrar_superheroes_por_dato(superheroes,"color_ojos")
            case "11":
                mostrar_superheroes_por_dato(superheroes,"inteligencia")
            case "12":
                break
            case other:
                print("OPCION INCORRECTA!!!!")
        system("pause")

except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)


