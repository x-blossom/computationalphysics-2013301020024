g=9.8
l=1
dt=0.02
omiga=[]
t=[]
theta=[]
t.append(0)
omiga.append(0)
theta.append(0.3)
for i in range(500):
	w_app=omiga[i]-(g/l)*theta[i]*dt
	omiga.append(w_app)
	s_app=theta[i]+omiga[i+1]*dt
	t_app=t[i]+dt
	
	theta.append(s_app)
	t.append(t_app)
	print omiga[-1],theta[-1]
import matplotlib.pyplot as plt
plt.plot(t,theta,'r--')
plt.ylabel('radians(rad)')
plt.xlabel('time(s)')
plt.text(0.2,0.7,'Euler_cormer method')
plt.text(0.2,0.6,'length=1 m,time step=0.02 s,inital angle=0.3 rad')

plt.show()
