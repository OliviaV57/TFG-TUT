import numpy as np
import matplotlib.pyplot as plt
import os.path
import sys

'''Parámetros de la simulación'''
volumen = 1000**3 #(Mpc/h)^3

'''Parámetros de la observación'''
h = 0.71

'''Constantes'''
dexSim = 0.1


# Creo unos arrays con todos los z para automatizarlo:

zobs = ['0.0-0.3', '0.45-0.6', '1.0-1.2','2.0-2.5', '3.0-4.2']
zsims = ['0.142', '0.523', '1.077', '2.235', '3.61']
simnom = ['SAGE', 'Galacticus']
#simnom = ['Galacticus', 'Sage', 'Sag']

for iiz, zob in enumerate(zobs):
    # print(iiz, zob)

    '''OBSERVACIONES'''
    ffobs = 'C:/Users/Olivia/TFG-TUT/Obs_Data/sfrf/gruppioni_2015_z'+zob+'_cha.txt'
    SFRobs_Low = np.loadtxt(ffobs, skiprows=4, usecols=(0), unpack=True) + np.log10(h)
    SFRobs_High = np.loadtxt(ffobs, skiprows=4, usecols=(1), unpack=True) + np.log10(h)
    freqObs = np.loadtxt(ffobs, skiprows=4, usecols=(2), unpack=True) - 3 * np.log10(h)
    errorObs = np.loadtxt(ffobs, skiprows=4, usecols=(3), unpack=True) - 3 * np.log10(h)

    dexObs = SFRobs_High - SFRobs_Low
    ghistObs = SFRobs_High - 0.5 * dexObs

    for sim in simnom:
        ffsim = 'C:/Users/Olivia/TFG-TUT/Datos_simulaciones/histograma_'+sim+'_z_'+zsims[iiz]+'.csv'

        if not os.path.isfile(ffsim):
            continue

        #print(ffsim)
        #dataSim = np.loadtxt(ffsim, dtype=str, unpack=True)  # dtype str para poder leer palabras también.
        StarFRSim = np.loadtxt(ffsim, skiprows=2, usecols=(1), unpack=True, delimiter=',')
        SFRSim = StarFRSim - 9  # * np.log10(10) = 1 #Msun h^-1 yr^-1

        freqSim = np.loadtxt(ffsim, skiprows=2, usecols=(2), unpack=True, delimiter=',')
        freqSim = freqSim / (volumen * dexSim)
        ftotSim = np.log10(freqSim, where=0 < freqSim)


        figure = 'redshift = ' + zsims[iiz] + ''
        print(figure)
        plt.figure(figure)

        # para cada z una gráfica:
        plt.xlabel('$Log_{10} \; $(SFR $[M_{\odot} \; h^{-1}\; yr^{-1}$])')
        plt.ylabel('$Log_{10} \; (\phi \; [h^3 \; Mpc ^{-3} \; dex^{-1}$])')
        plt.title('Función SFR SAGE vs Galacticus vs Observacional')
        plt.xlim(-0.5, 4)


        indSim = np.where(ftotSim < 0)
        plt.plot(SFRSim[indSim], ftotSim[indSim], label= ''+sim+' z = '+zsims[iiz]+'')

    plt.plot(ghistObs, freqObs, 'm', marker='o', linewidth=0, label='Obs z = ' + zob + '')
    plt.errorbar(ghistObs, freqObs, yerr=errorObs, xerr=None, fmt='.m')

    plt.legend()
    plotnom = 'C:/Users/Olivia/TFG-TUT/Figuras/Obs_Sage_Gala_allgalaxies_z_' + zsims[iiz] + '.png'
    # print(plotnom)
    plt.savefig(plotnom)












plt.show()
