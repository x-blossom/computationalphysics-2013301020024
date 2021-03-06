
g=9.8
l=1
dt=0.02
F=0.2
omi=2.0
import math as ma
import matplotlib.pyplot as plt
omiga=[]
t=[]
theta=[]
t.append(0)
omiga.append(0)
theta.append(0.2)
def LIN(x): 
	for i in range(500):
		w_app=omiga[i]-((g/l)*theta[i]+x*omiga[i]-F*ma.sin(omi*t[i]))*dt
		omiga.append(w_app)
		s_app=theta[i]+omiga[i+1]*dt
		t_app=t[i]+dt
		
		theta.append(s_app)
		t.append(t_app)
		print omiga[-1],theta[-1]
p1=plt.subplot(2,1,1)
p2=plt.subplot(2,1,2)
LIN(1.0)
p1.plot(t,theta,'r--')
p1.text(1,0.22,'Euler_cormer method      driven pendulum')
p1.text(3,0.15,r'$\Omega$ = 2.0  F= 0.2  q= 1.0')
omiga=[]
t=[]
theta=[]
t.append(0)
omiga.append(0)
theta.append(0.2)
LIN(0)
p2.plot(t,theta,'b--')
p2.text(1,0.22,'Euler_cormer method      driven pendulum')
p2.text(3,0.15,r'$\Omega$ = 2.0  F= 0.2  q= 0.0')
p2.set_ylabel('radians(rad)')
p2.set_xlabel('time(s)')
plt.show()
