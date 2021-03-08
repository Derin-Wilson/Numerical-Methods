#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:19:04 2020

@author: esha
"""

import numpy as np
import math


def M_M(A,B,n):
    C= np.empty((n,n))
    for i in range(0,n):
        for j in range(0,n):
            for k in range(0,n):
                C[i][j] += (A[i][k]*B[k][j])
    
    for i in range(0,n):
        for j in range(0,n):
                print(C[i][j],end=" ") 
        print("\n",end="") 
              
              
M = [[1, 1, 1, 1],  
    [2, 2, 2, 2],  
    [3, 3, 3, 3], 
    [4, 4, 4, 4]] 
N = [[1, 1, 1, 1],  
    [2, 2, 2, 2],  
    [3, 3, 3, 3], 
    [4, 4, 4, 4]]  
      

M_M(M,N,4)
