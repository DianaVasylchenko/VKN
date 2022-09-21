import math
x=float(input("введіть число x:  "))
def f1(x1):
     rez=x+x**0.5+(4*x+7)**(1./3.)
     return(rez)
def f2(x2) :
    rez=math.tan(x2)+x**2
    return(rez)
def f3(x3) :
    rez=math.log10(math.fabs(x3))  
    return(rez)
y=0.0
if x >= 3.7:
    y=f1(x)
elif  -1.5 < x < 3.7 :
    y=f2(x)
elif x <= -1.5 :
    y=f3(x)
print(y)
