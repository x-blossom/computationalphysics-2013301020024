#第十二次作业---三体问题
-------------



2013301020024 谢章权

   
---
 - ##摘要

    　　研究太阳，地球，木星三者构成的行星三体问题。

 - ##背景内容
    　　１．当简化近似三体问题，即认为太阳所在位置为原点，且静止仅提供作用力而不参与运动时，地球的运动方程为
            $$\frac{d^2x_e}{dt^2}=-\frac{4\pi^2x_e}{r_e^3}-\frac{4\pi^2(M_j/M_s)(x_e-x_j)}{r_{ej}^3}$$
             $$\frac{d^2y_e}{dt^2}=-\frac{4\pi^2y_e}{r_e^3}-\frac{4\pi^2(M_j/M_s)(y_e-y_j)}{r_{ej}^3}$$
　　　　其中
             $$r_e=\sqrt{x_e^2+y_e^2}$$
             $$r_{ej}=\sqrt{(x_e-x_j)^2+(y_e-y_j)^2}$$

　　　　同理，木星的运动方程为
　　　　     $$\frac{d^2x_j}{dt^2}=-\frac{4\pi^2x_j}{r_j^3}-\frac{4\pi^2(M_e/M_s)(x_j-x_e)}{r_{ej}^3}$$
             $$\frac{d^2y_j}{dt^2}=-\frac{4\pi^2y_j}{r_j^3}-\frac{4\pi^2(M_e/M_s)(y_j-y_e)}{r_{ej}^3}$$
　　　　其中
             $$r_j=\sqrt{x_j^2+y_j^2}$$

    　　２．若考虑太阳的运动，即并非仅将太阳作为一个引力的提供者，则相应的地球运动方程为
             $$\frac{d^2x_e}{dt^2}=-\frac{4\pi^2（x_e-x_s)}{r_{es}^3}-\frac{4\pi^2(M_j/M_s)(x_e-x_j)}{r_{ej}^3}$$
             $$\frac{d^2y_e}{dt^2}=-\frac{4\pi^2(y_e-y_s)}{r_{es}^3}-\frac{4\pi^2(M_j/M_s)(y_e-y_j)}{r_{ej}^3}$$
　　　　其中
             $$r_{es}=\sqrt{(x_e-x_s)^2+(y_e-y_s)^2}$$
             $$r_{ej}=\sqrt{(x_e-x_j)^2+(y_e-y_j)^2}$$

　　　　同理，木星的运动方程为
　　　　     $$\frac{d^2x_j}{dt^2}=-\frac{4\pi^2（x_j-x_s)}{r_{js}^3}-\frac{4\pi^2(M_j/M_s)(x_j-x_e)}{r_{ej}^3}$$
             $$\frac{d^2y_j}{dt^2}=-\frac{4\pi^2(y_j-y_s)}{r_{js}^3}-\frac{4\pi^2(M_j/M_s)(y_j-y_e)}{r_{ej}^3}$$
　　　　其中
             $$r_{js}=\sqrt{(x_j-x_s)^2+(y_j-y_s)^2}$$
　　　　同理，太阳的运动方程为
　　　　$$\frac{d^2x_s}{dt^2}=-\frac{4\pi^2(M_e/M_s)（x_s-x_e)}{r_{e　　　　s}^3}-\frac{4\pi^2(M_j/M_s)(x_s-x_j)}{r_{js}^3}$$
             $$\frac{d^2y_s}{dt^2}=-\frac{4\pi^2(M_e/M_s)（y_s-y_e)}{r_{e　　　　s}^3}-\frac{4\pi^2(M_j/M_s)(y_s-y_j)}{r_{js}^3}$$

     
 - ##正文
###　　　１．对于近似三体模拟
 　　$$\frac{M_e}{M_s}=3\times 10^{-6}$$          　　$$\frac{M_j}{M_s}=9.5\times 10^{-4}$$
###故当木星取真实木星质量时，其模拟结果如下
![Mj][1]
###取10倍木星质量时，其模拟结果如下
![10Mj][2]
###取100倍木星质量时，其模拟结果如下
![100Mj][3]
###当取1000倍木星质量时，此时
$$\frac{1000M_j}{M_s}=0.95$$
　　　　即木星作用在地球上的引力与太阳作用在地球上的引力已在同一数量级，模拟结果如下
![1000Mj][4]
　　　　可看出此时地球轨道已经脱离稳定状态，随着时间推移，其将会逸出原来轨道。


###　　　２．对于真实三体轨道模拟

 　　此时太阳也在运动，应选取质心系为坐标系。

```seq
木星-->地球: 4.2AU

地球- ->太阳: 1AU

```
此时质心（假设初始三点在同一直线上，即为X轴）坐标为（x,0）
$$M_sx=M_e(1-x)+M_j(5.2-x)$$
因地球质量相对于太阳质量过小，故近似得
$$x=\frac{\frac{5.02M_j}{M_s}}{1+\frac{M_j}{M_s}}$$


###故当木星取真实木星质量时，其模拟结果如下
![Mj][5]
###取10倍木星质量时，其模拟结果如下
![10Mj][6]
###取100倍木星质量时，其模拟结果如下
![100Mj][7]
　　　　地球轨道模拟如下
![100Mj （oribt of earth）][8]
　　　　可看出此时地球轨道仍保持一定程度的稳定状态
###当取1000倍木星质量时，此时
![1000Mj][9]
　　　　可看出此时地球轨道脱离稳定状态,即将逸出原来轨道。而此时木星质量已近似等于太阳，此二者将进行典型的二体运动。

 - 总结
通过模拟可以看出，真实模拟相对于近似模拟是存在区别的。在木星质量远小于太阳质量时，两种模拟的区别微乎其微。但是当去木星质量为100Mj时，近似模拟仍近似为一个椭圆轨道，而真实模拟下地球的轨道已经快要控制不住了。。。木星质量取1000Mj时，真实模拟的地球已经要飞出去了。。。
综上，还好木星质量没那么大，嗯，活着真好。


  [1]: https://github.com/x-blossom/computationalphysics-2013301020024/blob/master/12th/1_e_j.png
  [2]: https://github.com/x-blossom/computationalphysics-2013301020024/blob/master/12th/10_e_j.png
  [3]: https://github.com/x-blossom/computationalphysics-2013301020024/blob/master/12th/100_e_j.png
  [4]: https://github.com/x-blossom/computationalphysics-2013301020024/blob/master/12th/1000_e_j.png
  [5]: https://github.com/x-blossom/computationalphysics-2013301020024/blob/master/12th/1_e_j_s.png
  [6]: https://github.com/x-blossom/computationalphysics-2013301020024/blob/master/12th/10_e_j_s.png
  [7]: https://github.com/x-blossom/computationalphysics-2013301020024/blob/master/12th/100_e_j_s.png
  [8]: https://github.com/x-blossom/computationalphysics-2013301020024/blob/master/12th/100_e.png
  [9]: https://github.com/x-blossom/computationalphysics-2013301020024/blob/master/12th/1000_e_j_s.png
