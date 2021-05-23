import numpy as np
import matplotlib.pyplot as plt
import os.path
import Style
import sys

zsims = ['0.142', '3.61']
simnom = ['SAGE']
cm = plt.get_cmap('tab10') # Colour map to draw colours from
path2sim = 'C:/Users/Olivia/TFG-TUT/'

Mass_lista = []
SFR_lista = []
num_lista = []

for iiz, zsim in enumerate(zsims):
    for sim in simnom:
        ffsimav = path2sim + 'Datos_simulaciones/Medias_' + zsim + '.csv'
        ffsimtot = 'C:/Users/Olivia/TFG-TUT/Datos_simulaciones/Mass_SFR_SAGE_z_' + zsims[iiz] + '.csv'

        if not os.path.isfile(ffsimav):
            continue

        if not os.path.isfile(ffsimtot):
            continue

        '''Definimos colores'''
        cols = []
        col = cm(1. * iiz / len(zsims))
        cols.append(col)

        #print(cols,col)

        '''Leemos Medias'''
        ghist = np.loadtxt(ffsimav, skiprows=1, usecols=(0), unpack=True, delimiter=',')
        avSFR = np.loadtxt(ffsimav, skiprows=1, usecols=(1), unpack=True, delimiter=',')
        ErrorSFR = np.loadtxt(ffsimav, skiprows=1, usecols=(2), unpack=True, delimiter=',')
        ngal = np.loadtxt(ffsimav, skiprows=1, usecols=(3), unpack=True, delimiter=',')

        '''Leemos el total linea a linea'''
        ff = open(ffsimtot, 'r')
        iline = -1  # Para que en el bucle empiece en el 0
        for line in ff:
            iline += 1  # Cuenta las lineas que ya hay en el fichero. Quizá no haría falta ya que el fichero ya las tiene
            # contadas, preguntar a Violeta qué es más eficiente.
            char1 = line[0]  # Primer caracter de la linea 1.
            if not char1.isdigit(): continue  # (para saltar header)

            onlylines = iline % 10
            if onlylines != 0:
                continue

            data = np.array(line.split(','),
                            dtype=float)  # Así ya va a ser float, data[0] = columna que cuenta, data[1] = masas, data[2] = SFR

            num = data[0]
            SFR = data[2] - 9 #Msun yr^-1 h^-1
            Mass = data[1]

            Mass_lista.append(Mass)
            SFR_lista.append(SFR)
            num_lista.append(num)

        ff.close()


        ind = np.where(ngal > 10)

        plt.style.use(Style.style1)
        plt.plot(Mass_lista, SFR_lista, '.', label='Total SAGE z = ' + zsims[iiz] + '')
        plt.plot(ghist[ind], avSFR[ind], marker='^', linewidth=0, color='k', label='Media SAGE z = ' + zsims[iiz] + '')
        plt.errorbar(ghist[ind], avSFR[ind], yerr=ErrorSFR[ind], xerr=None, fmt='.k')
        plt.ylabel('log$_{10} \;$ (SFR $[M_{\odot} \; h^{-1}\; yr^{-1}$])')
        plt.xlabel('log$_{10} \;$(M$ \; [M_{\odot} \; h^{-1} $])')
        #plt.title('Media de la función SFR SAGE frente bines de masa de las galaxias')
        plt.xlim(8.5, 12)
        #plt.ylim(-2.5,3)
        plotnom = path2sim + 'Figuras/Definitivas/avSFR_vs_Mass_Sage_z_' + zsims[iiz] + '.png'
        plt.legend()
        plt.savefig(plotnom)

        plt.show()
