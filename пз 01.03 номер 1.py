import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,10)
y1 = x
y2 = 2*x
y3 = 3*x
y4 = x**2
y5 = 2*(x**2)
plt.figure(figsize=(10,6))
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.plot(x, y5)
plt.xlabel('Ось x')
plt.ylabel('Ось y')
plt.show()