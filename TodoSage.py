import numpy as np
import matplotlib.pyplot as plt
import sys

'''Parámetros de la simulación'''
volumen = 1000**3 #(Mpc/h)^3

'''Constantes'''
dexSim = 0.1

zsims = ['0,142', '0,523', '1,077', '2,235', '3,61']
simnom = ['SAGE']

for iiz, zsim in enumerate(zsims):
    for sim in simnom:
        ffsim = 'C:/Users/Olivia/TFG-TUT/Datos_simulaciones/histograma_' + sim + '_z_' + zsim + '.csv'
        # print(ffsim)
        # dataSim = np.loadtxt(ffsim, dtype=str, unpack=True)  # dtype str para poder leer palabras también.
        StarFRSim = np.loadtxt(ffsim, skiprows=2, usecols=(1), unpack=True, delimiter=',')
        SFRSim = StarFRSim - 9  # * np.log10(10) = 1 #Msun h^-1 yr^-1

        freqSim = np.loadtxt(ffsim, skiprows=2, usecols=(2), unpack=True, delimiter=',')
        freqSim = freqSim / (volumen * dexSim)
        ftotSim = np.log10(freqSim, where=0 < freqSim)

        plt.xlabel('$Log_{10} \; $(SFR $[M_{\odot} \; h^{-1}\; yr^{-1}$])')
        plt.ylabel('$Log_{10} \; (\phi \; [h^3 \; Mpc ^{-3} \; dex^{-1}$])')
        plt.title('Función SFR todos los redshifts SAGE')
        plt.xlim(-0.5, 4)

        indSim = np.where(ftotSim < 0)
        plt.plot(SFRSim[indSim], ftotSim[indSim], label= ''+sim+' z = '+zsim+'')


plt.legend()
plt.savefig('C:/Users/Olivia/TFG-TUT/Figuras/SAGE_todosZ.png')
plt.show()