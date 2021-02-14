import numpy as np
import matplotlib.pyplot as plt
import os.path
import sys

'''Parámetros de la simulación'''
volumen = 1000**3 #(Mpc/h)^3

'''Constantes'''
dexSim = 0.1

'''Arrays para automatizarlo'''
zsims = ['0.142', '3.61']
simnom = ['SAGE']

for iiz, zsim in enumerate(zsims):
   for sim in simnom:
        ffsim = 'C:/Users/Olivia/TFG-TUT/Datos_simulaciones/Histo_Mass_SFR_'+sim+'_z_'+zsims[iiz]+'.csv'

        if not os.path.isfile(ffsim):
            continue
        # print(ffsim)
        # dataSim = np.loadtxt(ffsim, dtype=str, unpack=True)  # dtype str para poder leer palabras también.
        MassSim = np.loadtxt(ffsim, skiprows=2, usecols=(1), unpack=True, delimiter=',') #Msun h^-1

        SFRSim = np.loadtxt(ffsim, skiprows=2, usecols=(2), unpack=True, delimiter=',')
        SFRSim = SFRSim - 9 # * np.log10(10) = 1 #Msun h^-1 yr^-1
        # ftotSim = np.log10(SFRSim, where=0 < SFRSim)

        #figure = 'redshift = ' + zsims[iiz] + ''
        #print(figure)
        #plt.figure(figure)

        # para cada z una gráfica:
        plt.ylabel('$Log_{10} \; $(SFR $[M_{\odot} \; h^{-1}\; yr^{-1}$])')
        plt.xlabel('$Log_{10} \; (Masa \; [M_{\odot} \; h^{-1} $])')
        plt.title('Función SFR SAGE frente Masa de las galaxias')
        plt.xlim(0, 12)

        indSim = np.where(SFRSim < 0)
        plt.plot(MassSim[indSim], SFRSim[indSim],'.', label='' + sim + ' z = ' + zsims[iiz] + '')

        plt.legend()
        plotnom = 'C:/Users/Olivia/TFG-TUT/Figuras/Mass_SFR_SAGE_z_' + zsims[iiz] + '.png'
        print(plotnom)
        plt.savefig(plotnom)

plt.show()