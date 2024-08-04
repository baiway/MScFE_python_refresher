import numpy as np
from scipy.constants import k, m_p   # Boltzmann's constant, proton mass
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def maxwell_boltzmann(v, T):
    """
    Calculates the probability density (i.e. probability per unit
    speed) of finding a molecule with speed `v` in hydrogen gas at
    temperature `T` using the Maxwell-Boltzmann distribution [1].

    [1] https://en.wikipedia.org/wiki/Maxwell-Boltzmann_distribution
    """
    m = 2 * m_p  # hydrogen is diatomic
    prefactor = (m / (2 * np.pi * k * T))**(3/2)
    return prefactor * 4 * np.pi * v**2 * np.exp(-m * v**2 / (2 * k * T))


# Load speeds and sort for plotting histogram later
speeds = np.loadtxt("speeds.txt")
speeds = np.sort(speeds)

# Create histogram and determine bin centres for curve fitting
hist, bin_edges = np.histogram(speeds, bins=50, density=True)
bin_centres = (bin_edges[:-1] + bin_edges[1:]) / 2

# Fit a Maxwell-Boltzmann distribution to the histogram
#
# `p0` is the 'initial guess' for the temperature parameter `T`.
# SciPy's `curve_fit` iteratively changes this to minimise the
# least-squares error.
#
# `curve_fit` then returns two parameters:
#  - `popt`: an array of optimimal parameters that minimise the least-
#          squares error. We extract the temperature from this
#  - `pcov`: a 2D array of popt covariances (there is uncertainty
#          associated with the fitting procedure). To obtain the
#          variances in individual parameters, we extract the diagonal
#          elements.
#
# Details: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html
popt, pcov = curve_fit(f=maxwell_boltzmann, xdata=bin_centres, ydata=hist, p0=[300])
T_fit = popt[0]
T_err = np.sqrt(pcov[0][0])

# Print the mean temperature +/- standard deviation
print(f"temperature = ({T_fit:.2f} +/- {T_err:.2f}) kelvin")

# Determine a new Maxwell distribution using the temperature
# from `curve_fit`
dist = maxwell_boltzmann(speeds, T_fit)

# Plot results
plt.figure(figsize=(10,6))
plt.bar(bin_centres, hist, width=bin_edges[1] - bin_edges[0], alpha=0.6,
        color="g", label="Speeds histogram")
plt.plot(speeds, dist, label=f"Maxwellian with T = {round(T_fit)}")
plt.xlabel("Speed (m/s)")
plt.ylabel("Probability density")
plt.legend()
plt.grid(True)
plt.savefig("distribution.png")
plt.show()
