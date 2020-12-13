import numpy as np
import matplotlib.pyplot as plt
import sys

'''Parámetros de la simulación'''
volumen = 1000**3 #(Mpc/h)^3
file1 = 'C:/Users/Olivia/TFG-TUT/Datos_simulaciones/SFR_Galacticus_z1.csv'
file2 = 'C:/Users/Olivia/TFG-TUT/Datos_simulaciones/SFR_Galacticus_z2.csv'
file3 = 'C:/Users/Olivia/TFG-TUT/Datos_simulaciones/SFR_Galacticus_z3.csv'

data1 = np.loadtxt(file1, dtype=str,  unpack=True) #dtype str para poder leer palabras también.
StarFR1 = np.loadtxt(file1, skiprows=1, usecols=(2), unpack=True, delimiter=',')
SFR1 = StarFR1 / (10**9) #Msun h^-1 yr^-1
SFRl1 = np.log10(SFR1) #log(Msun h^-1 yr^-1)
# print('logaritmo SFR = {}'.format(SFRl))

data2 = np.loadtxt(file2, dtype=str,  unpack=True) #dtype str para poder leer palabras también.
StarFR2 = np.loadtxt(file2, skiprows=1, usecols=(2), unpack=True, delimiter=',')
SFR2 = StarFR2 / (10**9) #Msun h^-1 yr^-1
SFRl2 = np.log10(SFR2) #log(Msun h^-1 yr^-1)

data3 = np.loadtxt(file3, dtype=str,  unpack=True) #dtype str para poder leer palabras también.
StarFR3 = np.loadtxt(file3, skiprows=1, usecols=(2), unpack=True, delimiter=',')
SFR3 = StarFR3 / (10**9) #Msun h^-1 yr^-1
SFRl3 = np.log10(SFR3) #log(Msun h^-1 yr^-1)


# print('SFR = {}'.format(SFR))

#gmin = np.amin(SFRl)
#gmax = np.amax(SFRl)

gmin = -1
gmax = 4
# print(gmin, gmax) #¿Por qué lo tengo que acotar así? ¿por que el resto no nos interesa?


# dex = 0.1
dex = 0.2
gedges = np.array(np.arange(gmin, gmax + dex, dex)) # Límites de los intervalos.
ghist = gedges[1:] - 0.5 * dex # centros de los intervalos.

# print('gedges = {}'.format(gedges))
# print(len(gedges))
freq1, bins_edges = np.histogram(SFRl1, bins=gedges)
freq2, bins_edges2 = np.histogram(SFRl2, bins=gedges)
freq3, bins_edges3 = np.histogram(SFRl3, bins=gedges)

'''Cambio de unidades eje y: '''

freq1 = freq1/(dex * volumen)
ftot1 = np.log10(freq1, where = 0<freq1) # El where deja como 0 donde hay 0, no hace el log de 0 ya que no existe.

freq2 = freq2/(dex * volumen)
ftot2 = np.log10(freq2, where = 0<freq2)

freq3 = freq3/(dex * volumen)
ftot3 = np.log10(freq3, where = 0<freq3)

#print('frecuencias = {}'.format(ftot))

plt.xlabel('$Log_{10} \; $(SFR $[M_{\odot} \; h^{-1}\; yr^{-1}$])')
plt.ylabel('$Log_{10} \; (\phi \; [h^3 \; Mpc ^{-3} \; dex^{-1}$])')
plt.title('Histograma SFR Galacticus')
plt.xlim(-1,2)

# plt.plot(ghist, ftot)
ind1 = np.where(ftot1<0)
ind2 = np.where(ftot2<0)
ind3 = np.where(ftot3<0)

plt.plot(ghist[ind1], ftot1[ind1], 'b', label='0.0<z<0.3') #Los puntos donde la frecuencia es 0 no la pinta.
plt.plot(ghist[ind2], ftot2[ind2], 'r', label='0.3<z<0.45')
plt.plot(ghist[ind3], ftot3[ind3], 'g', label='0.45<z<0.6')

plt.legend()
plt.savefig('C:/Users/Olivia/TFG-TUT/Figuras/histo_SFR_Galacticus_3z.png')
plt.show()
