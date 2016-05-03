a=[]
def nu(x):
	for j in range(10):
		a.append(x+j/10.)
for i in range(30,50):
        nu(i)
import math as ma
import matplotlib.pyplot as plt
g=9.8
B=0.00004
#print'the number of the pair of parameter'
#a=input()
print'input dt'
dt=input()
z=[]
def cannonshell(theta):
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
				co=(1-0.0065*y[-1]/288)^2.5
				B=B*co
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

cannonshell('theta')
print 'when velocity is 500m/s,','the optimum angle is 44.8, the max range of the cannon is',max(z),'m'
def can1(theta):
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
	plt.plot(x,y,'b-',linewidth=1,label='the optimum angle is 44.8')
	plt.xlabel('x (m)')
	plt.ylabel('y (m)')
	plt.title('cannon shell')
def can2(theta):
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
	plt.plot(x,y,'r-',linewidth=1,)
	plt.xlabel('x (m)')
	plt.ylabel('y (m)')
	plt.title('cannon shell')
can1(44.8)
can2(35)
can2(55)
can2(40)
can2(50)
plt.text(0,5000,'no air drag')
plt.legend(loc='upper right')
plt.show()
