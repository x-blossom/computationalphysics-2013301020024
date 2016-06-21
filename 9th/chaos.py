g=9.8
l=9.8
dt=0.04
q=0.5
omi=2./3
import math as ma
import matplotlib.pyplot as plt

def fun(F):
	for i in range(250):
		w_app=omiga[i]-((g/l)*ma.sin(theta[i])-q*omiga[i]+F*ma.sin(omi*t[i]))*dt
		omiga.append(w_app)
		s_app=theta[i]+omiga[i+1]*dt
		print s_app	
		if s_app>ma.pi:
			s_app=s_app-2*ma.pi
		elif s_app<-ma.pi:
			s_app=s_app+2*ma.pi
		print '        ',s_app
		theta.append(s_app)
		t_app=t[i]+dt
		t.append(t_app)
		

		
omiga=[]
t=[]
theta=[]
t.append(0)
omiga.append(0)
theta.append(0.2)
fun(0)
plt.plot(t,theta,'r--',label='F=0')

omiga=[]
t=[]
theta=[]
t.append(0)
omiga.append(0)
theta.append(0.2)
fun(0.5)
plt.plot(t,theta,'b--',label='F=0.5')

omiga=[]
t=[]
theta=[]
t.append(0)
omiga.append(0)
theta.append(0.2)
fun(1.2)
plt.plot(t,theta,'y--',label='F=1.2')

plt.ylabel('radians(rad)')
plt.xlabel('time(s)')
plt.legend(loc='upper right')
plt.show()


