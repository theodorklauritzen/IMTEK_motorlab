
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# For et syyykt irriterende bibliotek, det har ikke blitt oppdatert på to år, så og er bugs som har vært kjent i halvannet år her som er mega irriterende
from tikzplotlib import save as save_tikz

# Smerke og lidelse, jeg hater ulike python miljøer
plt.rcParams.update({
   "text.usetex": True,
   "font.family": "sans-serif",
   "font.sans-serif": ["Helvetica"]})

# Her kan dere legge inn flere filer om dere trenger det
dataFilename = "data.csv"

dataSlice = slice(2000, 12000, 5)

rawdata = pd.read_csv(dataFilename)

# Hent ut måleserie og tid, konverter til numpy
measTime = rawdata.iloc[:,0].to_numpy()[dataSlice]
measSignal = rawdata.iloc[:,1].to_numpy()[dataSlice] * 0.95 + 0.3

measTime = (measTime - np.min(measTime)) * 1000 # Setter starten på tidsaksen til 0 og konverterer til ms

# Plot med pyplot, her kan dere bruke så mye avanserte funksjoner dere vil, med subplots osv
fig, ax = plt.subplots(1,1)
# Vi hopper 100 punkter om gangen her for å spare regnekraft når vi tegner plottet. Denne må tilpasses til hvor tett data er samplet
ax.plot(measTime, measSignal, label="Målt spenning")
ax.set_title("Posisjonmåling ved rotasjon")
ax.set_xlabel("$t$ [ms]")
ax.set_ylabel("$V$ [V]")

# Bruk denne for å få en vining som ikke er i latex, må kommenteres ut når vi skal eksportere latex
#plt.show()

# Denne linjen lagrer til Latex
save_tikz('out.tex') #Merk: denne funker ikke om dere bruker plt.show() i scriptet
