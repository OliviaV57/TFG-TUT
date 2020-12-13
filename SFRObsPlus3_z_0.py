import numpy as np
import matplotlib.pyplot as plt
import sys

'''Parámetros de la simulación'''
volumen = 1000**3 #(Mpc/h)^3

'''Parámetros de la observación'''
h = 0.71

fileobs = 'C:/Users/Olivia/TFG-TUT/Obs_Data/sfrf/gruppioni_2015_z0.0-0.3_cha.txt'
dataobs = np.loadtxt(fileobs, dtype=str, unpack=True)
StarFR_low = np.loadtxt(fileobs, skiprows=4, usecols=(0), unpack=True) + np.log10(h)
StarFR_high = np.loadtxt(fileobs, skiprows=4, usecols=(1), unpack=True) + np.log10(h)
freqObs = np.loadtxt(fileobs, skiprows=4, usecols=(2), unpack=True) - 3 * np.log10(h)
errorObs = np.loadtxt(fileobs, skiprows=4, usecols=(3), unpack=True) - 3 * np.log10(h)

fileGala = 'C:/Users/Olivia/TFG-TUT/Datos_simulaciones/Histograma_Galacticus_z_0.csv'
dataGala = np.loadtxt(fileGala, dtype=str, unpack=True) #dtype str para poder leer palabras también.
StarFRGala = np.loadtxt(fileGala, skiprows=1, usecols=(1), unpack=True, delimiter=',')
SFRGala = StarFRGala - 9 * np.log10(10) #Msun h^-1 yr^-1
#print(StarFRGala)
#print('frecuencias = {}'.format(SFRGala))

fileSage = 'C:/Users/Olivia/TFG-TUT/Datos_simulaciones/histograma_Sage_z_0.csv'
dataSage = np.loadtxt(fileSage, dtype=str, unpack=True) #dtype str para poder leer palabras también.
StarFRSage = np.loadtxt(fileSage, skiprows=1, usecols=(1), unpack=True, delimiter=',')
SFRSage = StarFRSage - 9 #* np.log10(10) = 1 #Msun h^-1 yr^-1
#print(StarFRSage)
#print('frecuencias = {}'.format(SFRSage))

dexObs = StarFR_high - StarFR_low
dexGala = 0.1
dexSage = 0.1
dexSag = 0.1

ghistObs = StarFR_high - 0.5 * dexObs

freqGala = np.loadtxt(fileGala, skiprows=1, usecols=(2), unpack=True, delimiter=',')
freqGala = freqGala/(volumen*dexGala)
ftotGala = np.log10(freqGala, where = 0 < freqGala)
#print(ftotGala)

freqSage = np.loadtxt(fileSage, skiprows=1, usecols=(2), unpack=True, delimiter=',')
freqSage = freqSage/(volumen*dexSage)
ftotSage = np.log10(freqSage, where = 0 < freqSage)
#print(ftotSage)



plt.xlabel('$Log_{10} \; $(SFR $[M_{\odot} \; h^{-1}\; yr^{-1}$])')
plt.ylabel('$Log_{10} \; (\phi \; [h^3 \; Mpc ^{-3} \; dex^{-1}$])')
plt.title('Histograma SFR Galacticus vs SAGE vs Observacional')
plt.xlim(-0.5,2.5)

plt.plot(ghistObs, freqObs, 'b', marker = 'o', linewidth=0, label ='Obs 0.0< z < 0.3')
plt.errorbar(ghistObs, freqObs, yerr=errorObs, xerr=None, fmt = '.b')
indGala = np.where(ftotGala < 0)
plt.plot(SFRGala[indGala], ftotGala[indGala], 'g', label='Galacticus z = 0')
indSage = np.where(ftotSage < 0)
plt.plot(SFRSage[indSage], ftotSage[indSage], 'r', label='SAGE z = 0')


plt.legend()
plt.savefig('C:/Users/Olivia/TFG-TUT/Figuras/Obs_Galacticus_Sage_allgalaxies_z_0.png')
plt.show()
