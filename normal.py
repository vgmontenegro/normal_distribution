from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 0.01)

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()

plt.style.use('fivethirtyeight')
alpha = 0.8

ax.plot(x, norm.pdf(x, 0, 1.0), color='red', alpha=alpha, label='μ: 0, σ: 1.0')
ax.plot(x, norm.pdf(x, 0, 1.5), color='blue', alpha=alpha, label='μ: 0, σ: 1.5')
ax.plot(x, norm.pdf(x, 0, 2.0), color='green', alpha=alpha, label='μ: 0, σ: 2.0')
ax.set_xlim([-5, 5])
ax.legend()
plt.show()

