from visual import*
import math as ma
scene.title = "two_body"
ball1= sphere(pos=(0,0,0),radius=0.3, color=color.yellow)
ball2= sphere(pos=(1,1,0),radius=0.1, color=color.red)
ball1.trail = curve(color=ball1.color,interval=1,retain=100)
ball2.trail = curve(color=ball2.color,interval=1,retain=100)
rate(1)
dt=0.002
G1=0.0004*ma.pi**2
G2=4*ma.pi**2
def two_body(x1_ini,y1_ini,vx1_ini,vy1_ini,x2_ini,y2_ini,vx2_ini,vy2_ini):
    x1=[]
    y1=[]
    r=[]
    vx1=[]
    vy1=[]
    x2=[]
    y2=[]
    vx2=[]
    vy2=[]
    x1.append(x1_ini)
    y1.append(y1_ini)
    vx1.append(vx1_ini)
    vy1.append(vy1_ini)
    x2.append(x2_ini)
    y2.append(y2_ini)
    vx2.append(vx2_ini)
    vy2.append(vy2_ini)
    for i in range (10000):
        r.append(((x1[i]-x2[i])**2+(y1[i]-y2[i])**2)**0.5)
        vx1_app=vx1[i]-G1*(x1[i]-x2[i])/((r[i])**3)*dt
        vx1.append(vx1_app)
        x1_app=x1[i]+vx1[i+1]*dt
        x1.append(x1_app)
        vy1_app=vy1[i]-G1*(y1[i]-y2[i])/((r[i])**3)*dt
        vy1.append(vy1_app)
        y1_app=y1[i]+vy1[i+1]*dt
        y1.append(y1_app)
        vx2_app=vx2[i]-G2*(x2[i]-x1[i])/((r[i])**3)*dt
        vx2.append(vx2_app)
        x2_app=x2[i]+vx2[i+1]*dt
        x2.append(x2_app)
        vy2_app=vy2[i]-G2*(y2[i]-y1[i])/((r[i])**3)*dt
        vy2.append(vy2_app)
        y2_app=y2[i]+vy2[i+1]*dt
        y2.append(y2_app)
        ball1.x=x1_app
        ball1.y=y1_app
        ball2.x=x2_app
        ball2.y=y2_app
        ball1.trail.append(pos = ball1.pos)
        ball2.trail.append(pos = ball2.pos)
two_body(0,0,0,0,1,1,2*ma.pi,0)
	
