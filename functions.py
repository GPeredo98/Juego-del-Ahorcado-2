import copy
import itertools
import random
import re


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
obj = {}


def quitar_vidas(args):
    obj = args['states'][args['last_version']]
    letra = args['letra']
    letras_de_palabra = list(itertools.chain.from_iterable(obj['palabra_secreta']))

    # Buscamos si la letra coincide con alguna de la palabra oculta
    aux = [x for x in letras_de_palabra if x == letra]
    if len(aux) == 0:
        obj['vidas'] = obj['vidas'] - 1
    return obj


def verificar_si_es_numero(letra):
    resultado = True
    try:
        int(letra)
        resultado = True
    except:
        resultado = False
    return resultado


def verificar_letra_repetida(args):
    obj = args['states'][args['last_version']]
    letra = args['letra']
    # letras_de_palabra = list(itertools.chain.from_iterable(obj['palabra_secreta']))
    letras_de_palabra = obj['letras_encontradas']
    if len(obj['letras_encontradas']) > 0:
        aux = [x for x in letras_de_palabra if x == letra]

        if len(aux) > 0:
            print('Usted ya ingresó esta letra')

        else:
            copy.deepcopy(obj['letras_encontradas'].append(args['letra']))
            quitar_vidas(args)
    else:
        copy.deepcopy(obj['letras_encontradas'].append(args['letra']))
        quitar_vidas(args)


def seleccionar_palabra(args):
    obj = args['states'][args['last_version']]
    n = len(obj['palabras_disponibles'])
    rand = random.randint(1, n - 1)
    palabra_secreta_seleccionada = obj['palabras_disponibles'][rand]

    # Update the version and the state
    actual_version = 'v' + str(round(float(args['versions'][-1].replace('v', '')) + 1, 1))
    versions = args['versions'] + [actual_version]
    new_states = copy.deepcopy(args['states'])
    obj['palabra_secreta'] = palabra_secreta_seleccionada
    palabra_mostrada = re.sub(r'[^.]', "_", palabra_secreta_seleccionada)
    palabra_mostrada = palabra_mostrada.replace("", " ")
    obj['palabra_mostrada'] = palabra_mostrada
    new_states[actual_version] = obj
    args['states'] = copy.deepcopy(new_states)
    # Return the updated objects
    return versions, args['states']


def mostrar_palabra_mostrada(args):
    obj = args['states'][args['last_version']]
    while obj['vidas'] != 0:
        print('\n')
        print('Adivina la palabra secreta')
        print('Vidas: ' + str(obj['vidas']))
        print('Letras: ' + str(obj['letras_encontradas']))
        print(obj['palabra_mostrada'])

        letra = input('Ingresa la letra -> \n').lower()
        letra_valida = get_action(verificar_entrada, {
            'letra': letra
        })
        if letra == letra_valida:
            get_action(verificar_letra_repetida, {
                'states': args['states'],
                'last_version': args['last_version'],
                'letra': letra
            })
        get_action(destapar_palabra, {
                'states': args['states'],
                'last_version': args['last_version'],
                'versions': args['versions'],
                'letra': letra
            })

        aux = {
            'states': args['states'],
            'last_version': args['last_version'],
            'versions': args['versions'],
            'letra': letra
        }
        if not verificar_letras_ocultas(aux):
            print(obj['palabra_mostrada'])
            print("¡GANASTE!")
            break

    print("FIN DEL JUEGO")


def destapar_palabra(args):
    obj = args['states'][args['last_version']]
    palabra_mostrada = obj['palabra_secreta']
    letras = ''.join(obj['letras_encontradas'])

    # Usando REGEX tapamos las letras de la palabra, sin incluir las letras ya tomadas
    palabra_mostrada = re.sub(r'[^.' + letras + ']', "_", palabra_mostrada)

    actual_version = 'v' + str(round(float(args['versions'][-1].replace('v', '')) + 1, 1))
    versions = args['versions'] + [actual_version]
    new_states = copy.deepcopy(args['states'])

    palabra_mostrada = palabra_mostrada.replace("", " ")
    obj['palabra_mostrada'] = palabra_mostrada

    new_states[actual_version] = obj
    args['states'] = copy.deepcopy(new_states)
    return args['states']


def verificar_entrada(args):
    valido = True
    if len(args['letra']) > 1:
        print('Debe ingresar solo una letra\n')
        valido = False

    if len(args['letra']) < -1:
        print('Debe ingresar por lo menos una letra\n')
        valido = False

    if verificar_si_es_numero(args['letra']):
        print('Debe ingresar una letra, no un número\n')
        valido = False

    if valido:
        return args['letra']
    else:
        letra = input("Ingrese una letra:\n")
        args['letra'] = letra
        verificar_entrada(args)


def verificar_letras_ocultas(args):
    obj = args['states'][args['last_version']]

    letras_de_palabra = list(itertools.chain.from_iterable(obj['palabra_mostrada']))

    # Buscamos si la letra coincide con alguna de la palabra oculta
    aux = [x for x in letras_de_palabra if x == '_']
    if len(aux) > 0:
        return True
    else:
        return False
