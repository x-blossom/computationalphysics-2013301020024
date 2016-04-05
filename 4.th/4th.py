print"input a"
a=input()
print"input b"
b=input()
def A(v,t):
	dvdt=a-b*v
	return dvdt

v0=233
import numpy as np
t=np.linspace(0,100)
from scipy.integrate import odeint
sol=odeint(A,v0,t)
print sol
import matplotlib.pyplot as plt
plt.xlabel('time')
plt.ylabel('velocity')
plt.plot(t,sol,"r--")
plt.title('velocity&time')
plt.show()
