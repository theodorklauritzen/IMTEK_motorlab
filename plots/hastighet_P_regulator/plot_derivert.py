
import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt

# For et syyykt irriterende bibliotek, det har ikke blitt oppdatert på to år, så og er bugs som har vært kjent i halvannet år her som er mega irriterende
#from tikzplotlib import save as save_tikz

# Smerke og lidelse, jeg hater ulike python miljøer
#plt.rcParams.update({
#   "text.usetex": True,
#   "font.family": "sans-serif",
#   "font.sans-serif": ["Helvetica"]})

dataSlice = slice(8000, 15000, 1)

# Her kan dere legge inn flere filer om dere trenger det
measurementFile = "Hastighet_P_maaling.csv"
#referenceFile = "Hastighet_P_referanse.csv"

measData = pd.read_csv(measurementFile)

#refData= pd.read_csv(referenceFile)
# Hent ut måleserie og tid, konverter til numpy
measTime = measData.iloc[:,0].to_numpy()
measSignal = measData.iloc[:,1].to_numpy()
#refTime = refData.iloc[:,0].to_numpy()
#refSignal = refData.iloc[:,1].to_numpy()

samplePeriod = np.max(measTime) - np.min(measTime)
sampleFrequency = len(measTime) / samplePeriod
cutoff = 120
nyq = 0.5 * sampleFrequency

def butter_lowpass_filter(data, cutoff, order = 2):
    normal_cutoff = cutoff / nyq
    # Get the filter coefficients 
    b, a = sp.signal.butter(order, normal_cutoff, btype='low', analog=False)
    y = sp.signal.filtfilt(b, a, data)
    return y

measSignalFiltered = butter_lowpass_filter(measSignal, cutoff)

measSignalDerivated = np.diff(measSignalFiltered) / np.diff(measTime)

measSignal = measSignal[dataSlice]
measTime = measTime[dataSlice]
measSignalDerivated = measSignalDerivated[dataSlice]

measTime = (measTime - np.min(measTime)) * 1000 # Setter starten på tidsaksen til 0 og konverterer til ms
#refTime = (refTime - np.min(refTime)) * 1000 # Setter starten på tidsaksen til 0 og konverterer til ms

# Plot med pyplot, her kan dere bruke så mye avanserte funksjoner dere vil, med subplots osv
fig, ax = plt.subplots(1,1)
# Vi hopper 100 punkter om gangen her for å spare regnekraft når vi tegner plottet. Denne må tilpasses til hvor tett data er samplet
ax.plot(measTime, measSignalDerivated, label="Derivert respons")
ax.plot(measTime, 35 * (measSignal + 5), label="Referansespenning")
ax.set_title("P-regulator derivert")
ax.set_xlabel("$t$ [ms]")
ax.set_ylabel("$V$ [V/s]")

# Bruk denne for å få en vining som ikke er i latex, må kommenteres ut når vi skal eksportere latex
plt.show()

# Denne linjen lagrer til Latex
#save_tikz('out.tex') #Merk: denne funker ikke om dere bruker plt.show() i scriptet
