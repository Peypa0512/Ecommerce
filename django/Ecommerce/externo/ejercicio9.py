'''
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
'''

palabra = input('Por favor introduce una palabra' )
a = 0
e = 0
i = 0
o = 0
u = 0
for vocal in range(len(palabra)):

    if palabra[vocal].lower() == 'a':
        a += 1
    elif palabra[vocal].lower() == 'e':
        e += 1
    elif palabra[vocal].lower() == 'i':
        i += 1
    elif palabra[vocal].lower() == 'o':
        o += 1
    elif palabra[vocal].lower() == 'u':
        u += 1

print(f'En la palabra {palabra}, contiene {a} "a", {e} "e", {i} "i", {o} "o" y {u} "u"')
