import numpy as np
import matplotlib.pyplot as plt
import os.path
import sys

path2sim = 'C:/Users/Olivia/TFG-TUT/Datos_simulaciones/'
#path2sim = '/home/violeta/teaching/olivia/'

'''Arrays para automatizarlo'''
zsims = ['3.61', '4.038', '5.017']
simnom = ['SAGE']
cm = plt.get_cmap('tab10')  # Colour map to draw colours from

'''Parámetros de la simulación'''
volumen = 1000**3 #(Mpc/h)^3

'''Constantes'''
dex = 0.1
gmin = -1
gmax = 4

for iiz, zsim in enumerate(zsims):
    for sim in simnom:
        ffsim = path2sim+'Mass_SFR_10_z_' + zsim + '.csv'
        # print(ffsim)
        # dataSim = np.loadtxt(ffsim, dtype=str, unpack=True)  # dtype str para poder leer palabras también.
        StarFRSim = np.loadtxt(ffsim, skiprows=1, usecols=(2), unpack=True, delimiter=',')
        SFRSim = StarFRSim - 9  # * np.log10(10) = 1 #Msun h^-1 yr^-1



        gedges = np.array(np.arange(gmin, gmax + dex, dex))  # Límites de los intervalos.
        ghist = gedges[1:] - 0.5 * dex  # centros de los intervalos.

        freq, bins_edges = np.histogram(SFRSim, bins=gedges)
        freq = freq / (dex * volumen)
        ftot = np.log10(freq, where=0 < freq)

        plt.xlabel('log$_{10} \; $(SFR $[M_{\odot} \; h^{-1} \; yr^{-1}$])')
        plt.ylabel('log$_{10} \; (\phi \; [h^3 \; Mpc ^{-3} \; dex^{-1}$])')
        #plt.title('Función Masas redshifts altos SAGE con corte en masas altas')
        #plt.xlim(-0.5, 3.5)
        #plt.ylim(-7,-1)

        indSim = np.where(ftot < 0)
        plt.plot(ghist[indSim], ftot[indSim], '.', label= ''+sim+' z = '+zsim+'')

        photonom = 'C:/Users/Olivia/TFG-TUT/Figuras/FuncionSFR_corte_z_' + zsim + '.png'
        plt.legend()
        #plt.savefig(photonom)
        plt.show()