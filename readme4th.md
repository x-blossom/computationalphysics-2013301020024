#**readme**
        第四次作业

---



 - **简述**
通过scripy，numpy内置函数，运用欧拉迭代法解决常微分方程。然后通过matplotlib对数据进行处理，做成图形使其更为直观化。
 - **详细说明**
def A(v,t): 
dvdt=50-v 
return dvdt 
这三行是定义一个名为A的函数，并进行迭代运算
A：dv/dt=50-v，是一个非齐次一阶常微分方程

v0=233 
import numpy as np 
t=np.linspace(0,100) 
这三行是设置初值以及迭代次数，迭代次数通过numpy内置函数定义引入

from scipy.integrate import odeint 
sol=odeint(A,v0,t) 
print sol
这三行是通过scipy内置函数odeint，对前面定义的函数A（在已设置初值与迭代次数下进行运算），最后输出结果。
import matplotlib.pyplot as plt 
plt.xlabel('time') 
plt.ylabel('velocity') 
plt.plot(t,sol,"r--") 
plt.title('velocity&time') 
plt.show() 
上面六行是对matplotlib的画图设置及表达，分别是
设置x轴表示时间
设置y轴表示速度
设置时间速度一一对应的图像及绘图的颜色与格式
设置绘图标题
显示图像

 - **总结**

 - 学会定义函数
 - 掌握scipy与numpy内置函数的引入与使用
 - 能够使用matplotlib进行绘图处理并能设置参数

 - **致谢**
 - 感谢百度，感谢不知名的网络上的内容。

 
