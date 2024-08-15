#funcion imprimir saludo
def saludo():
    print("hola mundo")

saludo()

#funcion factorial usando la libreria math
#factorial de 5
#math.factorial

#raiz cuadra de 33
#math.sqrt

#usemos dentro de una funcion math.factorial

#funcion combinacion
#formula de combinancion es n!=k!*(n-k)!


#ejemplo de combinacion
n=10
k=3
#print(f'Combinaciones de {n} elementos tomados de {k} en k:{combinaciones(n,k)}')

#sintaxis de funciones
import pandas as pd
import numpy as np

def generar_archivo_txt(lista,nombre):
    nombreArchivo=nombre+".csv"
    nuevoDf=pd.DataFrame(lista)
    nuevoDf.to_csv(nombreArchivo,encoding='utf-8')
    return nombreArchivo

#generar matriz de forma automatica
#importar numpy
#usar random.randint
#opcional:parametros con valores por defecto

#print(generar_archivo_txt([[1,2,3],[4,5,6],[7,8,9]],'lista'))
# print(generar_archivo_txt(generar_matriz(3,3),'aleatorios'))

#funcion recursiva de ejemplo
def Factorial(numero):
    if(numero==0):
        return 1
    total=numero*Factorial(numero-1)
    return total

#print(Factorial(5))

# suma recursiva
# suma todos los numeros del 1 al 9 usando funcion suma_recursiva
numeros=[1,2,3,4,5,6,7,8,9]


#print(suma_recursivo(numeros))