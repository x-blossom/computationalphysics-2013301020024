import matplotlib.pyplot as plt
import math as ma
rate_Me=1
rate_Mj=1
dt=0.0001
px=0.083300
py=0.127889
def S_J_E(x1,y1,vx1,vy1,x2,y2,vx2,vy2,x3,y3,vx3,vy3):
	ve_x=[]
	ve_y=[]
	xe=[]
	ye=[]
	vj_x=[]
	vj_y=[]
	xj=[]
	yj=[]
	vr_x=[]
	vr_y=[]
	xr=[]
	yr=[]
	xe.append(x1)
	ye.append(y1)
	xj.append(x2)
	yj.append(y2)
	xr.append(x3)
	yr.append(y3)
	ve_x.append(vx1)
	ve_y.append(vy1)
	vj_x.append(vx2)
	vj_y.append(vy2)
	vr_x.append(vx3)
	vr_y.append(vy3)	
	for i in range(80000):
		r_e=(xe[i]**2+ye[i]**2)**0.5
		r_j=(xj[i]**2+yj[i]**2)**0.5
		r_r=(xr[i]**2+yr[i]**2)**0.5
		r_ej=((xe[i]-xj[i])**2+(ye[i]-yj[i])**2)**0.5
		r_er=((xe[i]-xr[i])**2+(ye[i]-yr[i])**2)**0.5
		r_jr=((xr[i]-xj[i])**2+(yr[i]-yj[i])**2)**0.5
		vex=ve_x[i]-(xe[i]-xr[i])/r_er**3*dt-rate_Mj*(xe[i]-xj[i])/r_ej**3*dt
		vey=ve_y[i]-(ye[i]-yr[i])/r_er**3*dt-rate_Mj*(ye[i]-yj[i])/r_ej**3*dt
		ve_x.append(vex)
		ve_y.append(vey)
		vjx=vj_x[i]-(xj[i]-xr[i])/r_jr**3*dt-rate_Me*(xj[i]-xe[i])/r_ej**3*dt
		vjy=vj_y[i]-(yj[i]-yr[i])/r_jr**3*dt-rate_Me*(yj[i]-ye[i])/r_ej**3*dt
		vj_x.append(vjx)
		vj_y.append(vjy)
		vrx=vr_x[i]-rate_Me*(xr[i]-xe[i])/r_er**3*dt-rate_Mj*(xr[i]-xj[i])/r_jr**3*dt
		vry=vr_y[i]-rate_Me*(yr[i]-ye[i])/r_er**3*dt-rate_Mj*(yr[i]-yj[i])/r_jr**3*dt
		vr_x.append(vrx)
		vr_y.append(vry)
		xe_app=xe[i]+ve_x[i+1]*dt
		ye_app=ye[i]+ve_y[i+1]*dt
		xj_app=xj[i]+vj_x[i+1]*dt
		yj_app=yj[i]+vj_y[i+1]*dt
		xr_app=xr[i]+vr_x[i+1]*dt
		yr_app=yr[i]+vr_y[i+1]*dt
		xe.append(xe_app)
		ye.append(ye_app)
		xj.append(xj_app)
		yj.append(yj_app)
		xr.append(xr_app)
		yr.append(yr_app)
	plt.plot(xe,ye,'r-',label='p1')
	plt.plot(xj,yj,'b--',label='p2')
	plt.plot(xr,yr,'-.',label='p3')
	
S_J_E(1,0,px,py,-1,0,px,py,0,0,-2*px,-2*py)
plt.legend(loc='upper left')
plt.xlabel('x ')
plt.ylabel('y ')
plt.show()
