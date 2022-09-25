import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import PIL.Image

x = y = np.linspace(-10, 10,150)
X,Y = np.meshgrid(x,y)
Z = np.cos(X)*np.cos(Y)*np.exp(-(Y/5)**2-(X/5)**2)
fig, ax = plt.subplots(figsize=(7,7))
ax.set_xlabel(r"$x$", fontsize = 15)
ax.set_ylabel(r"$y$", fontsize = 15)
norm = mpl.colors.Normalize(-abs(Z).max(), abs(Z).max())
p = ax.pcolor(X,Y,Z,norm=norm, cmap = 'Purples')

plt.show()

