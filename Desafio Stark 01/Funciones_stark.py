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
            datos[campo] = "No hair"
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
        
#-----------------------------------------------------------------------------------------------------
#A Y B

def obtener_heroes_dato(lista:list,clave:str,dato:str)->list:
    """Devuelve una lista con todos los superheroes que cumplan con una caracteristica

    Args:
        lista (list): Lista dodne se realizara la busqueda
        clave (str): Campo del diccionario
        dato (str): Dato que queremos buscar

    Raises:
        ValueError: Si la lista esa vacia lanzara una excepcio 

    Returns:
        _type_: Lista nueva con los datos encontrados
    """
    lista_dato= []

    if len(lista) > 0:
        for heroe in lista:
            if heroe[clave] == dato:
                lista_dato.append(heroe)
    else:
        raise ValueError("Lista Vacia!!!")

    return lista_dato

def mostrar_heroes_genero(lista:list,genero:str):
    """Recorre la lista y imprime el nombre y genero de los heroes por consola

    Args:
        lista (list): Lista que se va a recorrer
        genero (str): Genero que queremos mostrar

    Raises:
        ValueError: si la lista esta vacia retornara una excepcion
    """
    lista_genero = obtener_heroes_dato(lista,"genero",genero)
    if len(lista_genero) > 0:
        print("     *** LISTA MASCULINOS ***")
        for heroe in lista_genero:
            print(f"{heroe['nombre']:<20} {heroe['genero']}")
    else:
        raise ValueError("Lista vacia!!!")
    
#-------------------------------------------------------------------------------------------------------------
#C #D #E #F #I

def buscar_heroe_altura_max_min(lista:list,clave:str,dato:str,criterio = True):
    """Busca en la lista al heroe M o F mas alto y lo muestra por consola

    Args:
        lista (list): Lista dodne se realizara la busqueda
        clave (str): Campo para bucar por genero o otra condicion similar
        dato (str): Dato que estamos buscando
    """
    lista_dato = obtener_heroes_dato(lista,clave,dato)
    valor = buscar_maximo_minimo(lista_dato,"altura",criterio)
    for dato in lista_dato:
        if dato["altura"] == valor:
            print(f"{dato['nombre']:<20} {dato['genero']:<5} {dato['altura']:0.2f}")


def buscar_maximo_minimo(lista:list,clave:str,criterio = True):
    """Busca un valor maximo o un valor minimo dentro de una lista

    Args:
        lista (list): lista donde se realizara la busqueda
        clave (str): Campo del valor maximo o minimo que queremos encontrar
        criterio (bool, optional): False si queremos buscar el minimo . Defaults to True.

    Returns:
        bool: Valor maxio o minimo
    """
    if criterio == False:
        valor = buscar_minimo(lista,clave)
    else:
        valor = buscar_maximo(lista,clave)
    return valor

def buscar_maximo(lista:list,clave:str):
    """Busca un valor maximo dentro de la lista

    Args:
        lista (list): lista donde se realizara la busqueda
        clave (str): campo del diccionario donde buscaremos el valor maximo que queremos

    Raises:
        ValueError: Si la lista esta vacia lanzara una excepcion

    Returns:
        _type_: retorna el valor maximo
    """
    bandera = False
    if len(lista) > 0:
        for dato in lista:
            if bandera == False or dato[clave] > valor_maximo:
                valor_maximo = dato[clave]
                bandera = True
    else:
        raise ValueError("Lista Vacia!!!")
    return valor_maximo

def buscar_minimo(lista:list,clave:str):
    """Busca un valor Minimo dentro de la lista

    Args:
        lista (list): lista donde se realizara la busqueda
        clave (str): campo del diccionario donde buscaremos el valor minimo que queremos

    Raises:
        ValueError: Si la lista esta vacia lanzara una excepcion

    Returns:
        _type_: retorna el valor minimo
    """
    bandera = False
    if len(lista) > 0:
        for dato in lista:
            if bandera == False or dato[clave] < valor_minimo:
                valor_minimo = dato[clave]
                bandera = True
    else:
        raise ValueError("Lista Vacia!!!")
    return valor_minimo

#-------------------------------------------------------------------------------------------------------------
#G #H

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

def promedio_altura_genero(lista:list,genero:str):
    """Calcula el promedio por altura en una lista con heroes del mismo genero

    Args:
        lista (list): lista donde sacaremos los superheroes
        genero (str): genero en el cual queremos calcular el proemdio
    """
    lista_dato = obtener_heroes_dato(lista,"genero",genero)
    divisor = len(lista_dato)
    dividendo = acumulador(lista_dato,"altura")
    promedio = dividir(dividendo,divisor)
    print(f"La altura promedio de los superheroes '{genero}' es : {promedio:0.2f}")

#-------------------------------------------------------------------------------------------------------------
#J #K #L #M #N #O

def obtener_lista_sin_repetidos(lista:list,clave:str):
    """Genera una lista con datos sin repetirse

    Args:
        lista (list): lista donde obtendremos todos los datos
        clave (str): campo / llave del valor que queremos almacenar

    Raises:
        ValueError: Si la lista se encuentra vacia lanzara una excepcion

    Returns:
        _type_: Retorna una lista con los elementos buscados sin repetirse
    """
    lista_nueva = []
    if len(lista) > 0:
        for dato in lista:
            lista_nueva.append(dato[clave])
        return set(lista_nueva)
    else:
        raise ValueError("Lista Vacia!!!!")

def mostrar_superheroes_por_dato(lista:list,clave:str):
    """Lista todos los superheroes que cumplan con ciertos datos

    Args:
        lista (list): Lista de superheroes
        clave (str): campo o valor del dato que queremos mostrar
    """
    lista_nueva = obtener_lista_sin_repetidos(lista,clave)
    for dato in lista_nueva:
        print(f"\n      *** {dato} ***\n")
        for heroe in lista:
            if heroe[clave] == dato:
                print(f"-{heroe['nombre']}")

#----------------------- MENU ---------------------------------------

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