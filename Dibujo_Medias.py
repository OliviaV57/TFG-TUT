import numpy as np
import matplotlib.pyplot as plt
import os.path
import sys

zsims = ['0.142', '0.523', '1.077', '2.235', '3.61', '4.038','5.017']
simnom = ['SAGE']
cm = plt.get_cmap('tab10') # Colour map to draw colours from
path2sim = 'C:/Users/Olivia/TFG-TUT/'

for iiz, zsim in enumerate(zsims):
    for sim in simnom:
        ffsim = path2sim + 'Datos_simulaciones/Medias_' + zsim + '.csv'

        if not os.path.isfile(ffsim):
            continue
        '''Definimos colores'''
        cols = []
        col = cm(1. * iiz / len(zsims))
        cols.append(col)

        #print(cols,col)

        ghist = np.loadtxt(ffsim, skiprows=1, usecols=(0), unpack=True, delimiter=',')
        avSFR = np.loadtxt(ffsim, skiprows=1, usecols=(1), unpack=True, delimiter=',')
        ErrorSFR = np.loadtxt(ffsim, skiprows=1, usecols=(2), unpack=True, delimiter=',')


        plt.plot(ghist, avSFR, marker='.', linewidth=0, color='k', label='SAGE z = ' + zsims[iiz] + '')
        plt.errorbar(ghist, avSFR, yerr=ErrorSFR, xerr=None, fmt='.k')
        plt.ylabel('log$_{10} \;$ (SFR $[M_{\odot} \; h^{-1}\; yr^{-1}$])')
        plt.xlabel('log$_{10} \;$(M$_{\odot} \; [M_{\odot} \; h^{-1} $])')
        #plt.title('Media de la función SFR SAGE frente bines de masa de las galaxias')
        # plt.xlim(8.5, 12)
        plt.ylim(8,12)
        plotnom = path2sim + 'Figuras/Definitivas/avSFR_vs_Mass_Sage_z_' + zsims[iiz] + '.png'
        plt.legend()
        plt.savefig(plotnom)
        plt.show()
