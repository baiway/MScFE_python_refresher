# Exercise 2: estimating the temperature of a gas using SciPy's `curve_fit`
The file `speeds.txt` contains a list of molecular speeds for a sample of hydrogen gas containing 10,000 molecules. Your task is to estimate the temperature of this gas based on the distribution of speeds. You may assume the molecules follow a Maxwell-Boltzmann distribution, where the probability distribution of speeds is given by

```math
f(v) = \left( \frac{m}{2\pi k_\text{B}T}\right)^{3/2} 4\pi v^2 \exp\left(-\frac{mv^2}{2k_\text{B}T} \right)
```

where $m$ is the mass of a hydrogen molecule (diatomic!), $k_\text{B}$ is Boltzmann's constant, $T$ is the temperature in kelvin, $v$ is the molecular speed.

<details>
  <summary>Tip #1 (click me)</summary>
  
  Plot a histogram (use however many bins you like; I used 50).
  
</details>

<details>
  <summary>Tip #2 (click me)</summary>
  
  Fit a Maxwell-Boltzmann distribution to your histogram:

  ```python
  import numpy as np
  from scipy.constants import k, m_p
  from scipy.optimize import curve_fit

  def maxwell_boltzmann(v, T):
    factor = (m_p / (2 * np.pi * k * T))**(3/2)
    return 4 * np.pi * v**2 * factor * np.exp(-m_p * v**2 / (2 * k * T))

  # ...

  hist, bin_edges = np.histogram(speeds, bins=50, density=True)
  bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

  popt, pcov = curve_fit(f=maxwell_boltzmann, xdata=bin_centers, ydata=hist, p0=[300])
  T_fit = popt[0]
  ```
  
</details>

## Correct answers
<details>
  <summary>Click me!</summary>
  
  ```txt
  temperature = (297.47 +/- 2.78) kelvin
  ```
  ![Histogram with 50 bins showing the spread of molecular speeds in `speeds.txt`. A Maxwell-Boltzmann distribution with the calculated $T=299\:\text{K}$ is overplotted.](distribution.png)
  
</details>
