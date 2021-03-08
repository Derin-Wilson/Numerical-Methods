#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 18:48:45 2020

@author: esha
"""



import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

"""This is a program to perform polynomial interpolation"""
#Enter the data
x=np.array([0,1,2,3,4,5])
y=np.array([2.1,7.7,13.6,27.2,40.9,61.1])
print("The x matrix is :\n",x)
print("\n")
print("The y matrix is :\n",y)
print("\n")

plt.scatter(x,y,color='red')
plt.title("Actual data")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

#This is a module to perform Polynomial-Interpolation
def pol_int(x,y):
    n=len(x)
    m=eval(input("Enter the degree of the polynomial to be fitted : "))
    print("\n")
    z=z_mat(x,n,m)
    zt=Transpose(z)
    A=np.dot(zt,z)
    B=np.dot(zt,y)
    a=Gauss_Elim(A,B,len(A))
    return (z,zt,A,B,a)#Returns a tuple

#This is a module to find the z matrix for any polynomial-interpolation
def z_mat(x,n,m):
    z=np.zeros(shape=(n,m+1))
    for i in range(0,n):
        for j in range(0,m+1):
            d=np.copy(x[i])
            z[i][j]=pow(d,j)
    return(z)

#This is a module for Transpose of any n x m matrix
def Transpose(z):
    no_r=len(z)
    no_c=len(z[0])
    zt=np.zeros(shape=(no_c,no_r))
    for i in range(0,len(zt)):
        for j in range(0,len(zt[0])):
            d=np.copy(z[j][i])
            zt[i][j]=d
    return(zt)

#This is a module for Gauss-Elimination
def Gauss_Elim(A,B,n):
    RR_A,RR_B=Forward_Elim(A,B,n)#Function call for forward elimination
    sol=Back_Sub(RR_A,RR_B,n)#Function call for back substitution
    return sol
       
#Module to perform Forward Elimination
def Forward_Elim(A,B,n):
    for i in range(0,n-1):
        for j in range(i+1,n):
            factor=A[j][i]/A[i][i]
            for k in range(i,n):
                A[j][k]=A[j][k]-(factor*A[i][k])
            B[j]=B[j]-factor*B[i]
    return(A,B)#Returns a tuple contating row-reduced forms of A and B

#Module to perform Back-Substitution
def Back_Sub(A,B,n):
    x=np.zeros(n)
    s=0
    x[n-1]=B[n-1]/A[n-1][n-1]
    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            s=s+A[i][j]*x[j]
        x[i]=(B[i]-s)/A[i][i]
        s=0
    return(x)#Returns the solution matrix

sol=pol_int(x,y)#Interpolation
print("The z matrix is :\n",sol[0])
print("\n")
print("The transpose of matrix is :\n",sol[1])
print("\n")
print("The zt*z matrix is :\n",sol[2])
print("\n")
print("The zt*y vector is :\n",sol[3])
print("\n")
print("The coeff vector is :\n",sol[4])
print("\n")

#Module to find the polynomial given the coeff-matrix and also the fitted y-values
def func(k,x):
    l=len(x)
    x_f=np.copy(x)
    y_f=np.zeros(l)
    x=sym.Symbol('x')
    m=len(k)
    s=0
    for j in range(m-1,-1,-1):
        s=k[j]+s*x
    for j in range(0,l):
        y_f[j]=s.subs(x,x_f[j])
    return (s,y_f)

k=sol[4]#This is the coeff matrix
f,y_f=func(k,x)#f is the polynomial and y_f is as calculated by f
print("The polynomial which is to be fitted is :\n",f)

#Plotting
plt.scatter(x,y,label='actual data',color='red')
plt.plot(x,y_f,label='fitted data',color='green')
plt.legend(loc='best')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('The actual and fitted data')
plt.show()

