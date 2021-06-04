import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,1)
y = x**2 - 2*x + 1
plt.title('Grafico função x^2 - 2*x +1')
plt.xlabel('Eixo de X')
plt.ylabel('Eixo de Y')
plt.plot(x,y)
plt.show()