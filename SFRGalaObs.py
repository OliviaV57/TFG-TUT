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

fileGala = 'C:/Users/Olivia/TFG-TUT/Datos_simulaciones/SFR_Galacticus_z1.csv'
dataGala = np.loadtxt(fileGala, dtype=str, unpack=True) #dtype str para poder leer palabras también.
StarFRGala = np.loadtxt(fileGala, skiprows=1, usecols=(2), unpack=True, delimiter=',')
SFRGala = StarFRGala / (10 ** 9) #Msun h^-1 yr^-1
logSFRGala = np.log10(SFRGala) #log(Msun h^-1 yr^-1)
# print('logaritmo SFR = {}'.format(SFRl))



dexObs = StarFR_high - StarFR_low
ghistObs = StarFR_high - 0.5 * dexObs


gmin = -1
gmax = 4

dexGala = 0.2
gedgesGala = np.array(np.arange(gmin, gmax + dexGala, dexGala)) # Límites de los intervalos.
ghistGala = gedgesGala[1:] - 0.5 * dexGala # centros de los intervalos.

freqGala, bins_edges = np.histogram(logSFRGala, bins=gedgesGala)
freqGala = freqGala / (dexGala * volumen)
ftotGala = np.log10(freqGala, where =0 < freqGala)
print(ftotGala)
print(ghistGala)


plt.xlabel('$Log_{10} \; $(SFR $[M_{\odot} \; h^{-1}\; yr^{-1}$])')
plt.ylabel('$Log_{10} \; (\phi \; [h^3 \; Mpc ^{-3} \; dex^{-1}$])')
plt.title('Histograma SFR Galacticus vs Observacional')
plt.xlim(-1,2)

plt.plot(ghistObs, freqObs, 'b', label ='Obs 0.0< z < 0.3')
indGala = np.where(ftotGala < 0)
plt.plot(ghistGala[indGala], ftotGala[indGala], 'g', label='Galacticus 0.0<z<0.3')


plt.legend()
plt.savefig('C:/Users/Olivia/TFG-TUT/Figuras/SFR_Galacticus_Obs_z1.png')
plt.show()

# NOTA: SALE GALACTICUS MÁS ABAJO PORQUE LA DENSIDAD DE GALAXIAS QUE HE USADO ES MUCHO MÁS PEQUEÑA, NO ESTÁN TODAS
# LAS GALAXIAS.