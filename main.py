from functions import *

versions = []
states = {
    "v1": {
            "palabras_disponibles": ["fdask", "fdsfdas"],
            "palabra_secreta": None,
            "palabra_mostrada": None,
            "letras_encontradas": ['a','b'],
            "vidas": 5
        }
}

"""
states {
    "v1": {
        "palabras_disponibles": ["fdask", "fdsfdas"],
        "palabra_secreta": None,
        "palabra_mostrada": None,
        "letras_encontradas": ['a','b'],
        "vidas": 5
    }
}
"""


def get_action(function, args):
    """ Funcion contenedora
    """
    return function(args)


def get_last_version(args):
    """ Obtiene la ultima version de los estados
    """
    if args['versions'].__len__() == 0:
        return args['versions']
    return args['versions'][-1]


def agregar_palabra():
    print('fdsfa')
    pass


def elegir_palabra():
    pass


def ver_palabras():
    pass


def mostar_menu():
    print('===== MENU =====')
    print('1 Agregar palabra')
    print('2 Elegir palabra')
    print('4 Salir')
    opcion = input("-> ")
    ejecutar_opcion(int(opcion))


def ejecutar_opcion(opcion):
    if opcion == 1:
        agregar_palabra()
    elif opcion == 2:
        elegir_palabra()
    elif opcion == 3:
        ver_palabras()
    else:
        exit()


if __name__ == "__main__":
    mostar_menu()
