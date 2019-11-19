import re

frase = 'Hoy es lunes y me suenan las tripas de no poder comer paella. Me importa un pepino lo que diga Youssef.'

# FINDALL, cantidad de veces que se repite una palabra y devuelve una lista
palabra = 'paella'

print(re.findall(palabra, frase))
print(len(re.findall(palabra, frase)))
