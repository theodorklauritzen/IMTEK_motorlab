
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# For et syyykt irriterende bibliotek, det har ikke blitt oppdatert på to år, så og er bugs som har vært kjent i halvannet år her som er mega irriterende
#from tikzplotlib import save as save_tikz

# Smerke og lidelse, jeg hater ulike python miljøer
#plt.rcParams.update({
#   "text.usetex": True,
#   "font.family": "sans-serif",
#   "font.sans-serif": ["Helvetica"]})

# Her kan dere legge inn flere filer om dere trenger det

dataSlice = slice(0, -1, 1)
REF_VOLTAGE = 3.06 #2.98

DATA = np.genfromtxt('malinger.csv', delimiter=',')[1:,:].transpose()

DATA = DATA[:, DATA[0, :].argsort()]

FREKVENS = DATA[0]
FORSTERKNING = DATA[1] / REF_VOLTAGE
FASE_VINKEL = DATA[2]

#FREKVENS = np.array([0.1, 0.5, 1, 5, 7.5, 10, 50, 100])
#FASE_VINKEL = np.array([0, 0, -0.05, -6, -110, -150, -180, -180])

FREKVENS = FREKVENS[dataSlice]
FORSTERKNING = FORSTERKNING[dataSlice]
FASE_VINKEL = FASE_VINKEL[dataSlice]

forsterkning_db = 20 * np.log10(FORSTERKNING)

# Plot med pyplot, her kan dere bruke så mye avanserte funksjoner dere vil, med subplots osv
fig, ax = plt.subplots(1,1)

ax.grid(True, which="both", ls="-")


# Vi hopper 100 punkter om gangen her for å spare regnekraft når vi tegner plottet. Denne må tilpasses til hvor tett data er samplet
ax.set_xscale("log")
ax.set_xlabel("Frekvens [Hz]")
ax.set_ylabel("Fasevinkel [deg]")
ax.plot(FREKVENS, FASE_VINKEL)
ax.set_title("Bodeplot for Posisjonregulator")


# Bruk denne for å få en vining som ikke er i latex, må kommenteres ut når vi skal eksportere latex
plt.show()

# Denne linjen lagrer til Latex
#save_tikz('out.tex') #Merk: denne funker ikke om dere bruker plt.show() i scriptet
