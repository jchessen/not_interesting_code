import matplotlib.pyplot as plt
import numpy as np

# Load the MCMC samples from the CSV
samples = np.loadtxt('moyal_samples.csv')

# Plot the histogram of the samples
plt.hist(samples, bins=50, density=True, alpha=0.6, color='g', label='MCMC Samples')

# Plot the true Moyal PDF for comparison (if desired)
x = np.linspace(min(samples), max(samples), 1000)
true_pdf = 1 / np.sqrt(2 * np.pi) * np.exp(-0.5 * (x + np.exp(-x)))
plt.plot(x, true_pdf, label='True Moyal PDF', color='r')

plt.title('MCMC Sampling from the Moyal Distribution')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()
plt.show()
