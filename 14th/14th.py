import math as ma
import matplotlib.pyplot as plt

dt=1./30000
dx=0.01
c=300
x=[]
for i in range(100):
	x.append(i*dx)

def wave(r):
	for i in range(1,100):
		tmp=ma.e**(-1000*(x[i]-0.3)**2)
		li[1].append(tmp)
	li[0].append(0)
	for i in range(1,99):
		li_app=2*(1-r**2)*li[1][i]-li[0][i]+r**2*(li[1][i+1]-li[1][i-1])
		li[0].append(li[1][i+1])
		li[1][i]=li_app
		li[2].append(li_app)
	li[2].append(0)

li=[([]*100) for i in range (1,4)]
li[0].append(0)
li[1].append(0)
li[2].append(0)
wave(0.)
plt.plot(x,li[2],'r',label='r=0')

li=[([]*100) for i in range (1,4)]
li[0].append(0)
li[1].append(0)
li[2].append(0)
wave(0.2)
plt.plot(x,li[2],'b',label='r=0.2')

li=[([]*100) for i in range (1,4)]
li[0].append(0)
li[1].append(0)
li[2].append(0)
wave(0.5)
plt.plot(x,li[2],'y',label='r=0.5')

li=[([]*100) for i in range (1,4)]
li[0].append(0)
li[1].append(0)
li[2].append(0)
wave(0.7)
plt.plot(x,li[2],'b--',label='r=0.7')

li=[([]*100) for i in range (1,4)]
li[0].append(0)
li[1].append(0)
li[2].append(0)
wave(1)
plt.plot(x,li[2],'y--',label='r=1')

plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right')
plt.show()
