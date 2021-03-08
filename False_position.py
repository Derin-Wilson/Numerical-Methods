MAX_ITER = 100000
import numpy as np 
# An example function whose solution 
# is determined using Bisection Method.  
# The function is x^3 - x^2 + 2 
def func( x ): 
    return np.log(x)
  
# Prints root of func(x) in interval [a, b] 
def regulaFalsi( a , b): 
    if func(a) * func(b) >= 0: 
        print("You have not assumed right a and b") 
       
      
    c = a # Initialize result 
      
    for i in range(MAX_ITER): 
          
        # Find the point that touches x axis 
        c = (a * func(b) - b * func(a))/ (func(b) - func(a)) 
          
        # Check if the above found point is root 
        if func(c) == 0: 
            break
          
        # Decide the side to repeat the steps 
        elif func(c) * func(a) < 0: 
              b = c 
        else: 
            a = c 
        print("The value of root is : " ,c,"after",i) 
        if(i>1000):
            break
# Driver code to test above function 
# Initial values assumed 
a =0.5
b =5
regulaFalsi(a, b) 

