import numpy as np
import matplotlib.pyplot as plt
import os.path
import statistics as stats
import sys


'''Arrays para automatizarlo'''
zsims = ['0.142', '3.61']
simnom = ['SAGE']
cm = plt.get_cmap('tab10') # Colour map to draw colours from

'''True o False si estoy haciendo un test o el programa entero'''
test = False

'''Hago los bines de masa'''

# Cortes de las masas, la masa mínima y la masa máxima que voy a usar:
gmin = 8.5
gmax = 13

# intervalo:
dex = 0.2
# límites de los intervalos y punto del medio:
gedges = np.array(np.arange(gmin, gmax + dex, dex))  # Desde gmin hasta gmax+dex sumando dex cada vez.

ghist = gedges[1:] - 0.5 * dex  # centros de los intervalos, que es lo que nos interesa



for iiz, zsim in enumerate(zsims):

    '''Leemos el archivo'''
    ffsim = 'C:/Users/Olivia/TFG-TUT/Datos_simulaciones/Mass_SFR_SAGE_z_'+zsims[iiz]+'.csv'

    if not os.path.isfile(ffsim):
        continue
    # print(ffsim)
    # dataSim = np.loadtxt(ffsim, dtype=str, unpack=True)  # dtype str para poder leer palabras también.
    # f = open(ffsim, 'r') #'r': python read file.

    '''Definimos lista de colores'''
    cols = []
    col = cm(1. * iiz / len(zsims))
    cols.append(col)

    '''inicializamos contadores'''
    sumasfr= np.zeros(shape=len(ghist)) #SFR acumulativa
    ngal= np.zeros(shape=len(ghist)) #numero de galaxias
    medias = np.zeros(shape=len(ghist)) #media(sumasfr/ngal)

    '''Empezamos a leer linea a linea'''
    ff = open(ffsim, 'r')
    iline = -1 #Para que en el bucle empiece en el 0

    for line in ff:
        iline += 1 #Cuenta las lineas que ya hay en el fichero. Quizá no haría falta ya que el fichero ya las tiene
                    # contadas, preguntar a Violeta qué es más eficiente.
        char1 = line[0] #Primer caracter de la linea 1.

        if not char1.isdigit(): continue  # (para saltar header)

        if test and iline>1000000000:
            exit()

        onlylines = iline % 10
        if onlylines != 0:
            continue

        data = np.array(line.split(','), dtype=float) #Así ya va a ser float, data[0] = columna que cuenta, data[1] = masas, data[2] = SFR

        SFR = data[2]
        Mass = data[1]

        #loop por los bines las masas hasta el penultimo edge
        for ie, edge in enumerate(gedges[:-1]):
            #print(ie,gedges[ie],gedges[ie+1])
            #print (Mass)
            if Mass >= gedges[ie] and Mass<gedges[ie+1]:
                sumasfr[ie] = sumasfr[ie] + SFR
                ngal[ie] = ngal[ie] + 1
                #print(ie, sumasfr[ie],ngal[ie])

    for ie, edge in enumerate(gedges[:-1]):
        medias[ie] = sumasfr[ie]/ngal[ie]
        print(ie, medias[ie])
        #Incluir error de la media.








