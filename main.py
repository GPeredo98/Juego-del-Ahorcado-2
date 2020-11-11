from functions import *

versions = ['v1.0']
states = {
    "v1.0": {
        "palabras_disponibles": ["perro", "botella", "fideo"],
        "palabra_secreta": None,
        "palabra_mostrada": None,
        "letras_encontradas": None,
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


def getStates():
    return states


def getVersions():
    return versions


def setStates(newStates):
    states = newStates


def setVersions(newVersions):
    versions = newVersions


def opcion_agregar_palabra():
    print('aqui llamar al metodo de functions')
    pass


def opcion_jugar():
    new_versions, new_states = get_action(seleccionar_palabra, {
        'states': states,
        'versions': versions,
        'last_version': get_action(get_last_version, {'versions': versions})
    })
    get_action(mostrar_palabra_secreta, {
        'states': new_states,
        'versions': new_versions,
        'last_version': get_action(get_last_version, {'versions': new_versions})
    })


def mostar_menu():
    print('===== MENU =====')
    print('1 Jugar')
    print('2 Agregar palabra')
    print('3 Salir')
    opcion = input("-> ")
    ejecutar_opcion(int(opcion))


def ejecutar_opcion(opcion):
    if opcion == 1:
        opcion_jugar()
    elif opcion == 2:
        opcion_agregar_palabra()
    else:
        exit()


if __name__ == "__main__":
    mostar_menu()
