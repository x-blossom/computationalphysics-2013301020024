import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
a=np.array([[-1.,-0.67,-0.33,0,0.33,0.67,1.],[-1.,0.,0.,0.,0.,0.,1.],[-1.,0.,0.,0.,0.,0.,1.],[-1.,0.,0.,0.,0.,0.,1.],[-1.,0.,0.,0.,0.,0.,1.],[-1.,0.,0.,0.,0.,0.,1.],[-1.,-0.67,-0.33,0,0.33,0.67,1.]])
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-1, 1, 0.5)
Y = np.arange(-1, 1, 0.5)
X, Y = np.meshgrid(X, Y)
Z=([[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3]])
print Z
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.show()

