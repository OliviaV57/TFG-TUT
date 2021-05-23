import numpy as np
import matplotlib.pyplot as plt
import os.path
import Style
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
cm = plt.get_cmap('tab10') # Colour map to draw colours from

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

    for iis, sim in enumerate(simnom):
        ffsim = 'C:/Users/Olivia/TFG-TUT/Datos_simulaciones/histograma_'+sim+'_z_'+zsims[iiz]+'.csv'

        if not os.path.isfile(ffsim):
            continue
        cols = []
        col = cm(1.*iis/len(simnom))
        cols.append(col)
        #print(ffsim)
        #dataSim = np.loadtxt(ffsim, dtype=str, unpack=True)  # dtype str para poder leer palabras también.
        StarFRSim = np.loadtxt(ffsim, skiprows=2, usecols=(1), unpack=True, delimiter=',')
        SFRSim = StarFRSim - 9  # * np.log10(10) = 1 #Msun h^-1 yr^-1

        freqSim = np.loadtxt(ffsim, skiprows=2, usecols=(2), unpack=True, delimiter=',')
        freqSim = freqSim / (volumen * dexSim)
        ftotSim = np.log10(freqSim, where=0 < freqSim)

        plt.style.use(Style.style1)
        figure = 'redshift = ' + zsims[iiz] + ''
        # print(figure)
        plt.figure(figure)

        # para cada z una gráfica:
        plt.xlabel('log$_{10} \; $(SFR $[M_{\odot} \; h^{-1}\; yr^{-1}$])')
        plt.ylabel('log$_{10} \; (\phi \; [h^3 \; Mpc ^{-3} \; dex^{-1}$])')
        #plt.title('Función SFR SAGE vs Observacional')
        plt.xlim(-0.5, 3.5)

        indSim = np.where(ftotSim < 0)
        #axp.plot(kg,pkg,color = col, )
        plt.plot(SFRSim[indSim], ftotSim[indSim], color = col, label= ''+sim+' z = '+zsims[iiz]+'')

    plt.plot(ghistObs, freqObs, 'k', marker='o', linewidth=0, label='Obs z = ' + zob + '')
    plt.errorbar(ghistObs, freqObs, yerr=errorObs, xerr=None, fmt='.k')

    plt.legend()
    plotnom = 'C:/Users/Olivia/TFG-TUT/Figuras/Definitivas/Obs_Sage_allgalaxies_z_' + zsims[iiz] + '.png'
    # print(plotnom)
    plt.savefig(plotnom)


plt.show()




'''

            #HAcer lo mismo con lo siguiente, no olvidar tabulador

    StarFRGala = np.loadtxt(ffGalacticus, skiprows=1, usecols=(1), unpack=True, delimiter=',')
    SFRGala = StarFRGala - 9 * np.log10(10) #Msun h^-1 yr^-1

    StarFRSage = np.loadtxt(ffSage, skiprows=1, usecols=(1), unpack=True, delimiter=',')
    SFRSage = StarFRSage - 9  # * np.log10(10) = 1 #Msun h^-1 yr^-1

    StarFRSag = np.loadtxt(ffSag, skiprows=1, usecols=(1), unpack=True, delimiter=',')
    SFRSag = StarFRSag - 9  # * np.log10(10) = 1 #Msun h^-1 yr^-1

   


   

    freqGala = np.loadtxt(ffGalacticus, skiprows=1, usecols=(2), unpack=True, delimiter=',')
    freqGala = freqGala / (volumen * dexSim)
    ftotGala = np.log10(freqGala, where=0 < freqGala)
    # print(ftotGala)

    freqSage = np.loadtxt(ffSage, skiprows=1, usecols=(2), unpack=True, delimiter=',')
    freqSage = freqSage / (volumen * dexSim)
    ftotSage = np.log10(freqSage, where=0 < freqSage)
    # print(ftotSage)

    freqSag = np.loadtxt(ffSag, skiprows=1, usecols=(2), unpack=True, delimiter=',')
    freqSag = freqSag / (volumen * dexSim)
    ftotSag = np.log10(freqSag, where=0 < freqSag)
    # print(ftotSag)






    indGala = np.where(ftotGala[iiz] < 0)
    plt.plot(SFRGala[indGala], ftotGala[indGala], 'g', label='Galacticus z = 0')
    indSage = np.where(ftotSage[iiz] < 0)
    plt.plot(SFRSage[indSage], ftotSage[indSage], 'r', label='SAGE z = 0')
    indSag = np.where(ftotSag[iiz] < 0)
    plt.plot(SFRSag[indSag], ftotSag[indSag], 'y', label='SAG z = 0')
'''


    #plt.legend()

    #plotnom = "Obs_Galacticus_Sage_Sag_allgalaxies_z_'+zsims[iiz]+'.png"
               #+zsims[iiz]+'.png'

    #hacer un print y ver que funciona

    #plt.savefig('C:/Users/Olivia/TFG-TUT/Figuras/Obs_Galacticus_Sage_Sag_allgalaxies_z_'+zsims[iiz]+'.png')
    #plt.savefig(plotnom)
    #plt.show()
