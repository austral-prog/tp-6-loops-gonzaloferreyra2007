# Replace the "ANSWER HERE" for your answer

def put(value, lst):
    """
    Coloca value en el primer lugar vacio ("") que encuentre en lst
    y retorna el indice donde lo coloco.
    Si no hay ningun lugar vacio, retorna -1.
    IMPORTANTE: esta funcion modifica la lista original.

    Ejemplo:
        colors = ["Red", "", "Green"]
        put("Blue", colors) -> 1
        # colors ahora es ["Red", "Blue", "Green"]
    """
    for i in range(len(lst)):
        # Si encontramos un espacio vacío
        if lst[i] == "":
            # Modificamos la lista original directamente
            lst[i] = value
            # Retorno temprano: ya cumplimos la tarea
            return i
            
    # Si recorrimos toda la lista y no hubo un "", devolvemos -1
    return -1


def remove(value, lst):
    """
    Busca todas las ocurrencias de value en lst, las reemplaza por ""
    y retorna la cantidad de eliminaciones realizadas.
    IMPORTANTE: esta funcion modifica la lista original.

    Ejemplo:
        colors = ["Red", "Green", "Red", "Blue"]
        remove("Red", colors) -> 2
        # colors ahora es ["", "Green", "", "Blue"]
    """
    eliminaciones = 0
    
    for i in range(len(lst)):
        # Si el elemento actual es el que queremos borrar
        if lst[i] == value:
            # Reemplazamos por un string vacío
            lst[i] = ""
            # Aumentamos nuestro contador
            eliminaciones = eliminaciones + 1
            
    return eliminaciones
