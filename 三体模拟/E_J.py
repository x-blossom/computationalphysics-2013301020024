import matplotlib.pyplot as plt
import math as ma
rate_Me=3.3*10**-7
rate_Mj=9.5*10**-4
dt=0.01
def J_E(x1,y1,vx1,vy1,x2,y2,vx2,vy2):
	ve_x=[]
	ve_y=[]
	xe=[]
	ye=[]
	vj_x=[]
	vj_y=[]
	xj=[]
	yj=[]
	xe.append(x1)
	ye.append(y1)
	xj.append(x2)
	yj.append(y2)
	ve_x.append(vx1)
	ve_y.append(vy1)
	vj_x.append(vx2)
	vj_y.append(vy2)	
	for i in range(3000):
		r_e=(xe[i]**2+ye[i]**2)**0.5
		r_j=(xj[i]**2+yj[i]**2)**0.5
		r_ej=((xe[i]-xj[i])**2+(ye[i]-yj[i])**2)**0.5
		vex=ve_x[i]-4*ma.pi**2*xe[i]/r_e**3*dt-4*ma.pi**2*rate_Mj*(xe[i]-xj[i])/r_ej**3*dt
		vey=ve_y[i]-4*ma.pi**2*ye[i]/r_e**3*dt-4*ma.pi**2*rate_Mj*(ye[i]-yj[i])/r_ej**3*dt
		ve_x.append(vex)
		ve_y.append(vey)
		vjx=vj_x[i]-4*ma.pi**2*xj[i]/r_j**3*dt-4*ma.pi**2*rate_Me*(xj[i]-xe[i])/r_ej**3*dt
		vjy=vj_y[i]-4*ma.pi**2*yj[i]/r_j**3*dt-4*ma.pi**2*rate_Me*(yj[i]-ye[i])/r_ej**3*dt
		vj_x.append(vjx)
		vj_y.append(vjy)
		xe_app=xe[i]+ve_x[i+1]*dt
		ye_app=ye[i]+ve_y[i+1]*dt
		xj_app=xj[i]+vj_x[i+1]*dt
		yj_app=yj[i]+vj_y[i+1]*dt
		xe.append(xe_app)
		ye.append(ye_app)
		xj.append(xj_app)
		yj.append(yj_app)
	plt.plot(xe,ye,'r--',label='earth')
	plt.plot(xj,yj,'b--',label='jupiter')
	
J_E(1,0,0,2*ma.pi,5.2,0,0,0.86*ma.pi)
plt.legend(loc='upper right')
plt.text(-5,5,'Mass of Jupiter = Mj')
plt.xlabel('x /AU')
plt.ylabel('y /AU')
plt.show()
