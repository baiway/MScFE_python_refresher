import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Load data
t, signal = np.loadtxt("audio.csv", delimiter=",", skiprows=1, unpack=True)

# Perform the FFT
fft_result = np.fft.fft(signal)
fft_magnitude = np.abs(fft_result)
fft_freq = np.fft.fftfreq(len(signal), d=(t[1] - t[0]))

# Only take the positive frequencies
freqs = fft_freq[:len(fft_freq)//2]
magnitudes = fft_magnitude[:len(fft_magnitude)//2]

# Find peaks in the magnitudes
peaks, _ = find_peaks(magnitudes)
peak_freqs = freqs[peaks]
print("Frequencies identified from FFT include:")
for pf in peak_freqs:
    print(f"  {pf} Hz")

# Visualise peaks in the FFT between 400 and 500 Hz
lower = np.argmin(np.abs(400 - freqs))
upper = np.argmin(np.abs(freqs - 500))
plt.figure(figsize=(10, 4))
plt.plot(freqs[lower:upper], magnitudes[lower:upper])
plt.title("Frequency spectrum")
plt.xlabel("Frequency / Hz")
plt.ylabel("Relative magnitude / arb.")
plt.savefig("spectrum.png")
plt.grid(True)
plt.show()
