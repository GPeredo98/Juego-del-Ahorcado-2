from functions import *

versions = ['v1.0']
states = {
    "v1.0": {
        "palabras_disponibles": ["perro", "botella", "fideo", "zapato", "messi"],
        "palabra_secreta": None,
        "palabra_mostrada": None,
        "letras_encontradas": [],
        "vidas": 5
    }
}



def opcion_agregar_palabra():
    print('aqui llamar al metodo de functions')
    pass


def opcion_jugar():
    new_versions, new_states = get_action(seleccionar_palabra, {
        'states': states,
        'versions': versions,
        'last_version': get_action(get_last_version, {'versions': versions})
    })
    vivo = get_action(mostrar_palabra_mostrada, {
        'states': new_states,
        'versions': new_versions,
        'last_version': get_action(get_last_version, {'versions': new_versions})
    })
    if vivo:
        mostar_menu()


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
