g=9.8
l=1
dt=0.01
import math as ma
import matplotlib.pyplot as plt
omiga=[]
t=[]
theta=[]
t.append(0)
omiga.append(0)
def THE(a):
	theta.append(a)

THE(0.1745)
for i in range(500):
	w_app=omiga[i]-(g/l)*ma.sin(theta[i])*dt
	omiga.append(w_app)
	s_app=theta[i]+omiga[i+1]*dt
	t_app=t[i]+dt		
	theta.append(s_app)
	t.append(t_app)
	if abs(float(theta[-1])-float(theta[0]))<0.0001:
		print t[-1]
	else:
		continue
	print 'over'
plt.ylabel('radians(rad)')
plt.xlabel('time(s)')
plt.plot(t,theta,'b-',label=r'$\theta$(initial) = 20 degress')

omiga=[]
t=[]
theta=[]
t.append(0)
omiga.append(0)
THE(0.5236)
for i in range(500):
	w_app=omiga[i]-(g/l)*ma.sin(theta[i])*dt
	omiga.append(w_app)
	s_app=theta[i]+omiga[i+1]*dt
	t_app=t[i]+dt		
	theta.append(s_app)
	t.append(t_app)
	if abs(float(theta[-1])-float(theta[0]))<0.0001:
		print t[-1]
	else:
		continue
	print 'over1'
plt.ylabel('radians(rad)')
plt.xlabel('time(s)')
plt.plot(t,theta,'r-',label=r'$\theta$(initial) = 30 degress')

omiga=[]
t=[]
theta=[]
t.append(0)
omiga.append(0)
THE(1.0472)
for i in range(500):
	w_app=omiga[i]-(g/l)*ma.sin(theta[i])*dt
	omiga.append(w_app)
	s_app=theta[i]+omiga[i+1]*dt
	t_app=t[i]+dt		
	theta.append(s_app)
	t.append(t_app)
	if abs(float(theta[-1])-float(theta[0]))<0.0001:
		print t[-1]
	else:
		continue
	print 'over2'
plt.ylabel('radians(rad)')
plt.xlabel('time(s)')
plt.plot(t,theta,'y-',label=r'$\theta$(initial) = 60 degress')

omiga=[]
t=[]
theta=[]
t.append(0)
omiga.append(0)
THE(1.3962)
for i in range(500):
	w_app=omiga[i]-(g/l)*ma.sin(theta[i])*dt
	omiga.append(w_app)
	s_app=theta[i]+omiga[i+1]*dt
	t_app=t[i]+dt		
	theta.append(s_app)
	t.append(t_app)
	if abs(float(theta[-1])-float(theta[0]))<0.0005:
		print t[-1]
	else:
		continue
	print 'over3'
plt.ylabel('radians(rad)')
plt.xlabel('time(s)')
plt.plot(t,theta,'b--',label=r'$\theta$(initial) = 80 degress')
plt.legend(loc='upper right')
plt.show()
