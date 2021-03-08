import numpy as np
import sympy as sym
import math as m

"""This is a  program to carry out Integration via Adaptive Quadrature"""

x = sym.Symbol('x')
f = 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5 #Define the function here
xl = 0 #Lower Limit
xu = 0.8 #Upper Limit
etol = 0.0005 #Tolerance

#Module to carry out Adaptive Quadrature
def Apt_Quad(xl, xu, n, f, i):
    e=100 #Dummy value for initial error
    while 1>0:
        I = np.zeros(i) #Array to store the 1st column Simpson1/3 estimates
        for j in range(0, i):
            I[j] = Simp_1_3(xl, xu, n, f) #Using Simp_1_3() method to calculate the Integral value
            n = 2*n #No of segments being doubled each time
        res, e = Rec(I, 1, e) #The 2nd arg gives level of integration which is 1 for Simpson1/3
        if e<etol:
            print("The value of the Integral as obtained after {} passes is : {}".format(i, res))
            print("The approximate error is : {}".format(e))
            break
        else:
            i+=1 

#Module to carry out Recursion
def Rec(I, o, e): #o is the order of integration and e is error
    l = len(I) #The length of the incoming array
    #print(I)
    if l==1: #If l equals 1 means the end is nigh(for i-th pass)
        return (I, e)
    else:
        I1 = np.zeros(l-1)
        for i in range(0, l-1):
            I1[i] = (4**(o)*I[i+1]-I[i])/(4**(o)-1)
        e = err(I1[l-2], I[l-1])
        if e<etol: #Stop immediately as sufficient accuracy reached
            return (I1[l-2], e)
        else:
            return Rec(I1, o+1, e) #Recursion
        
#Module to carry out Repeated Trapezoidal Rule
def Simp_1_3(xl, xu, n, f):
    h = (xu-xl)/float(n)
    sum = f.subs(x, xl)
    for i in range(1,n):
        if i%2!=0:
            sum = sum+4*f.subs(x, xl+i*h)
        else:
            sum = sum+2*f.subs(x, xl+i*h)
    ans = h*(sum+f.subs(x, xu))/3
    return ans

#Module to carry out error evaluation
def err(a, b):
    e  = (abs(a-b))/a
    return e*100 #Forumla for approximate error

Apt_Quad(xl, xu, 2, f, 1) #Method call
        
    
    

