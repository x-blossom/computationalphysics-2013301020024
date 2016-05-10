from visual import*
scene.title = "the baseball"
box=box(pos=(0,0,0),length=50, height=0.1, width=50,color=color.white)
ball = sphere(pos=(0,4,0),radius=0.8, color=color.red)
X0 = arrow(pos=(0,0,0), axis=(30,0,0), color=color.cyan, shaftwidth=0.005)
Y0 = arrow(pos=(0,0,0), axis=(0,10,0), color=color.red, shaftwidth=0.005)
Z0 = arrow(pos=(0,0,0), axis=(0,0,10), color=color.yellow,shaftwidth=0.005)
xlabel=label(text='x axis',pos=(30,0,0),color=color.green,yoffset=-100,opacity=0)
ylabel=label(text='y axis',pos=(0,10,0),color=color.green,zoffset=-100,opacity=0)
zlabel=label(text='z axis',pos=(0,0,10),color=color.green,xoffset=-100,opacity=0)


g=9.8
B=0.0039
S=0.00041
dt=0.01
def baseball(v_x,v_y,v_z,w_x,w_y,w_z):
    x=[]
    y=[]
    z=[]
    v=[]
    vx=[]
    vy=[]
    vz=[]
    x.append(0)
    y.append(0)
    z.append(0)
    vx.append(v_x)
    vy.append(v_y)
    vz.append(v_z)
    wx=w_x
    wy=w_y
    wz=w_z
    for i in range (50000):
        rate=100
        v.append(((vx[i])**2+(vy[i])**2+(vz[i])**2)**0.5)
        vx_app=vx[i]-B*vx[i]*v[i]*dt+S*(wy*vz[i]-wz*vy[i])*dt
        vx.append(vx_app)
        x_app=x[i]+vx[i]*dt
        x.append(x_app)
        ball.x=x_app
        y_app=y[i]+vy[i]*dt
        y.append(y_app)
        vy_app=vy[i]-g*dt-B*vy[i]*v[i]*dt+S*(wz*vx[i]-wx*vz[i])*dt
        vy.append(vy_app)
        ball.y=y_app
        z_app=z[i]+vz[i]*dt
        ball.z=z_app
        vz_app=vz[i]-B*vz[i]*v[i]*dt+S*(wx*vy[i]-wy*vx[i])*dt	
        z.append(z_app)
        vz.append(vz_app)
        ball.trail.append(pos = ball.pos)
        print x[-1],y[-1],z[-1]
        if y[-1]<0:
        	break
        else:
        	continue
ball.trail = curve(color = ball.color,interval=10)
#text1=text(pos=(50,50,50), string='---2000 rpm', color=color.red, depth=0.3, justify='center')
baseball(10,10,0,2000,2000,2000)
ball.trail = curve(color = color.blue)
#text2=text(pos=(50,50,45), string='---200 rpm', color=color.blue, depth=0.3, justify='center')
baseball(10,10,0,200,200,200)
ball.trail = curve(color = color.yellow)
#text3=text(pos=(50,50,40), string='---20 rpm', color=color.yellow, depth=0.3, justify='center')
baseball(10,10,0,20,20,20)
ball.trail = curve(color = color.orange)
#text4=text(pos=(50,50,35), string='---0 rpm', color=color.orange, depth=0.3, justify='center')
baseball(10,10,0,0,0,0)


