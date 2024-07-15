import numpy as np
import matplotlib.pyplot as plt

# Load data
reaction_times = np.loadtxt("reaction_times.txt")

# Calculate mean and standard deviation
mean = np.mean(reaction_times)
std = np.std(reaction_times)

# Form output string
output_str = f"avg. reaction time = ({mean:.2f} +/- {std:.2f}) seconds"

# Print output string and write to file
print(output_str)
with open("descriptive_statistics.txt", "w") as file:
    file.write(output_str)

# Plot histogram
plt.figure(figsize=(10,6))
plt.hist(reaction_times, bins=30, edgecolor="black", alpha=0.7, color="skyblue")
plt.xlabel("Reaction time / s")
plt.ylabel("Frequency")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("histogram.png")
plt.show()
