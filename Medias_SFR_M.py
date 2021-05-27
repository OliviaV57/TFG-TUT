import numpy as np
import matplotlib.pyplot as plt
import os.path
import sys

path2sim = 'C:/Users/Olivia/TFG-TUT/Datos_simulaciones/'
# path2sim = '/home/violeta/teaching/olivia/'

'''Arrays para automatizarlo'''
zsims = ['0', '0.142', '3.61', '4.038', '5.017']
simnom = ['SAGE']
cm = plt.get_cmap('tab10')  # Colour map to draw colours from

'''True o False si estoy haciendo un test o el programa entero'''
test = False
ntest = 1000

'''Hago los bines de masa'''

# Cortes de las masas, la masa mínima y la masa máxima que voy a usar:
gmin = 8.5
gmax = 12.3

# intervalo:
dex = 0.2
# límites de los intervalos y punto del medio:
gedges = np.array(np.arange(gmin, gmax + dex, dex))  # Desde gmin hasta gmax+dex sumando dex cada vez.

ghist = gedges[1:] - 0.5 * dex  # centros de los intervalos, que es lo que nos interesa
# print('Rangos en masa = {}'.format(ghist))

if test: zsims = zsims[0]

for iiz, zsim in enumerate(zsims):
    '''Leemos el archivo'''
    ffsim = path2sim + 'Mass_SFR_SAGE_z_' + zsim + '.csv'
    if test: ffsim = path2sim + 'test.csv'
    if not os.path.isfile(ffsim):
        continue

    '''Definimos lista de colores'''
    cols = []
    col = cm(1. * iiz / len(zsims))
    cols.append(col)

    '''inicializamos contadores'''
    sumasfrm = np.zeros(shape=len(ghist))  # SFR acumulativa
    ngal = np.zeros(shape=len(ghist))  # numero de galaxias
    medias = np.zeros(shape=len(ghist))  # media(sumasfr/ngal)
    errormedias = np.zeros(shape=len(ghist))  # error de la media (sig/sqrt(ngal))
    sig = np.zeros(shape=len(ghist))  # Desviación estándar sqrt((sum(sfr-medias)^2/ngal-1))

    '''Empezamos a leer linea a linea para calcular la media'''
    with open(ffsim, 'r') as ff:
        iline = -1  # Para que en el bucle empiece en el 0
        for line in ff:
            iline += 1  # Cuenta las lineas que ya hay en el fichero.
            char1 = line[0]  # Primer caracter de la linea 1.
            if not char1.isdigit(): continue  # (para saltar header)

            if test and iline > ntest: break

            data = np.array(line.split(','))
            SFR = float(data[2]) - 9  # Msun h^-1 yr ^-1 (log)
            Mass = float(data[1])  # Msun h^-1 (log)
            SFR_M = SFR/Mass #yr ^ -1 (log)

            # loop por los bines las masas hasta el penultimo edge
            for ie, edge in enumerate(gedges[:-1]):
                if Mass >= edge and Mass < gedges[ie + 1]:
                    # print(iline,ie,edge,gedges[ie + 1],Mass)
                    sumasfrm[ie] = sumasfrm[ie] + SFR_M
                    ngal[ie] = ngal[ie] + 1
                    break
    # print(ngal,sumasfr)

    # Una vez leído el fichero calculamos las MEDIAS con los números totales en cada bin. Hay que leer
    # el fichero y por eso salir del loop del fichero.
    for ie, edge in enumerate(gedges[:-1]):
        if ngal[ie] > 10:
            medias[ie] = sumasfrm[ie] / ngal[ie]
    # print(medias)

    '''Segunda lectura del fichero para calcular los errores'''

    with open(ffsim, 'r') as ff:
        iline = -1  # Para que en el bucle empiece en el 0
        for line in ff:
            iline += 1
            char1 = line[0]  # Primer caracter de la linea 1.
            if not char1.isdigit():
                continue  # (para saltar header)

            if test and iline > ntest: break

            data = np.array(line.split(','))
            SFR = float(data[2]) - 9  # Msun h^-1 yr^-1
            Mass = float(data[1])  # Msun h^-1
            SFR_M = SFR/Mass # yr ^ -1

            for ie, edge in enumerate(gedges[:-1]):
                if Mass >= edge and Mass < gedges[ie + 1]:
                    # print(iline,ie,edge,gedges[ie + 1],Mass)
                    # Addition for the numerator
                    sig[ie] = (SFR_M - medias[ie]) ** 2

                    break
    # print(sig)
    # Una vez leído el fichero calculamos los ERRORES con los números totales en cada bin. Hay que leer todo
    # el fichero y por eso salir del loop del fichero.
    for ie, edge in enumerate(gedges[:-1]):
        if ngal[ie] > 10:
            sig[ie] = (sig[ie] / ((ngal[ie] - 1) * ngal[ie])) ** .5
        else:
            sig[ie] = 0
    # print(sig)

    tofile = np.column_stack((ghist, medias, sig, ngal))
    # print(tofile)
    outfil = path2sim + 'Medias_SFR_M_' + zsim + '.csv'  # El directorio, hay que crear el excel antes
    header1 = 'bines de masa, Medias de SFR/M, errores, ngal'
    # print(medias,errormedias)
    with open(outfil, 'w') as outf:
        # outf.write(header1)
        np.savetxt(outf, tofile, delimiter=',', header=header1)
        outf.closed
    # print(outf,'Output file :{}'.format(outfil))