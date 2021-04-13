import numpy as np
import matplotlib.pyplot as plt
import sys

'''Parámetros de la observación'''
h = 0.71
zobs = ['0.0-0.3', '0.45-0.6', '1.0-1.2','2.0-2.5', '3.0-4.2']
color = ['b', 'y', 'g', 'r', 'm']
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

    plt.xlabel('log$_{10} \;$(SFR $[M_{\odot} \; h^{-1}\; yr^{-1}$])')
    plt.ylabel('log$_{10} \; (\phi \; [h^3 \; Mpc ^{-3} \; dex^{-1}$])')
    #plt.title('Función SFR todos los redshifts Observaciones')
    plt.xlim(-0.5, 3.5)

    #plt.plot(ghistObs, freqObs, marker = 'o', linewidth=0.2, label='Obs z = ' + zob + '')
    plt.errorbar(ghistObs, freqObs, yerr=errorObs, xerr=None, elinewidth=0.9, fmt='o--', label='Obs z = ' + zob + '')

plt.legend()
plt.savefig('C:/Users/Olivia/TFG-TUT/Figuras/Definitivas/Obs_todosZ.png')
plt.show()