import numpy as np
import matplotlib.pyplot as plt
import os.path
import sys


'''Arrays para automatizarlo'''
zsims = ['0.142', '3.61']
simnom = ['SAGE']
cm = plt.get_cmap('tab10') # Colour map to draw colours from
Mass_lista = []
SFR_lista = []
num_lista = []

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

    '''Empezamos a leer linea a linea'''
    ff = open(ffsim, 'r')
    iline = -1 #Para que en el bucle empiece en el 0
    for line in ff:
        iline += 1 #Cuenta las lineas que ya hay en el fichero. Quizá no haría falta ya que el fichero ya las tiene
                    # contadas, preguntar a Violeta qué es más eficiente.
        char1 = line[0] #Primer caracter de la linea 1.
        if not char1.isdigit(): continue  # (para saltar header)

        onlylines = iline % 10
        if onlylines != 0:
            continue

        data = np.array(line.split(','), dtype=float) #Así ya va a ser float, data[0] = columna que cuenta, data[1] = masas, data[2] = SFR

        num= data[0]
        SFR = data[2]
        Mass = data[1]

        Mass_lista.append(Mass)
        SFR_lista.append(SFR)
        num_lista.append(num)

    ff.close()


    plt.plot(Mass_lista, SFR_lista, '.', color=col, label='SAGE z = ' + zsims[
        iiz] + '')  # Aparece todas las veces la leyenda, me gustaría que solo apareciera una vez por redshift
    plt.ylabel('$Log_{10} \; $(SFR $[M_{\odot} \; h^{-1}\; yr^{-1}$])')
    plt.xlabel('$Log_{10} \; (Masa \; [M_{\odot} \; h^{-1} $])')
    plt.title('Función SFR SAGE frente Masa de las galaxias')
    plt.xlim(8.5, 12.5)
    plt.legend()
    plotnom = 'C:/Users/Olivia/TFG-TUT/Figuras/SFR_vs_Mass_Sage_z_' + zsims[iiz] + '.png'
    # print(plotnom)
    plt.savefig(plotnom)

    plt.show()
