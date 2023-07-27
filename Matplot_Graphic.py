import matplotlib.pyplot as plt
import numpy as np
#definindo intervalo
xs = range(-60, 120, 1)
#declarando variaveis
res1=[]
res2=[]
res3=[]
res4=[]
res5=[]
pos= 1
#realizando o calculo e conversão 
for x in xs:
    rad = x*(np.pi/180)
    y1= 2*(np.sin(rad))
    y2= np.sin(2*rad)
    y3= np.cos(rad)
    y4= np.cos(2*rad)
    y5= np.sin(rad)
    res1.insert(pos,y1)
    res2.insert(pos,y2)
    res3.insert(pos,y3)
    res4.insert(pos,y4)
    res5.insert(pos,y5)
    pos= pos+1
    #print(x, "=",rad, "=",y1, "=",y2)
#montando o grafico 
plt.plot(xs, res1, color='blue', label = "y1(x)=2sen(x)") 
plt.plot(xs, res2, color='orange', label = "y2(x)=sen(2x)")
plt.plot(xs, res3, color='red', label = "y3(x)=cos(x)")
plt.plot(xs, res4, color='green', label = "y4(x)=cos(2x)")
plt.plot(xs, res5, color='yellow', label = "y5(x)=sen(x)")
plt.ylabel('Cos e Sen')
plt.xlabel('Valor em Graus')
plt.title('y1(x)=y2(x)')
plt.legend()  
plt.show() 