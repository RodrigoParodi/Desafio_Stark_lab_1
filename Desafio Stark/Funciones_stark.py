
#------------------------- CARGAR LISTA NUEVA CON DATOS VALIDADOS ---------------------------
def cargar_datos(lista:list,cantidad:int)->list:
    """Carga una lista de datos nueva con datos validados

    Args:
        lista (list): lista de donde obtendremos los datos
        cantidad (int): cantidad de datos cargados en la lista

    Returns:
        list: Lista nueva cargada
    """
    lista_nueva = []
    for i in range(cantidad):
        validar_int(lista[i],"fuerza")

        validar_float(lista[i],"altura")
        validar_float(lista[i],"peso")

        validar_str(lista[i],"nombre")
        validar_str(lista[i],"identidad")
        validar_str(lista[i],"empresa")
        validar_str(lista[i],"genero")
        validar_str(lista[i],"color_ojos")
        validar_str(lista[i],"color_pelo")
        validar_str(lista[i],"inteligencia")

        lista_nueva.append(lista[i])
    return lista_nueva

def validar_str(datos:dict,campo:str):
    """Valida que un tipo de dato almacenado en un campo del diccionario sea un string y si lo es le otorga 
        un nuevo formato

    Args:
        datos (dict): Diccionario de datos que vamos a validar
        campo (str): Llave del diccionario que queremos validar

    Raises:
        TypeError: Si lo ingresado no es un string lanzara una excepcion.
    """
    valor = datos[campo]
    if type(valor) == str:
        if len(datos[campo]) > 0:
            datos[campo] = valor.lower().capitalize()
        else:
            datos[campo] = "N/A"
    else:
        raise TypeError("Esto no es un String!!!")

def validar_int(datos:dict,campo:str):
    """Valida que el tipo de dato almacenado en un campo del diccionario sea un numero Entero

    Args:
        datos (dict): Diccionario de datos que vamos a validar
        campo (str): Llave del diccionario que queremos validar

    Raises:
        TypeError: En caso de que lo ingresado no sea un numero entero lanzara una excepcion.
    """
    valor = datos[campo]
    if type(valor) != int:
        if valor.isdigit():
            datos[campo] = int(valor)
        else:
            raise TypeError("Esto no es un numero entero!!!")


def validar_float(datos:dict,campo:str):
    """Valida que el tipo de dato almacenado en un campo del diccionario sea un numero flotante

    Args:
        datos (dict): Diccionario de datos que vamos a validar
        campo (str): Llave del diccionario que queremos validar

    Raises:
        TypeError: En caso de que lo ingresado no sea un numero flotante lanzara una excepcion.
    """
    valor = datos[campo]
    if type(valor) != float:
        if valor.replace('.', '').isdigit() == True:
            datos[campo] = float(valor)
        else:
            raise TypeError("Esto no es un numero flotante!!!")

#--------------------------------------------------------------------------------------------
#B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe

def mostrar_nombres_superheroes(lista:list):
    """Recorre la lista y muestra por consola el nombre de todos los superheroes

    Args:
        lista (list): Lista a recorrer

    Raises:
        ValueError: Si la lista se encuetra vacia lanzara una excepcion
    """
    if len(lista) > 0:
        print("          *** NOMBRES SUPERHEROES ***")
        for dato in lista:
            print(f"-{dato['nombre']}")
    else:
        raise ValueError("Error , Lista vacia!!!")

#--------------------------------------------------------------------------------------------
#C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
#la altura del mismo

def mostrar_nombre_altura(lista:list):
    """Recorre la lista mostrando por consola el nombre de los superheroes junto a su altura

    Args:
        lista (list): Lista a recorrer

    Raises:
        ValueError: Si la lista se encuetra vacia lanzara una excepcion
    """
    if len(lista) > 0:
        print("       *** NOMBRES Y ALTURAS ***")
        print(" NOMBRE             ALTURA")
        print("----------------------------------------------------")
        for dato in lista:
            print(f"{dato['nombre']:<20} {dato['altura']:0.2f}")
    else:
        raise ValueError("Error , Lista vacia!!!")

#--------------------------------------------------------------------------------------------
#D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
#G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
#indicadores anteriores (MÁXIMO, MÍNIMO)
#H. Calcular e informar cual es el superhéroe más y menos pesado.

def buscar_maximo(lista:list,clave:str):
    """Busca el valor maximo almacenado en uno de los campos de un diccionario

    Args:
        lista (list): Lista donde se buscara el valor maximo
        clave (str): Clave del campo / llave del diccionario donde realizaremos la busqueda

    Returns:
        _type_: Retorna el valor maximo
    """
    bandera = True
    for dato in lista:
        if bandera == True or dato[clave] > valor_maximo:
            valor_maximo = dato[clave]
            bandera = False
    return valor_maximo

def superheroe_maximo(lista:list,clave:str):
    """Muestra el nombre y el dato del superheroe con el valor maximo buscado en uno de sus datos

    Args:
        lista (list): lista donde se ralizara la busqueda del valor maximo
        clave (str): Clave del campo / llave del diccionario donde realizaremos la busqueda
    """
    valor_maximo = buscar_maximo(lista,clave)
    print(f"\n          *** SUPERHEROE MAYOR {clave.upper()} ***")
    print(f" NOMBRE             {clave.upper()}")
    print("----------------------------------------------------")
    for dato in lista:
        if dato[clave] == valor_maximo:
            print(f"{dato['nombre']:<20} {dato[clave]:0.2f}")

#--------------------------------------------------------------------------------------------
#E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
#G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
#indicadores anteriores (MÁXIMO, MÍNIMO)
#H. Calcular e informar cual es el superhéroe más y menos pesado.

def buscar_minimo(lista:list,clave:str):
    """Busca el valor minimo almacenado en uno de los campos de un diccionario

    Args:
        lista (list): Lista donde se buscara el valor minimo
        clave (str): Clave del campo / llave del diccionario donde realizaremos la busqueda

    Returns:
        _type_: Retorna el valor minimo
    """
    bandera = True
    for dato in lista:
        if bandera == True or dato[clave] < valor_minimo:
            valor_minimo = dato[clave]
            bandera = False
    return valor_minimo

def superheroe_minimo(lista:list,clave:str):
    """Muestra el nombre y el dato del superheroe con el valor minimo buscado en uno de sus datos

    Args:
        lista (list): lista donde se ralizara la busqueda del valor minimo
        clave (str): Clave del campo / llave del diccionario donde realizaremos la busqueda
    """
    valor_minimo = buscar_minimo(lista,clave)
    print(f"\n          *** SUPERHEROE MENOR {clave.upper()} ***")
    print(f" NOMBRE             {clave.upper()}")
    print("----------------------------------------------------")
    for dato in lista:
        if dato[clave] == valor_minimo:
            print(f"{dato['nombre']:<20} {dato[clave]:0.2f}")


#--------------------------------------------------------------------------------------------
#F. Recorrer la lista y determinar la altura promedio de los superhéroes
#(PROMEDIO)

def acumulador(lista:list,clave:str):
    """Acumula la cantidad de X datos almacenados en un campo especifico

    Args:
        lista (list): lista donde se realizara la busqueda
        clave (str): Campo / llave donde obtendremos los valores para acumularlos

    Returns:
        _type_: El total de la acumulacion
    """
    acumulador = 0
    for dato in lista:
        acumulador = acumulador + dato[clave]
    return acumulador


def calcular_promedio(lista:list,clave:str):
    """Calcula el promedio y lo muetra por consola

    Args:
        lista (list): lista donde se obtendra los datos
        clave (str): campo / llave del valor que vamos a calcular el promedio
    """
    divisor = len(lista)
    dividendo = acumulador(lista,clave)
    promedio = dividir(dividendo, divisor)
    print(f"El promedio de {clave} es de {promedio:0.2f}")
    


def dividir(dividendo,divisor):
    """Divide dos numeros y retorna su resultado

    Args:
        dividendo (_type_): Primer numero
        divisor (_type_):  Segundo numero

    Raises:
        ZeroDivisionError: Si dividimos por zero lanzara una excepcion

    Returns:
        _type_: Resultado de la division
    """
    if divisor > 0:
        return dividendo / divisor
    else:
        raise ZeroDivisionError("No se puede dividir por 0 !!!!")
    

#--------------------------------------------------------------------------------------------
#J. Construir un menú que permita elegir qué dato obtener


def mostrar_menu(lista_menu:list):
    """Imprimira por consola un menu de opciones

    Args:
        lista_menu (list): Lista que debe contener las opciones a mostrar del menu

    Returns:
        _type_: Devuelve la opcion escogida por el usuario
    """
    from os import system
    for opcion in lista_menu:
        print(opcion)
    opcion = input("Ingrese una opcion : ")
    system("cls")
    return opcion