import itertools

versions = ['v1.0']
states = {
    "v1": {
        "palabras_disponibles": ["Perro", "Botella", "Fideo"],
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


# Inicio del juego

# verificarEntrada
# verificarLetraRepetida
# cargarPalabrasSecretas
# seleccionarPalabra
# verificarSiEsNumero
# destaparPalabra
# verificarLetrasOcultas

def quitar_vidas(letra, palabra_secreta, vidas):
    pass
    # coincide = False
    # letras_de_palabra = palabra_secreta.toCharArray()
