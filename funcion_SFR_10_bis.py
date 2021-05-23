import numpy as np
import matplotlib.pyplot as plt
import os.path
import Style
import sys

path2sim = 'C:/Users/Olivia/TFG-TUT/Datos_simulaciones/'
#path2sim = '/home/violeta/teaching/olivia/'

'''Arrays para automatizarlo'''
zsims = ['3.61', '4.038','5.017']
simnom = ['SAGE']
cm = plt.get_cmap('tab10')  # Colour map to draw colours from

'''Parámetros de la simulación'''
volumen = 1000**3 #(Mpc/h)^3

'''Constantes'''
dex = 0.1
gmin = -1
gmax = 4


for iiz, zsim in enumerate(zsims):
    for iis, sim in enumerate(simnom):
        ff10 = path2sim + 'Mass_SFR_10_z_' + zsim + '.csv'
        ffall = path2sim + '/histograma_' + sim + '_z_' + zsim + '.csv'
        ffhigh = path2sim + 'Mass_SFR_corte_z_' + zsim + '.csv'



        if not os.path.isfile(ff10):
            continue

        if not os.path.isfile(ffall):
            continue

        if not os.path.isfile(ffhigh):
            continue

        cols = []
        col = cm(1. * iis / len(simnom))
        cols.append(col)

        '''Corte más masivas'''

        StarFRHigh = np.loadtxt(ffhigh, skiprows=1, usecols=(2), unpack=True, delimiter=',')
        SFRHigh = StarFRHigh - 9  # * np.log10(10) = 1 #Msun h^-1 yr^-1

        gedges = np.array(np.arange(gmin, gmax + dex, dex))  # Límites de los intervalos.
        ghist = gedges[1:] - 0.5 * dex  # centros de los intervalos.

        freqHigh, bins_edgesHigh = np.histogram(SFRHigh, bins=gedges)
        freqHigh = freqHigh / (dex * volumen)
        ftotHigh = np.log10(freqHigh, where=0 < freqHigh)

        '''10 por ciento más masivas'''
        StarFR10 = np.loadtxt(ff10, skiprows=1, usecols=(2), unpack=True, delimiter=',')
        SFR10 = StarFR10 - 9  # * np.log10(10) = 1 #Msun h^-1 yr^-1

        gedges10 = np.array(np.arange(gmin, gmax + dex, dex))  # Límites de los intervalos.
        ghist10 = gedges10[1:] - 0.5 * dex  # centros de los intervalos.

        freq10, bins_edges = np.histogram(SFR10, bins=gedges10)
        freq10 = freq10 / (dex * volumen)
        ftot10 = np.log10(freq10, where=0 < freq10)

        '''TODAS LAS GALAXIAS'''
        StarFRAll = np.loadtxt(ffall, skiprows=2, usecols=(1), unpack=True, delimiter=',')
        SFRAll = StarFRAll - 9  # * np.log10(10) = 1 #Msun h^-1 yr^-1

        freqAll = np.loadtxt(ffall, skiprows=2, usecols=(2), unpack=True, delimiter=',')
        freqAll = freqAll / (volumen * dex)
        ftotAll = np.log10(freqAll, where=0 < freqAll)

        plt.style.use(Style.style1)
        plt.xlabel('log$_{10} \; $(SFR $[M_{\odot} \; h^{-1} \; yr^{-1}$])')
        plt.ylabel('log$_{10} \; (\phi \; [h^3 \; Mpc ^{-3} \; dex^{-1}$])')
        #plt.title('Función Masas redshifts altos SAGE con corte en masas altas')
        plt.xlim(-0.5, 3.5)
        #plt.ylim(-10,-5)

        ind10 = np.where(ftot10 < 0)
        indHigh = np.where(ftotHigh < 0)
        indAll = np.where(ftotAll < 0)

        plt.plot(ghist10[ind10], ftot10[ind10], 'o', color ='steelblue', label='10$\%$ ' + sim + ' z = ' + zsim + '')
        plt.plot(ghist[indHigh], ftotHigh[indHigh], '*', color='r', label='Corte ' + sim + ' z = ' + zsim + '')
        plt.plot(SFRAll[indAll], ftotAll[indAll], '^', color = 'k', label='' + sim + ' z = ' + zsim + '')

        photonom = 'C:/Users/Olivia/TFG-TUT/Figuras/Definitivas/FuncionSFR_10_z_' + zsim + '.png'
        plt.legend()
        plt.savefig(photonom)
        plt.show()