import itertools
# Inicio del juego

# verificarEntrada
# verificarLetraRepetida
# cargarPalabrasSecretas
# seleccionarPalabra
# verificarSiEsNumero
# destaparPalabra
# verificarLetrasOcultas


# letra, palabra_secreta, vidas
def quitar_vidas(args):
    obj = args['states'][args['last_version']]
    letra = args['letra']
    coincide = False
    letras_de_palabra = list(itertools.chain.from_iterable(obj['palabra_secreta']))

    # Buscamos si la letra coincide con alguna de la palabra oculta
    aux = [x for x in letras_de_palabra if x == letra]
    if len(aux) == 0:
        obj['vidas'] = obj['vidas'] - 1

    return obj


def verificar_si_es_numero(args):
    pass


def destapar_palabra(args):
    pass