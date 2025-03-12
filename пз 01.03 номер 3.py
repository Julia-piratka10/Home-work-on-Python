import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3]
ay = [25, 17, 29]
by = [2, 13, 30]
cy = [10, 20, 25]
dy = [15, 28, 27]
y = [ay, by, cy, dy]
plt.figure(figsize=(12,6))
plt.stackplot(x, y)
plt.xlabel('Ось х')
plt.ylabel('Ось у')

plt.show()