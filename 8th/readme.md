#第七次作业---单摆运动探究
-------------



2013301020024 谢章权

   
---
 - ##摘要

    　　通过使用Euler,Euler-cromer近似方法来模拟单摆的运动行为，包括线性单摆与非线性单摆。

 - ##背景内容
    　　１．对于单摆，最简单的模型即为不考虑空气阻力等外力，仅考虑重力的小角近似线性常微分运动方程，即为
            $$\frac{d^2\theta}{dt^2}=-{g\over l}\theta$$
　　　　通过选取适当变量  $\omega$  使得
             $$\frac{d\theta}{dt}=\omega$$
　　　　则可运用前面所学常微分方程求解知识进行求解。

    　　２．若考虑外力（含驱动力），则单摆运动方程为
            $$\frac{d^2\theta}{dt^2}=-{g\over l}\theta-q\frac{d\theta}{dt}+F_Dsin(\Omega_Dt)$$
   　　３．如果是非线性单摆（不考虑小角近似），则
            $$\frac{d^2\theta}{dt^2}=-{g\over l}sin\theta$$

     
 - ##正文
###　　　１．对于线性仅含重力情形模拟
## 　　 　　Euler-calculate
$$\omega_{i+1}=\omega_{i}-{g\over l}\theta{\Delta}t$$
$$\theta_{i+1}=\theta_{i}-\omega_i{\Delta}t$$
$$t_{i+1}=t_{i}+{\Delta}t$$
![Euler模拟](https://github.com/x-blossom/computationalphysics-2013301020024/blob/master/7th/EULER-non%20force.png)
## 　　 　　Euler-cromer-calculate
$$\omega_{i+1}=\omega_{i}-{g\over l}\theta_i{\Delta}t$$
$$\theta_{i+1}=\theta_{i}-\omega_{i+1}{\Delta}t$$
$$t_{i+1}=t_{i}+{\Delta}t$$
![Euler-cromer模拟](https://github.com/x-blossom/computationalphysics-2013301020024/blob/master/7th/Euler_cromer-non%20force.png)
　　　　　其基本保持一个正弦波的运动状态
　　　　　可以看出，对于单摆的摆动模拟，Euler-cromer方法要优于Euler方法。
###　　　２．对于线性含外力情形模拟
## 　 　　　Euler-cromer-calculate
$$\omega_{i+1}=\omega_{i}-[{g\over l}sin\theta_i-q\omega_{i}+F_Dsin(\Omega_Dt)]{\Delta}t$$
$$\theta_{i+1}=\theta_{i}+\omega_{i+1}{\Delta}t$$
$$t_{i+1}=t_{i}+{\Delta}t$$
![Euler-cromer模拟](https://github.com/x-blossom/computationalphysics-2013301020024/blob/master/7th/driving-force.png)
　　　　可看出当q=0时，即使存在驱动力单摆依旧可以达到一种动态的类正弦稳定平衡。
　　　　q$\neq$0时（$q=1.0$,$\Omega=2.0$,$F_D=0.2$），单摆最终会趋于静止
###　　　3．对于非线性不含外力情形模拟
## 　 　　　Euler-cromer-calculate
$$\omega_{i+1}=\omega_{i}-{g\over l}sin\theta_i{\Delta}t$$
$$\theta_{i+1}=\theta_{i}-\omega_{i+1}{\Delta}t$$
$$t_{i+1}=t_{i}+{\Delta}t$$
![Euler-cromer模拟](https://github.com/x-blossom/computationalphysics-2013301020024/blob/master/7th/3.8.png)
　　　　可看出此时的振幅是与周期正有关的，具体数值对比如下
　　　　　　　　　　($g=9.8m/s^2,l=1m$)
| 初始振幅($\theta^°$)        | 周期T(s)   |
| --------   | -----:  |
|  20    |  2.01|
|   30     |  2.04   |
|    60     |   2.15    |
|    80     |    2.28   |


 - 总结
对于摆子的运动学模拟，Euler-cromer很明显是优于Euler法的。对于非线性单摆（不考虑小角近似），它的周期不再与我们通常所认为的周期公式$2\pi\sqrt{l\over g}$吻合,而是与初始释放位置（振幅）正相关。



