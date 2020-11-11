from functions import *


def opcion_agregar_palabra():
    print('aqui llamar al metodo de functions')
    pass


def opcion_elegir_palabra():
    print('aqui llamar al metodo de functions')
    pass


def mostar_menu():
    print('===== MENU =====')
    print('1 Agregar palabra')
    print('2 Elegir palabra')
    print('3 Salir')
    opcion = input("-> ")
    ejecutar_opcion(int(opcion))


def ejecutar_opcion(opcion):
    if opcion == 1:
        opcion_agregar_palabra()
    elif opcion == 2:
        opcion_elegir_palabra()
    else:
        exit()


if __name__ == "__main__":
    mostar_menu()
