import numpy as np
import matplotlib.pyplot as plt
import os.path
import Style
import sys

zsims = ['3.61', '4.038','5.017']
simnom = ['SAGE']
cm = plt.get_cmap('tab10') # Colour map to draw colours from
path2sim = 'C:/Users/Olivia/TFG-TUT/'

for iiz, zsim in enumerate(zsims):
    for sim in simnom:
        ffav = path2sim + 'Datos_simulaciones/Medias_' + zsim + '.csv'
        ffcorte = path2sim + 'Datos_simulaciones/Mass_SFR_corte_z_' + zsim + '.csv'
        ff10 = path2sim + 'Datos_simulaciones/Mass_SFR_10_z_' + zsim + '.csv'

        if not os.path.isfile(ffav):
            continue

        if not os.path.isfile(ffcorte):
            continue

        if not os.path.isfile(ff10):
            continue


        '''Definimos colores'''
        cols = []
        col = cm(1. * iiz / len(zsims))
        cols.append(col)

        #print(cols,col)

        '''MEDIAS'''

        ghist = np.loadtxt(ffav, skiprows=1, usecols=(0), unpack=True, delimiter=',')
        avSFR = np.loadtxt(ffav, skiprows=1, usecols=(1), unpack=True, delimiter=',') #Msun h^-1 yr^-1
        ErrorMass = np.loadtxt(ffav, skiprows=1, usecols=(2), unpack=True, delimiter=',')

        '''CORTE'''
        MassCorte = np.loadtxt(ffcorte, skiprows=1, usecols=(1), unpack=True, delimiter=',')
        StarFRCorte = np.loadtxt(ffcorte, skiprows=1, usecols=(2), unpack=True, delimiter=',')
        SFRCorte = StarFRCorte - 9 #Msun h^-1 yr^-1

        '''10 PORCIENTO'''
        Mass10 = np.loadtxt(ff10, skiprows=1, usecols=(1), unpack=True, delimiter=',')
        StarFR10 = np.loadtxt(ff10, skiprows=1, usecols=(2), unpack=True, delimiter=',')
        SFR10 = StarFR10 - 9  # Msun h^-1 yr^-1

        indav = np.where(avSFR>0)
        #indcorte = np.where(StarFR>0)

        plt.style.use(Style.style1)
        plt.plot(Mass10, SFR10, marker='.', color = 'steelblue', linewidth=0, label='10$\%$ SAGE z = ' + zsims[iiz] + '')
        plt.plot(MassCorte, SFRCorte, marker='*', color = 'r', linewidth=0, label='corte SAGE z = ' + zsims[iiz] + '')
        plt.plot(ghist[indav], avSFR[indav], marker='^', linewidth=0, color='k', label='SAGE z = ' + zsims[iiz] + '')
        plt.errorbar(ghist[indav], avSFR[indav], yerr=ErrorMass[indav], xerr=None, fmt='.k')
        plt.ylabel('log$_{10} \;$ (SFR $[M_{\odot} \; h^{-1}\; yr^{-1}$])')
        plt.xlabel('log$_{10} \;$(M$ \; [M_{\odot} \; h^{-1} $])')
        #plt.title('Media de la función SFR SAGE frente bines de masa de las galaxias')
        #plt.xlim(8.4, 11.6)
        plt.ylim(-2.5,3)
        plotnom = path2sim + 'Figuras/Definitivas/Medias_corte_10_z_' + zsims[iiz] + '.png'
        plt.legend()
        plt.savefig(plotnom)
        plt.show()
