#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 19:16:27 2020

@author: esha
"""

import math

# Python3 code for implementation of Newton 
# Raphson Method for solving equations 
  
# An example function whose solution  
# is determined using Bisection Method.  
# The function is x^3 - x^2 + 2 
def func( x ): 
    return math.exp(-x/2)*(4-x)-2
  
# Derivative of the above function  
# which is 3*x^x - 2*x 
def derivFunc( x ): 
    return -3*math.exp(-x/2) + 0.5*x*math.exp(-x/2)
  
# Function to find the root 
def newtonRaphson( x ): 
    i=0
    if abs(derivFunc( x ))> 1e-8:
        while True:
            h = func(x) / derivFunc(x) 
            x1=x-h
            err=(x1-x)/x1
            x=x1
            i+=1
            
            print("iteration",i,"x is",x1,"error",err)
            
            if(abs(err)<=0.001 or i>=100):
                break
       
       
      
    
# Driver program to test above 
x0=6 # Initial values assumed 
print(derivFunc(x0) )

# This code is contributed by "Sharad_Bhardwaj" 
