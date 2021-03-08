#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 19:01:57 2020

@author: esha
"""
import numpy as np
A=np.array([[1.0,2,3],[0.0,1.0,5],[5.0,6,0.0]])
B=np.eye(len(A)) # makes identity matrix

def LU(A,B,n):
    L,U=forw_elim(A,n)
    D=forw_sub(L,B,n)
    x=back_sub(U,D,n)
   
    return (x)

def forw_elim(A,n):
    L=np.eye(len(A))
    n=len(A)
    for i in range(n):
        for j in range(i+1,n):
            
            fac=A[j][i]/A[i][i]
            L[j][i]=fac
            
            for k in range(i,n):
                A[j][k]-= fac*A[i][k]
    return(L,A)
    
    
def forw_sub(L,B,n):
    n=len(L)
    D=[0 for i in range(n)]
   
    D[0]=B[0]/L[0][0]
    for i in range(1,n):
        s=0
        for j in range(0,i):
            s+= L[i][j]*D[j]
            D[i]=(B[i]-s)/L[i][i]
        
    return D     
        
def back_sub(U,D,n):
    n=len(U)
    x=[0 for i in range(n)]
   
    x[n-1]=D[n-1]/U[n-1][n-1]
    for i in range(n-2,-1,-1):
        s=0
        for j in range(i+1,n):
            s+= U[i][j]*x[j]
            x[i]=(D[i]-s)/U[i][i]
        
    return x     
      

def Transpose(A):
    nr=len(A)
    nc=len(A[0])
    At=np.zeros((nc,nr))
    
    for i in range(nc):
        for j in range(nr):
            At[i][j]=A[j][i]
            
    return(At)
    
   
    
def Inv(A,B):
    n=len(A)
    A_Inv=np.zeros(shape=(n,n))
    for i in range(0,n):
        K=np.copy(A)
        A_Inv[i]=LU(K,B[i],n)
    return(Transpose(A_Inv))

print("The Inverse matrix is :\n",Inv(A,B))
print("\n")
print("A times its inverse is :\n",np.dot(A,Inv(A,B)))   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    







                
        
 
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
