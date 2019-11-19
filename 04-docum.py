import math
import doctest

def raizcuadrada(listaNumeros):
    """
        La función devuele una lista con la raiz cuadrada de los elementos númericos pasados por el parámetro en formato lista.

    >>> lista = [4,9,16]
    >>> raizcuadrada(lista)
    [2.0, 3.0, 4.0]

    >>> lista = [45,23,12]
    >>> raizcuadrada(lista)
    [6.708203932499369, 4.795831523312719, 3.4641016151377544]


    >>> lista = []
    >>> for i in [4, 9 , 16]:
    ...     lista.append(i)
    >>> raizcuadrada(lista)
    [2.0, 3.0, 4.0]

    """

    return [math.sqrt(n) for n in listaNumeros]

# imprimir pruebas
doctest.testmod()