de=10
b=8./3
dt=0.0001

x=[]
y=[]
z=[]
t=[]
x.append(1)
y.append(0)
z.append(0)
t.append(0)

def r(pa):
	for i in range (500000):

		r=pa
		x_app=x[i]+de*(y[i]-x[i])*dt
		y_app=y[i]+(-x[i]*z[i]+r*x[i]-y[i])*dt
		z_app=z[i]+(x[i]*y[i]-b*z[i])*dt
		t_app=t[i]+dt
		x.append(x_app)
		y.append(y_app)
		z.append(z_app)
		t.append(t_app)

import matplotlib.pyplot as plt
r(25)
plt.plot(t,z,'r--',label='r=25')

x=[]
y=[]
z=[]
t=[]
x.append(1)
y.append(0)
z.append(0)
t.append(0)
r(10)
plt.plot(t,z,'b--',label='r=10')

x=[]
y=[]
z=[]
t=[]
x.append(1)
y.append(0)
z.append(0)
t.append(0)
r(5)
plt.plot(t,z,'y--',label='r=5')
plt.text(30,42,r'$\delta$ = 10  b= 8/3 ')
plt.ylabel('z')
plt.xlabel('time(s)')
plt.legend(loc='upper right')
plt.show()

