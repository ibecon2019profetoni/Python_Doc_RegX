import doctest


def pruEmail(mail):
    """
        Esta función prueba si tu email es válido.
        Si tiene un @ en su lugar central, esta perfecto.
        Si el @ esta al inicio del string o al final del string, esta mal.
        Si no existe @, esta mal.

    >>> pruEmail('pepe@ibecon.es')
    True

    >>> pruEmail('@pepeibecon.es')
    False

    >>> pruEmail('pepeibecon.es@')
    False

    >>> pruEmail('pepeibecon.es')
    False

    """

    mail_usuario = mail.count('@')

    if mail_usuario != 1 or mail.rfind('@') == len(mail)-1 or mail.find('@') == 0:
        return False
    else:
        return True


# imprimir pruebas
doctest.testmod()
