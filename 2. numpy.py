import numpy as np

#arreglos unidimensionales
lista=[1,2,3,4,5]
a=np.array(lista)
print(a)
print(a.dtype)

a_complejo=np.array(lista,dtype=complex)
print(a_complejo)

# crea un arreglo unidimensional de numeros pares 2,4,6,8,10
# para ello basarse en en el array a
#prueba utilizar dtype en el nuevo arreglo

#Arreglos multidimensionales
c=np.array([[0,1,2],[3,4,5]])
# print(c)
# print(f'dimension {c.ndim}')
# print(f'tamanio {c.shape}')

# crea un arreglo multidimensionales que tenga los valores de c dividos a la mitad

# Navegar por los valores de numpy
arreglo=np.arange(56)
# print(arreglo)
matriz=arreglo.reshape((8,7))
print(matriz)

print(matriz[0,3:5])
print(matriz[6:,5:])
print(matriz[:,2])
print(matriz[2::2,::2])

# selecciona la ultima fila

