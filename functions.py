import itertools
import random

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
# destaparPalabra
# verificarLetrasOcultas
""""
args = { 
    "states": {
        "v1": {
            "palabras_disponibles": ["fdask", "fdsfdas"],
            "palabra_secreta": "fantasma",
            "palabra_mostrada": "________",
            "letras_encontradas": ['a','b'],
            "vidas": 5,
        }
    },
    "letra": "g"
}
"""


def quitar_vidas(args):
    obj = args['states'][args['last_version']]
    letra = args['letra']
    letras_de_palabra = list(itertools.chain.from_iterable(obj['palabra_secreta']))

    # Buscamos si la letra coincide con alguna de la palabra oculta
    aux = [x for x in letras_de_palabra if x == letra]
    if len(aux) == 0:
        obj['vidas'] = obj['vidas'] - 1
    return obj


def verificar_si_es_numero(args):
    resultado = True
    try:
        int(args['letra'])
        resultado = True
    except:
        resultado = False
    print('Debe ingresar una letra, no un número')
    return resultado


def cargar_palabras_secretas(args):
    obj = args['states'][args['last_version']]
    lista = []
    lista.append("jacuzzi")
    lista.append("helicoptero")
    lista.append("tornado")
    lista.append("cerveza")
    lista.append("maestro")
    lista.append("destornillador")
    lista.append("farmaceutico")
    lista.append("medioambiente")
    obj['palabras_disponibles'] = lista
    return obj


def verificar_letra_repetida(args):
    obj = args['states'][args['last_version']]
    letra = args['letra']
    letras_de_palabra = list(itertools.chain.from_iterable(obj['palabra_secreta']))
    if len(obj['letras_encontradas']) > 0:
        aux = [x for x in letras_de_palabra if x == letra]

        if len(aux) > 0:
            print('Usted ya ingresó esta letra\n')
        else:
            obj['letras_encontradas'].append(args['letra'])
            quitar_vidas(args)
    else:
        obj['letras_encontradas'].append(args['letra'])
        quitar_vidas(args)

def seleccionar_palabra(args):
    obj = args['states'][args['last_version']]
    n = len(obj['palabras_disponibles'])
    rand = random.randint(1, n - 1)
    palabra_secreta_seleccionada = obj['palabras_disponibles'][rand]
    obj['palabra_secreta'] = palabra_secreta_seleccionada
    return obj