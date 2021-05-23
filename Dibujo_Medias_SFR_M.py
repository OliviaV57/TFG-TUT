import numpy as np
import matplotlib.pyplot as plt
import os.path
import Style
import sys

zsims = ['0.142', '3.61', '4.038', '5.017']
simnom = ['SAGE']
cm = plt.get_cmap('tab10')  # Colour map to draw colours from
path2sim = 'C:/Users/Olivia/TFG-TUT/'

Mass_lista = []
SFR_M_lista = []
num_lista = []

for iiz, zsim in enumerate(zsims):
    for sim in simnom:
        ffsimav = path2sim + 'Datos_simulaciones/Medias_SFR_M_' + zsim + '.csv'
        ff10 = path2sim + 'Datos_simulaciones/Mass_SFR_10_z_' + zsim + '.csv'
        ffmax = path2sim + 'Datos_simulaciones/Mass_SFR_corte_z_' + zsim + '.csv'

        if not os.path.isfile(ffsimav):
            continue

        if not os.path.isfile(ff10):
            continue

        if not os.path.isfile(ffmax):
            continue

        '''Definimos colores'''
        cols = []
        col = cm(1. * iiz / len(zsims))
        cols.append(col)

        # print(cols,col)

        '''Leemos Medias'''
        ghist = np.loadtxt(ffsimav, skiprows=1, usecols=(0), unpack=True, delimiter=',')
        avSFR = np.loadtxt(ffsimav, skiprows=1, usecols=(1), unpack=True, delimiter=',')
        ErrorSFR = np.loadtxt(ffsimav, skiprows=1, usecols=(2), unpack=True, delimiter=',')
        ngal = np.loadtxt(ffsimav, skiprows=1, usecols=(3), unpack=True, delimiter=',')

        '''Leemos el 10% '''
        Mass10 = np.loadtxt(ff10, skiprows=1, usecols=(1), unpack=True, delimiter=',')
        StarFR10 = np.loadtxt(ff10, skiprows=1, usecols=(2), unpack=True, delimiter=',')
        SFR10 = StarFR10 - 9  # Msun h^-1 yr^-1
        SFRM10 = SFR10/Mass10 #yr^-1

        '''Leemos el corte con las más masivas'''
        MassCorte = np.loadtxt(ffmax, skiprows=1, usecols=(1), unpack=True, delimiter=',')
        StarFRCorte = np.loadtxt(ffmax, skiprows=1, usecols=(2), unpack=True, delimiter=',')
        SFRCorte = StarFRCorte - 9  # Msun h^-1 yr^-1
        SFRMCorte = SFRCorte / MassCorte  # yr^-1


        ind = np.where(ngal > 10)

        plt.style.use(Style.style1)

        plt.plot(Mass10, SFRM10, marker='.', linewidth=0, color='steelblue', label='10$\%$ SAGE z = ' + zsims[iiz] + '')
        plt.plot(MassCorte, SFRMCorte, marker='*', linewidth=0, color='r', label='Corte SAGE z = ' + zsims[iiz] + '')
        plt.plot(ghist[ind], avSFR[ind], marker='^', linewidth=0, color='k', label='Media SAGE z = ' + zsims[iiz] + '')
        plt.errorbar(ghist[ind], avSFR[ind], yerr=ErrorSFR[ind], xerr=None, fmt='.k')
        plt.ylabel('log$_{10} \;$ (SFR/M [$yr^{-1}$])')
        plt.xlabel('log$_{10} \;$(M $\; [M_{\odot} \; h^{-1} $])')
        # plt.title('Media de la función SFR SAGE frente bines de masa de las galaxias')
        # plt.xlim(8.5, 12)
        plt.ylim(-0.5,0.3)
        plotnom = path2sim + 'Figuras/Definitivas/avSFR_M_vs_Mass_Sage_10_z_' + zsims[iiz] + '.png'
        plt.legend()
        plt.savefig(plotnom)
        plt.show()
