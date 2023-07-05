palabra = input('Introduce una palabra: ')
palabra_inversa = palabra[::-1]

igual = 0
fin = 0

for item in reversed(range(len(palabra))):

    print(palabra_inversa[item] + "\t" + palabra[fin])

    if palabra_inversa[item].lower() == palabra[fin].lower():
        igual += 1
    fin += 1


if len(palabra) == igual:
    print(f'La palabra {palabra} es palindroma')
else:
    print(f'La palabra {palabra} no es palindroma')





