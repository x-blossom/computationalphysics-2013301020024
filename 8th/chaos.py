g=9.8
l=9.8
dt=0.04
q=0.5
F=1.2
omi=2/3
import math as ma
import matplotlib.pyplot as plt
omiga=[]
t=[]
theta=[]
t.append(0)
omiga.append(0)
def THE(a):
	theta.append(a)

THE(0.2)
for i in range(500):
	w_app=omiga[i]-((g/l)*ma.sin(theta[i])-q*omiga[i]+F*ma.sin(omi*t[i]))*dt
	omiga.append(w_app)
	s_app=theta[i]+omiga[i+1]*dt
	t_app=t[i]+dt
	t.append(t_app)		
	theta.append(s_app)
	
	
	if theta[-1]<-ma.pi:
		b=theta[-1]+2*ma.pi
		theta.remove(theta[-1])
		theta.append(b)
	else:
		continue


	if theta[-1]>ma.pi:
		a=theta[-1]-2*ma.pi
		theta.remove(theta[-1])
		theta.append(a)
		
	else:
		continue	
plt.ylabel('radians(rad)')
plt.xlabel('time(s)')
plt.plot(t,theta,'b-',label=r'$\theta$(initial) = 0.2 digress')
plt.show()


