'''

Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8,
y muestre por pantalla el menor y el mayor de los precios.

'''

precios = [50, 75, 46, 22, 80, 6, 8]

#precios.sort()

mayor_menor = sorted(precios, reverse=True)
print(mayor_menor)

precios.sort(reverse=True)
print(precios)




