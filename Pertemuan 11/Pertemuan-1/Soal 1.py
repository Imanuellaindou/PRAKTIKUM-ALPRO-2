import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10)
y = np.sin(x)
z = np.cos(x)

plt.plot(x, y, 'b', label='Sin')
plt.plot(x, z, 'r', label='Cos')

plt.xlabel('x')
plt.ylabel('Nilai')
plt.title('Plotting Demonstrasi')
plt.legend()
plt.grid(True)

plt.show()