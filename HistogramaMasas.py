####################################################################################################

''' PARA HACERLO CON PANDAS'''

# import pandas as pd
'''
File = pd.ExcelFile('Mass_total_Galacticus.xlsx') # Función dentro de la variable 'File' donde almacenamos el 
# archivo excel.
# print(File.sheet_names) #imprime el nombre de las hojas de excel que tenemos en nuestro archivo.

df = File.parse('Mass_total_Galacticus') # Variable que utilizando la función parse lee el contenido de la hoja
# de excel en la que estamos.
# En este caso solo hay una hoja, pero imagino que es útil para cuando hay más.
# print(df) #Imprime la hoja de la que hablamos, filas y columnas.

'''

#####################################################################

''' PARA HACERLO CON XLRD '''
# import xlrd
'''
# file = 'C:/Users/Olivia/TFG-TUT/Mass_total_Galacticus.xlsx'  # Variable donde almacenamos el archivo excel
# wb = xlrd.open_workbook(file)  # Variable que lee nuestro excel.

hoja = wb.sheet_by_index(0)  # Variable que elige la hoja en la que trabajamos, by index, ponemos el numero.
# By name el nombre, da igual lee lo mismo.

#print(hoja.nrows)  # imprime el número de filas
#print(hoja.ncols)  # imprime el número de columnas
# print(hoja.cell_value(0, 0)) #Valor de una celda en particular.

# bucle que selecciona la columna o la fila que quiero
#for i in range(1, hoja.nrows):  # rango: desde la fila 1 a todas las filas
 #   print(hoja.cell_value(i, 2))  # imprimir las filas que pedí en el rango y la columna 2 en este caso.
# NB: Python empieza a contar desde 0, 2 es mi tercera columna.
'''

##########################################################

'''PARA HACERLO CON OPENPYXL'''
import openpyxl
import math
import numpy as np

wb = openpyxl.load_workbook("Mass_total_Galacticus.xlsx") #Abre mi excel
file = wb["Mass_total_Galacticus"] # Lee la hoja que quiero que lea de mi excel. En este caso se llaman igual. Sheet 1.

Masas=[] #Creo una lista vacía que voy a ir rellenando
for row in file.iter_rows(min_row = 2): #Cojo solo la columna 2. La C en mi excel.
   m = row[2].value # Cojo los valores de la columna 2 y los meto en una variable. Identifica donde hay valores.
   logm = math.log(m) #Hago el logaritmo de cada uno de mis valores
   Masas.append(logm) #Hago de esa variable una lista y la pongo en mi lista vacía.

# print (Masas) # Me imprime mi lista de masas!!

# Ordeno mis masas:
Mass = sorted(Masas) #Variable con mis masas ordenadas de menor a mayor.
print(Mass)

#Creo un diccionario que me dice cuantos elementos hay de cada masa en mi lista:
from collections import Counter
counted = Counter(Mass)
# print(counted) #solo hay una de cada, normal. No importa, las voy a contar por intervalos.


'''hist, bin_edges = np.histogram(Mass) # Por defecto utiliza 10 bins del mismo tamaño y te devuelve un tuple (lista de
# n que componen mi organización) de las frecuencias y de los limites de los bines correspondientes. Va a haber un 
# limite de bines más que miembros de mi histograma.
print(hist)
print(bin_edges)
# print(hist.size)
# print(bin_edges.size)'''

#Se pueden hacer los limites de los bines manualmente también:

first_edge, last_edge = Mass[0], Mass[-1] #Como mi lista de masas está ordenada, cojo la primera masa como límite
# inferior y la última como límite superior. En este caso sé que la última está en el puesto 99, ya que tengo 100 masas,
# pero creo que no siempre voy a saber cuantas masas tengo, así que he puesto el índice -1, que te da el último puesto.
n_equal_bins = 10 #Los mismos que pone numpy por defecto.
bin_edges = np.linspace(start = first_edge,stop = last_edge,
                        num = n_equal_bins+1, endpoint = True)
# linspace return evenly spaced samples over a specified interval.
# Returns num evenly spaced samples calculated over the interval [start, stop]
# num = 10+1 porque queremos 10 intervalos, por lo que necesitamos 11 límites.
# The endpoint of the interval can optionally be excluded.
print(bin_edges)

'''Pequeñp cálculo de nuestro intervalo a mano:
Dif = Mass[-1]-Mass[0]
interval = Dif/10
edge2 = Mass[0] + interval
print(interval)
Con un bucle se podría hacer de esta manera también y así no utilizar linspace:
'''
Diff = Mass[-1] - Mass[0]
n = 10
interval = Diff/n
edge = Mass[0]
for ibin in range(len(Mass)):
   edge =  edge + interval




