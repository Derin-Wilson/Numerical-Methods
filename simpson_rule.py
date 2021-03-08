#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:23:13 2020

@author: esha
"""

import math
import numpy as np

# Function to calculate f(x) 
def func( x ): 
    return np.sqrt((9.81*68.1)/0.25)*math.tanh(np.sqrt((9.81*0.25)/68.1)*x)
  
# Function for approximate integral 
def simpsons_( ll, ul, n ): 
  
    # Calculating the value of h 
    h = ( ul - ll )/n 
  
    # List for storing value of x and f(x) 
    x = list() 
    fx = list() 
      
    # Calcuting values of x and f(x) 
    i = 0
    while i<= n: 
        x.append(ll + i * h) 
        fx.append(func(x[i])) 
        i += 1
  
    # Calculating result 
    res = 0
    i = 0
    while i<= n: 
        if i == 0 or i == n: 
            res+= fx[i] 
        elif i % 2 != 0: 
            res+= 4 * fx[i] 
        else: 
            res+= 2 * fx[i] 
        i+= 1
    res = res * (h / 3) 
    return res 
      
# Driver code 
lower_limit = 0   # Lower limit 
upper_limit = 10 # Upper limit 
n = 100 # Number of interval 
print("%.6f"% simpsons_(lower_limit, upper_limit, n)) 