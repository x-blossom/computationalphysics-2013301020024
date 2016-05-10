from visual import*
scene.title = "Lorenz_model"
ball= sphere(pos=(1,0,0),radius=0.01, color=color.yellow)
X0 = arrow(pos=(0,0,0), axis=(50,0,0), color=color.cyan, shaftwidth=0.005)
Y0 = arrow(pos=(0,0,0), axis=(0,50,0), color=color.red, shaftwidth=0.005)
Z0 = arrow(pos=(0,0,0), axis=(0,0,50), color=color.yellow,shaftwidth=0.005)
xlabel=label(text='x axis',pos=(50,0,0),color=color.green,yoffset=-100,opacity=0)
ylabel=label(text='y axis',pos=(0,50,0),color=color.green,zoffset=-100,opacity=0)
zlabel=label(text='z axis',pos=(0,0,50),color=color.green,xoffset=-100,opacity=0)
de=10
b=8./3
dt=0.0001

x=[]
y=[]
z=[]
t=[]
x.append(1)
y.append(0)
z.append(0)
t.append(0)

ball.trail = curve(color=ball.color,interval=1,retain=100)

for i in range (500000):
        rate=100
        r=25
        x_app=x[i]+de*(y[i]-x[i])*dt
        y_app=y[i]+(-x[i]*z[i]+r*x[i]-y[i])*dt
        z_app=z[i]+(x[i]*y[i]-b*z[i])*dt
        t_app=t[i]+dt
        ball.x=x_app
        x.append(x_app)
        ball.y=y_app
        y.append(y_app)
        ball.z=z_app
        z.append(z_app)
        t.append(t_app)
        ball.trail.append(pos = ball.pos)




