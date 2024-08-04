# Exercise 2: estimating the temperature of a gas using SciPy's `curve_fit`
The file `speeds.txt` contains a list of molecular speeds for a sample of hydrogen gas containing 10,000 molecules. Your task is to estimate the temperature of this gas based on the distribution of speeds. You may assume the molecules follow a Maxwell-Boltzmann distribution, where the probability distribution of speeds is given by

```math
f(v) = \left( \frac{m}{2\pi k_\text{B}T}\right)^{3/2} 4\pi v^2 \exp\left(-\frac{mv^2}{2k_\text{B}T} \right)
```

where $m$ is the mass of a hydrogen molecule (diatomic!), $k_\text{B}$ is Boltzmann's constant, $T$ is the gas temperature in kelvin, and $v$ is the molecular speed.

If you're not sure where to start, click Hint \#1 below.

## Hints
<details>
  <summary>Hint #1 (click me)</summary>
  
  This task involves curve fitting. I recommend SciPy's `curve_fit` function (see [scipy.optimize.curve_fit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html), but alternatives are available. The code below illustrates a common `curve_fit` pattern. 

  ```python
  import numpy as np
  from scipy.optimize import curve_fit
  import matplotlib.pyplot as plt

  def func(x, a, c):
      """Parabola with equation y = a * x^2 + c."""
      return a * x**2 + c

  # Generate 10 x-coordinates over interval [-10, 10)
  xdata = np.random.uniform(-10, 10, 10)

  # Generate ydata that follows y = 0.5 * x^2 + 5 but with some noise
  ydata = 0.5 * xdata**2 + 5 + np.random.normal(0, 0.5, size=xdata.size)

  # Fit parabola defined in `func` to data. Here we're setting our guess
  # for the parameters `a` and `c` to be 1 and 3 respectively
  # (even though we know they're 0.5 and 5 respectively).
  popt, pcov = curve_fit(f=func, xdata=xdata, ydata=ydata, p0=[1, 3])
  afit, cfit = popt
  aerr, cerr = np.sqrt(np.diag(pcov))

  # Print fit parameters
  print(f"a = {afit:.2f} +/- {aerr:.2f}")
  print(f"c = {cfit:.2f} +/- {cerr:.2f}")

  # Plot smooth fit using more points and parameters from curve_fit
  x = np.linspace(-10, 10, 100)
  yfit = func(x, afit, cfit)
  plt.scatter(xdata, ydata, label="data")
  plt.plot(x, yfit, label="fit", linestyle="dashed")
  plt.legend()
  plt.show()
  ```

  Use the example above as a template to work through the exercise:
  - The molecular speeds in `speeds.txt` will play the role of `xdata`
  - You can define a function `maxwell-boltzmann` that takes two arguments, the molecular speed `v` and the gas temperature `T`, to replace `func`. Here `T` will be our fit parameter determined by `curve_fit`.
  - For `ydata`, put the molecular speeds into bins using [NumPy's `histogram`](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html) function. If you're not sure how to do this, click on Hint \#2.
    ```
  
</details>

<details>
  <summary>Hint #2 (click me)</summary>
  
  You can use NumPy's `histogram` function (see [numpy.histogram](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html)) to produce a histogram.
  ```python
  hist, bin_edges = np.histogram(speeds, bins=50, density=True)
  bin_centres = (bin_edges[:-1] + bin_edges[1:]) / 2
  ```

  You can now use replace `xdata` with `bin_centres` and `ydata` with `hist` in the template code above.

  If you want to later plot the histogram, use the following snippet. Alternatively, you can use Matplotlib's `hist` function (see [`matplotlib.pyplot.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)).
  ```python
  import matplotlib.pyplot as plt
  
  plt.bar(bin_centres, hist, width=bin_edges[1] - bin_edges[0], label="histogram")
  plt.xlabel("Speed (m/s)")
  plt.ylabel("Probability density")
  plt.legend()
  plt.grid(True)
  plt.show()
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
