import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
a=np.array([[-1.,-0.67,-0.33,0,0.33,0.67,1.],[-1.,0.,0.,0.,0.,0.,1.],[-1.,0.,0.,0.,0.,0.,1.],[-1.,0.,0.,0.,0.,0.,1.],[-1.,0.,0.,0.,0.,0.,1.],[-1.,0.,0.,0.,0.,0.,1.],[-1.,-0.67,-0.33,0,0.33,0.67,1.]])
b=np.zeros((7,7))
def for_b():
	for i in range(1,6):
		for j in range(1,6):
			b[i,j]=0
	b[0,:]=b[6,:]=[-1.,-0.67,-0.33,0,0.33,0.67,1.]
	b[:,0]=[-1.,-1.,-1.,-1.,-1.,-1.,-1.]
	b[:,6]=[1.,1.,1.,1.,1.,1.,1.]
def for_ab():
	for i in range(0,7):
		t=b[i,:]
		a[i,:]=t

def test():
	for_b()
	for i in range(1,6):
		for j in range(1,6):
			b[i,j]=(a[i-1,j]+a[i+1,j]+a[i,j+1]+a[i,j-1])/4.
	#print b,'over'
	for_ab()
for i in range(10):
	test()
print a
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-1,1+1/3.,1/3.)
Y = np.arange(-1,1+1/3.,1/3.)
X, Y = np.meshgrid(X, Y)
ax.plot_surface(X, Y, a, rstride=1, cstride=1, cmap='rainbow')
plt.show()

