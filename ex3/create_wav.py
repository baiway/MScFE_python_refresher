import numpy as np
import wave

# Load data
t, signal = np.loadtxt("audio.csv", delimiter=",", skiprows=1, unpack=True)
sample_rate = 44100      # hertz

# Convert to (little-endian) 16 bit integers.
audio = (signal * (2 ** 15 - 1)).astype("<h")

# Save as WAV file
with wave.open("sound.wav", "w") as file:
    file.setnchannels(1) # 1 channel
    file.setsampwidth(2) # 2 bytes per sample
    file.setframerate(sample_rate)
    file.writeframes(audio.tobytes())

# Open using any compatible media player. One of the commands below may work for you.
# If not, install VLC Media Player (https://www.videolan.org/) and open in the usual way
#   macOS: `open sound.wav`
#   Linux: `xdg-open sound.wav`
#   Windows PowerShell: `Start-Process "sound.wav"`
