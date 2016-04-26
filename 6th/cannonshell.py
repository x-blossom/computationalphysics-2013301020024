a=[]
def nu(x):
	for j in range(10):
		a.append(x+j/2.)
for i in range(30,50):
        nu(i)
import math as ma
import matplotlib.pyplot as plt
g=9.8
B=0.0001
#print'the number of the pair of parameter'
#a=input()
print'input dt'
dt=input()
z=[]
def cannonshell(theta):
#	print"a new pair of parameter"
#	print"input the initial velocity (m)"
#	v=input()
#	print"input the initial angle    "
#	theta=input()
	for i in a:
		theta=float(i)
		v=500		
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
		print 'theta =',theta,'the range of the cannon is',x[-1],'m'
		print"                        "
		z.append(x[-1])
		plt.plot(x,y,'r-',linewidth=1)
		plt.xlabel('x (m)')
		plt.ylabel('y (m)')
		plt.title('cannon shell')
#for i in range (a):
#	cannonshell('v','theta')
cannonshell('theta')
print 'when velocity is 500m/s,','the max range of the cannon is',max(z),'m'
plt.text(0,4000,'with air drag')
plt.show()
