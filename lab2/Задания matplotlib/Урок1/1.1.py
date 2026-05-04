
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
y1 = x
y2 = [i**2 for i in x]

plt.title('Зависимости: y1 = x, y2 = x^2')
plt.xlabel('x', color='deeppink')
plt.ylabel('y1,y2', color='deeppink')
plt.grid()
plt.plot(x,  y1, color='pink' )
plt.plot(x, y2, color='deeppink')

plt.show()