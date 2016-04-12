import math as ma
import matplotlib.pyplot as plt
g=9.8
B=0.0001
print'the number of the pair of parameter'
a=input()
print'input dt'
dt=input()
def cannonshell(v,theta):
	print"a new pair of parameter"
	print"input the initial velocity (m)"
	v=input()
	print"input the initial angle    "
	theta=input()
	vy=[]
	vx=[]
	vy.append(v*ma.sin(ma.radians(theta)))
	vx.append(v*ma.cos(ma.radians(theta)))
	x=[]
	y=[]
	x.append(0)
	y.append(0.000001)
	for i in range(500000):
		if y[-1]>=0:
			fvy=vy[i]-g*dt-B*ma.sqrt(vx[i]**2+vy[i]**2)*vy[i]*dt
			vy.append(fvy)
			fvx=vx[i]-B*ma.sqrt(vx[i]**2+vy[i]**2)*vx[i]*dt
			vx.append(fvx)
			fx=x[i]+vx[i]*dt
			x.append(fx)
			fy=y[i]+vy[i]*dt
			y.append(fy)
		else: 
			break
	print 'the range of the cannon is',x[-1],'m'
	print"                       "
	plt.plot(x,y,'r-',linewidth=1)
	plt.xlabel('x (m)')
	plt.ylabel('y (m)')
	plt.title('cannon shell')
for i in range (a):
	cannonshell('v','theta')
plt.text(0,4000,'with air drag')
plt.show()


