'''
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas
y muestre por pantalla su producto escalar.

'''

# producto escalar es una operación algebraica que toma dos vectores y retorna un escalar en grados

u = [1, 2, 3]
v = [-1, 0, 2]
grados = 0
for k in range(len(u)):
    grados += u[k]*v[k]

print(f'El producto escalar en grados es {grados}º')
