import numpy as np
import matplotlib.pyplot as plt
import sys

'''Parámetros de la simulación'''
volumen = 1000**3 #(Mpc/h)^3 #No estoy segura de que este sea el volumen, en el paper no lo encuentro

'''Parámetros de las observación'''
hobs = 0.71

file = 'C:/Users/Olivia/TFG-TUT/Obs_Data/sfrf/gruppioni_2015_z0.0-0.3_cha.txt'
file2 = 'C:/Users/Olivia/TFG-TUT/Obs_Data/sfrf/gruppioni_2015_z0.3-0.45_cha.txt'
file3 = 'C:/Users/Olivia/TFG-TUT/Obs_Data/sfrf/gruppioni_2015_z0.45-0.6_cha.txt'

data = np.loadtxt(file, dtype=str,  unpack=True) #dtype str para poder leer palabras también.
data1 = np.loadtxt(file2, dtype=str,  unpack=True)
data2 = np.loadtxt(file3, dtype=str,  unpack=True)

StarFR_low = np.loadtxt(file, usecols=(0), unpack=True) + np.log10(hobs) #log(Msun yr^-1 h^-1)
StarFR_high = np.loadtxt(file, skiprows=4, usecols=(1), unpack=True) + np.log10(hobs) # si es # entiende qu elo salta
freq = np.loadtxt(file, skiprows=4, usecols=(2), unpack=True) - 3 * np.log10(hobs)
error = np.loadtxt(file, skiprows=4, usecols=(3), unpack=True) - 3 * np.log10(hobs)

#print(StarFR_low)
#print(StarFR_high)
#print(freq)
#print(error)


StarFR_low2 = np.loadtxt(file2, skiprows=4, usecols=(0), unpack=True) + np.log10(1/hobs)
StarFR_high2 = np.loadtxt(file2, skiprows=4, usecols=(1), unpack=True) + np.log10(1/hobs)
freq2 = np.loadtxt(file2, skiprows=4, usecols=(2), unpack=True) - 3 * np.log10(hobs)
error2 = np.loadtxt(file2, skiprows=4, usecols=(3), unpack=True) - 3 * np.log10(hobs)

StarFR_low3 = np.loadtxt(file3, skiprows=4, usecols=(0), unpack=True) + np.log10(1/hobs)
StarFR_high3 = np.loadtxt(file3, skiprows=4, usecols=(1), unpack=True) + np.log10(1/hobs)
freq3 = np.loadtxt(file3, skiprows=4, usecols=(2), unpack=True) - 3 * np.log10(hobs)
error3 = np.loadtxt(file3, skiprows=4, usecols=(3), unpack=True) - 3 * np.log10(hobs)


# dex = 0.1
dex = StarFR_high - StarFR_low
#print(dex)

ghist = StarFR_high - 0.5 * dex

#print(ghist)

dex2 = StarFR_high2 - StarFR_low2
ghist2 = StarFR_high2 - 0.5 * dex2

dex3 = StarFR_high3 - StarFR_low3
ghist3 = StarFR_high3 - 0.5 * dex3




plt.xlabel('$Log_{10} \; $(SFR $[M_{\odot} \; h^{-1}\; yr^{-1}$])')
plt.ylabel('$Log_{10} \; (\phi \; [h^3 \; Mpc ^{-3} \; dex^{-1}$])')
plt.title('Histograma SFR Obs')
plt.xlim(0.7, 2.5)

# plt.plot(ghist, ftot)
# ind = np.where(freq<0)

plt.plot(ghist, freq, 'b', label = '0.0< z < 0.3')
plt.plot(ghist2, freq2, 'r', label = '0.3< z < 0.45')
plt.plot(ghist3, freq3, 'g', label = '0.45< z < 0.6')
#plt.legend('0.0< z < 0.3', '0.3< z < 0.45', '0.45 < z < 0.6')
plt.errorbar(ghist, freq, yerr=error, xerr=None, fmt = '.b')
plt.errorbar(ghist2, freq2, yerr=error2, xerr=None, fmt = '.r')
plt.errorbar(ghist3, freq3, yerr=error3, xerr=None, fmt = '.g')
plt.legend()
plt.savefig('C:/Users/Olivia/TFG-TUT/Figuras/histo_SFR_OBS_3z.png')
plt.show()