import matplotlib.pyplot as plt
N=[]
t=[]
dt=0.1
N.append(1500)
t.append(0)
print"input a"
a=input()
print"input b"
b=input()
for i in range(14):
	N_app=N[i]+(a*N[i]-b*N[i]**2)*dt
	N.append(N_app)
	t.append(dt+t[i])
	print N_app
plt.plot(t,N,'r--',label='a=10,b=0.01,N(0)=1500')
plt.xlabel('t')
plt.ylabel('N')
plt.legend(loc='upper right')
plt.show()
