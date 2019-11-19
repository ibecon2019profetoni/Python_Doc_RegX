import re
# normalizar (limpiar) la frase de tildes
from unicodedata import normalize


frase = 'Hoy es lunes y me suenan las tripas, el lunes no puedo comer paella y quiero irme en un camión. El sábado también me sonaban las tripas y tuve que recurrir a una niñera, para no asesinar a mis hijos, que no tengo.'


# frase = normalize('NFKD', frase).encode('ascii','ignore').decode('ascii')

# FINDALL
palabra = 'sabado'

print(re.findall(palabra,frase))

# si tenemps ñ, se pierden, como evitarlo
eñe = frase.replace('ñ','#').replace('Ñ','$')
frase = normalize('NFKD',eñe)\
        .encode('ascii','ignore').decode('ascii')\
        .replace('#','ñ').replace('$','Ñ')

print(frase)

a,b = 'áéíóúàèìòùü','aeiouaeiouu'
tranformar = str.maketrans(a,b)
print(frase.translate(tranformar))

