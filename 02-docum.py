"""
    Pruebas con la documentación
    ----------------------------
    Saber que lo que programas funciona adecuadamente antes de lanzarlo a producción ó antes de arrancarlo
"""

def areaTriangulo(base, altura):
    """
        Calcula el área de un triángulo, muy, pero muy bien.

        >>> areaTriangulo(3,3)
        'El área del triángulo es: 4.5'

        >>> areaTriangulo(1,3)
        'El área del triángulo es: 1.5'

    """
    return 'El área del triángulo es: ' + str((base * altura) / 2)

import doctest
doctest.testmod()