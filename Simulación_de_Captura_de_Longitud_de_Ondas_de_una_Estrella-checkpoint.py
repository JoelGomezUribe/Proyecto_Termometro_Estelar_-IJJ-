# Todas las librerias que seran utilizadas
from numpy import *
from random import *
import pandas as pd

# Se definen las constantes que se usan para la ecuación de Plank
k = 1.380649 * 10**(-23)
c = 299792458 
h = 6.62607015 * 10**(-34)
a = h*c/k

# Se define la ecuación de Plank
def E(y,t):
    E = (8*pi*a*k/(y**5))/(e**(a/(y*t))-1)
    return(E)

T = int(3000*random()) + 3000 # Se plante una temperatura aleatoria de 3000 a 6000 grados Kelvin
F = arange(7*10**(-9), 4*10**(-6), 10**(-9)) # Se da un rango un rango de longitudes de onda para calcular la curva de poder de emision espectral con la temperatura planteada (cubre cada nanometro hasta 4 micrometros)
I = [] # Se hace una lista donde se colocara cada valor de poder de emision espectral
for i in F: # Se calcula los poderes de emision espectral por cada valor de longitud de onda y la temperatura planteada
    I.append(E(i,T))

A = [] # Una lista para colocar 200 indices de la maxima longitud de onda a la ultima 
B = [] # Una lista para colocar 200 indices de la primera longitud de onda a la maxima 
# El proposito es que cada valor de los indices de la lista A y B que esten en la misma posición corresponda a valores cuyo poder de emision espectral sea igual (o por lo menos lo mas cercano posible)
for i in range(200): # Se hara 200 veces lo siguiente para tener 200 valores de la lista
    x = i*((max(I)-I[len(I)-1])/199)+I[len(I)-1] # Del ultimo valor de la lista de emision espectral (que seria un minimo) al maximo, se dividira en 200 y 'x' depende del valor de iteracion tendra una fraccion del valor de poder de emision espectral (el primero seria el minimo y el ultimo el maximo)
    y = 0 # Esta variable corresponde a los indices del primero al indice del maximo
    z = len(I)-1 # Esta variable corresponde a los indices del ultimo al indice del maximo
    while I[y] < x: # Aqui se encontrara el del indice cuyo valor de la lista sea el mas parecido a x
        y = y + 1 # Se ira sumando 1 para comprovar si el indice 'y' corresponde al minimo que sea mayor o igual a 'x'
    while I[z] < x: # Aqui se encontrara el del indice cuyo valor de la lista sea el mas parecido a x
        z = z - 1 # Se ira restando 1 para comprovar si el indice 'z' corresponde al minimo que sea mayor o igual a 'x'
    A.append(z) # Se agrega a la lista ya que es el indice que más se parce a 'x' despues del maximo
    B.append(y) # Se agrega a la lista ya que es el indice que más se parce a 'x' antes del maximo

Datos = [] # Esta es una lista donde se agregaran los valores de longitud de onda que corresponda a una simulacion de la medicion de la radacion del astro
# Aquí lo que se hace es simular una medición de la radiacion de una estrella, ya que las mediciones no son lo mas precisas que puede haber, los valores seran aleatorios, pero tienen que ser correspondientes con la emision de radiacion de la estrella con la temperatura planteada
for i in range(200): # Se hara esto 200 veces ya que es el tamaño de las listas A y B
    for j in range(A[i]-B[i]+1): # Como se tienen que generar valores de acuerdo a la emision, esto seran de los indices que su emsion radiactiva sea "igual", por eso asi son las listas A y B, yde cada valor se generara al menos el valor de la diferencia de los indices mas 1 
        r = 0 # Este sera el valor del indice que se genere de manera aleatoria
        r = int((A[i]-B[i])*random()) + B[i] # Se genera un valor aleatorio de el indice de la lista B al de la lista A
        Datos.append(F[r]) # Con indice que le corresponde a la lista de la longitudes de onda se colocara a la lista de datos, entonces de esta manera se colocan datos de longitud de onda de manera aleatoria pero respetando la emisión de la estrella con la temperatura planteada

DF = [] # Esta es una lista donde se colocan los datos ya obtenidos, pero mas "revueltos" para que no haya ningun orden especial en los datos obtenidos en la simulacion de la medición
while Datos != []: # Esto se hara hasta que la lista este vacia
    i = 0 # Esta variable sera el indice de la lista de datos
    i = int(len(Datos)*random()) # El indice sera de manera aleatoria del tamaño de la lista de datos
    DF.append(Datos[i]) # El valor que corresponde a este indice se agrega a la nueva lista
    Datos.pop(i) # El valor que corresponde a este indice se borrara a la lista de datos

Archivo = pd.DataFrame(DF) # Con la biblioteca pandas se agrega la lista de datos finales a un archivo .csv
Archivo.to_csv('Datos_Finales.csv')

s = open("Temperatura_Real.txt", "w") # Se hara un archivo de texto donde coloque la temperatura planteada aleatoria, para comprovar si la temperatura calculada es la correcta
s.write("Las muestras de radiación que se dan son a partir de una estrella que esta a %g grados Kelvin" % T )
s.close()