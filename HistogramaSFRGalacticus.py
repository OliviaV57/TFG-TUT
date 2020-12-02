import numpy as np
import matplotlib.pyplot as plt
import sys

'''Parámetros de la simulación'''
volumen = 1000**3 #(Mpc/h)^3

data = np.loadtxt('Mass_total_galacticus.csv', dtype=str,  unpack=True) #dtype str para poder leer palabras también.
StarFR = np.loadtxt('SFR_Galacticus_10000.csv', skiprows=1, usecols=(2), unpack=True, delimiter=',')
SFR = StarFR / (10**9)
SFRl = np.log10(SFR)
# print('logaritmo SFR = {}'.format(SFRl))

# print('SFR = {}'.format(SFR))

#gmin = np.amin(SFRl)
#gmax = np.amax(SFRl)

gmin = -1
gmax = 4
print(gmin, gmax) #¿Por qué lo tengo que acotar así? ¿por que el resto no nos interesa?


# dex = 0.1
dex = 0.2
gedges = np.array(np.arange(gmin, gmax + dex, dex)) # Límites de los intervalos.
ghist = gedges[1:] - 0.5 * dex # centros de los intervalos.

print('gedges = {}'.format(gedges))
print(len(gedges))
freq, bins_edges = np.histogram(SFRl, bins=gedges)

'''Cambio de unidades eje y: '''

freq = freq/(dex * volumen)
ftot = np.log10(freq, where = 0<freq) # El where deja como 0 donde hay 0, no hace el log de 0 ya que no existe.

print('frecuencias = {}'.format(ftot))

plt.xlabel('$Log_{10} \; $(SFR $[M_{\odot} \; h^{-1}\; Gyr^{-1}$])')
plt.ylabel('$Log_{10} \; (\phi \; [h^3 \; Mpc ^{-3} \; dex^{-1}$])')
plt.title('Histograma SFR Galacticus')

# plt.plot(ghist, ftot)
ind = np.where(ftot<0)

plt.plot(ghist[ind], ftot[ind]) #Los puntos donde la frecuencia es 0 no la pinta.
plt.savefig('histo_SFR_Galacticus.png')
plt.show()



