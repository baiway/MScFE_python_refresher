import numpy as np
from scipy.constants import k, m_p
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def maxwell_boltzmann(v, T):
    """Maxwellian distribution defined here:
    https://en.wikipedia.org/wiki/Maxwell%E2%80%93Boltzmann_distribution"""
    factor = (m_p / (2 * np.pi * k * T))**(3/2)
    return 4 * np.pi * v**2 * factor * np.exp(-m_p * v**2 / (2 * k * T))


speeds = np.loadtxt("speeds.txt")
speeds = np.sort(speeds) # sorted for plotting later

hist, bin_edges = np.histogram(speeds, bins=50, density=True)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

popt, pcov = curve_fit(f=maxwell_boltzmann, xdata=bin_centers, ydata=hist, p0=[300])
T_fit = popt[0]
T_err = np.sqrt(pcov[0][0])

print(f"temperature = ({T_fit:.2f} +/- {T_err:.2f}) kelvin")

dist = maxwell_boltzmann(speeds, T_fit)

plt.figure(figsize=(10,6))
plt.bar(bin_centers, hist, width=bin_edges[1] - bin_edges[0], alpha=0.6, color="g", 
        label="Speeds histogram")
plt.plot(speeds, dist, label=f"Maxwellian with T = {int(T_fit)}")
plt.xlabel("Speed (m/s)")
plt.ylabel("Probability density")
plt.legend()
plt.grid(True)
plt.legend()
plt.savefig("distribution.png")
plt.show()
