
import math

def f(x):
    return math.exp(-x)-x

def secant( x ): 
    i=0
    d=0.01
    while ((f(x-d)-f(x))> 1e-6) :
           
            x1= x - ((f(x)*(-d))/(f(x-d)-f(x)))
            
            err=(x1-x)/x1
            i+=1
            x=x1
            print("iteration",i,"x is",x1,"error",err)
            if(abs(err)<=0.0001 or i>=100):
                break
    return x1   
       

x0 = 1 # Initial values assumed 
secant(x0) 
  