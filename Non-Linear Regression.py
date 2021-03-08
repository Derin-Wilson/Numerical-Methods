import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

"""This is a code to perform Non-Linear Regression via Gauss Newton Method."""
"""Note the use of Sympy to carry out symbolic computation."""
"""The code is highly generalised. However, the user must manually define the function form,
the individual parameters, the partial derivatives and the matrix. Just look for 
/*Manual Intervention needed*/ and follow the corresponding examples."""

#This is the given dataset and the corresponding scatter plot
K=[(9.58*10**7,-78.4119),(9.581*10**7,-78.2809),(9.582*10**7,-77.6955),(9.583*10**7,-77.9017),(9.584*10**7,-77.6219),(9.585*10**7,-77.7346),(9.586*10**7,-77.3264),(9.587*10**7,-77.0228),(9.588*10**7,-77.0116),(9.589*10**7,-76.9978),(9.59*10**7,-77.1691),(9.591*10**7,-76.3959),(9.592*10**7,-76.5368),(9.593*10**7,-76.5986),(9.594*10**7,-75.9251),(9.595*10**7,-76.4683),(9.596*10**7,-76.1168),(9.597*10**7,-75.986),(9.598*10**7,-75.9121),(9.599*10**7,-75.198),(9.6*10**7,-75.3556),(9.601*10**7,-74.9559),(9.602*10**7,-74.8481),(9.603*10**7,-75.0825),(9.604*10**7,-74.8915),(9.605*10**7,-74.7229),(9.606*10**7,-74.3703),(9.607*10**7,-74.5724),(9.608*10**7,-74.0785),(9.609*10**7,-73.9684),(9.61*10**7,-74.1571),(9.611*10**7,-73.7761),(9.612*10**7,-73.608),(9.613*10**7,-73.4015),(9.614*10**7,-73.2046),(9.615*10**7,-73.0437),(9.616*10**7,-72.7368),(9.617*10**7,-72.671),(9.618*10**7,-72.6937),(9.619*10**7,-72.201),(9.62*10**7,-72.3267),(9.621*10**7,-71.8846),(9.622*10**7,-71.8481),(9.623*10**7,-71.6784),(9.624*10**7,-71.4149),(9.625*10**7,-71.0938),(9.626*10**7,-70.9062),(9.627*10**7,-70.787),(9.628*10**7,-70.4523),(9.629*10**7,-70.3844),(9.63*10**7,-70.093),(9.631*10**7,-69.936),(9.632*10**7,-69.9041),(9.633*10**7,-69.5365),(9.634*10**7,-69.2365),(9.635*10**7,-69.2724),(9.636*10**7,-68.9441),(9.637*10**7,-68.4834),(9.638*10**7,-68.377),(9.639*10**7,-68.2777),(9.64*10**7,-67.9335),(9.641*10**7,-67.8276),(9.642*10**7,-67.3677),(9.643*10**7,-67.2121),(9.644*10**7,-66.9543),(9.645*10**7,-66.5628),(9.646*10**7,-66.3919),(9.647*10**7,-66.2225),(9.648*10**7,-65.8333),(9.649*10**7,-65.4605),(9.65*10**7,-65.2045),(9.651*10**7,-64.86),(9.652*10**7,-64.6347),(9.653*10**7,-64.3055),(9.654*10**7,-63.921),(9.655*10**7,-63.6229),(9.656*10**7,-63.3132),(9.657*10**7,-62.9083),(9.658*10**7,-62.4926),(9.659*10**7,-62.1753),(9.66*10**7,-61.7799),(9.661*10**7,-61.3998),(9.662*10**7,-60.9837),(9.663*10**7,-60.6005),(9.664*10**7,-60.13),(9.665*10**7,-59.7679),(9.666*10**7,-59.362),(9.667*10**7,-58.8551),(9.668*10**7,-58.3979),(9.669*10**7,-57.9813),(9.67*10**7,-57.4714),(9.671*10**7,-57.0503),(9.672*10**7,-56.6426),(9.673*10**7,-56.2068),(9.674*10**7,-55.8046),(9.675*10**7,-55.4163),(9.676*10**7,-55.1658),(9.677*10**7,-54.9431),(9.678*10**7,-54.8101),(9.679*10**7,-54.7577),(9.68*10**7,-54.7391),(9.681*10**7,-54.8365),(9.682*10**7,-55.0157),(9.683*10**7,-55.203),(9.684*10**7,-55.4826),(9.685*10**7,-55.8251),(9.686*10**7,-56.1373),(9.687*10**7,-56.549),(9.688*10**7,-56.8983),(9.689*10**7,-57.2847),(9.69*10**7,-57.6948),(9.691*10**7,-58.0864),(9.692*10**7,-58.5025),(9.693*10**7,-58.8397),(9.694*10**7,-59.1333),(9.695*10**7,-59.6324),(9.696*10**7,-59.9333),(9.697*10**7,-60.2584),(9.698*10**7,-60.6089),(9.699*10**7,-60.8731),(9.7*10**7,-61.2167),(9.701*10**7,-61.5615),(9.702*10**7,-61.7549),(9.703*10**7,-62.0251),(9.704*10**7,-62.3054),(9.705*10**7,-62.5325),(9.706*10**7,-62.7754),(9.707*10**7,-63.2065),(9.708*10**7,-63.3878),(9.709*10**7,-63.5167),(9.71*10**7,-63.8702),(9.711*10**7,-64.0812),(9.712*10**7,-64.2383),(9.713*10**7,-64.4088),(9.714*10**7,-64.5798),(9.715*10**7,-64.8458),(9.716*10**7,-65.0902),(9.717*10**7,-65.2676),(9.718*10**7,-65.4861),(9.719*10**7,-65.5697),(9.72*10**7,-65.8855),(9.721*10**7,-65.9254),(9.722*10**7,-66.1197),(9.723*10**7,-66.3695),(9.724*10**7,-66.4352),(9.725*10**7,-66.6378),(9.726*10**7,-66.7653),(9.727*10**7,-66.9068),(9.728*10**7,-67.0008),(9.729*10**7,-67.1592),(9.73*10**7,-67.2369),(9.731*10**7,-67.3674),(9.732*10**7,-67.5434),(9.733*10**7,-67.8334),(9.734*10**7,-67.8152),(9.735*10**7,-67.8429),(9.736*10**7,-68.0408),(9.737*10**7,-68.0338),(9.738*10**7,-68.4292),(9.739*10**7,-68.4913),(9.74*10**7,-68.4621),(9.741*10**7,-68.6884),(9.742*10**7,-68.5909),(9.743*10**7,-68.9225),(9.744*10**7,-68.9119),(9.745*10**7,-69.1127),(9.746*10**7,-69.2131),(9.747*10**7,-69.3178),(9.748*10**7,-69.4601),(9.749*10**7,-69.3414),(9.75*10**7,-69.4669),(9.751*10**7,-69.7638),(9.752*10**7,-69.7311),(9.753*10**7,-69.8488),(9.754*10**7,-69.8445),(9.755*10**7,-69.9179),(9.756*10**7,-70.2205),(9.757*10**7,-70.3532),(9.758*10**7,-70.5463),(9.759*10**7,-70.3361),(9.76*10**7,-70.4333),(9.761*10**7,-70.6723),(9.762*10**7,-70.4073),(9.763*10**7,-70.5563),(9.764*10**7,-70.8198),(9.765*10**7,-71.0367),(9.766*10**7,-70.9699),(9.767*10**7,-71.0749),(9.768*10**7,-71.1531),(9.769*10**7,-71.1948),(9.77*10**7,-71.2866),(9.771*10**7,-71.2072),(9.772*10**7,-71.5042),(9.773*10**7,-71.4413),(9.774*10**7,-71.4487),(9.775*10**7,-71.495),(9.776*10**7,-71.6052),(9.777*10**7,-71.9859),(9.778*10**7,-71.7211),(9.779*10**7,-71.9483),(9.78*10**7,-71.7974)]
l=len(K)
xd=np.zeros(l)
yd=np.zeros(l)
for i in range(0,l):
    xd[i]=K[i][0]
    yd[i]=K[i][1]
plt.scatter(xd,yd,color='red')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('y vs x scatter plot')
plt.show()

#Enter the form of the guess function
#Manual intervention needed
x=sym.Symbol('x')
a0=sym.Symbol('a0')
a1=sym.Symbol('a1')
a2=sym.Symbol('a2')
a3=sym.Symbol('a3')
a4=sym.Symbol('a4')
f=a0+a1/(1+a2*(x-a3)**2)+a4*x

#Our function contains 5 parameters and we calculate the partial derivatives wrt the params
#Manual intervention needed
f_a0=sym.diff(f,a0)
f_a1=sym.diff(f,a1)
f_a2=sym.diff(f,a2)
f_a3=sym.diff(f,a3)
f_a4=sym.diff(f,a4)

#Displaying the form of the test function and its derivatives
#Manual intervention needed
print("The form of the test function is :\n",f,"\n")
print("The pd of f wrt a0 is :\n",f_a0,"\n")
print("The pd of f wrt a1 is :\n",f_a1,"\n")
print("The pd of f wrt a2 is :\n",f_a2,"\n")
print("The pd of f wrt a3 is :\n",f_a3,"\n")
print("The pd of f wrt a4 is :\n",f_a4)

#User defined initial values of parameters and tolerances
#Manual intervention needed
a0i=eval(input("Enter the initial guess for a0 : "))
a1i=eval(input("Enter the initial guess for a1 : "))
a2i=eval(input("Enter the initial guess for a2 : "))
a3i=eval(input("Enter the initial guess for a3 : "))
a4i=eval(input("Enter the initial guess for a4 : "))
t0=eval(input("Enter the tolerance for a0 : "))
t1=eval(input("Enter the tolerance for a1 : "))
t2=eval(input("Enter the tolerance for a2 : "))
t3=eval(input("Enter the tolerance for a3 : "))
t4=eval(input("Enter the tolerance for a4 : "))

#Creating arrays for parameters and function derivatives
#Manual intervention needed
a=np.array([a0,a1,a2,a3,a4]) #Stores the parameters in symbolic form
A0=np.array([a0i,a1i,a2i,a3i,a4i]) #Initial Parameter matrix (user given numeric values)
f_p=np.array([f_a0,f_a1,f_a2,f_a3,f_a4]) #Initial Derivative matrix

#Module to perform Non-Linear Regression
def NL_Reg(xd,yd,A0,t0,t1,f,f_p):
    nop=len(A0) #The number of parameters
    n=len(xd) #The number of datapoints
    dA=np.zeros(nop) #The matrix to store change in parameters
    i=0 #Counts the no of parameters
    while 1>0:
        Z=Z_Mat(xd,nop,n,f,f_p,A0) #The Z-matrix
        D=D_Mat(xd,yd,n,f,f_p,A0) #The D-matrix
        Zt=np.transpose(Z) #The transpose of Z-matrix
        L=np.dot(Zt,Z) #Calculating Zt*Z
        R=np.dot(Zt,D) #Calculating Zt*D
        LI=np.linalg.inv(L) #Calculating (Zt*Z)^-1
        dA=np.dot(LI,R) #Solving the master equation L*dA=R <=> dA=LI*R ; LI=L^-1
        #Manual intervention needed
        e0=abs(dA[0]*100)/A0[0]
        e1=abs(dA[1]*100)/A0[1]
        e2=abs(dA[2]*100)/A0[2]
        e3=abs(dA[3]*100)/A0[3]
        e4=abs(dA[4]*100)/A0[4]
        #Condition for termination
        #Manual intervention needed
        if e0<t0 and e1<t1 and e2<t2 and e3<t3 and e4<t4 or i==300:
            A0=A0+dA
            return (A0,i)
        else:
            A0=A0+dA
            print(A0,i+1)
            i+=1
        
#Module for Parameter-Substitution
def P_Sub(f,f_p,A):
    """f is a function whereas f_p is an array of functions"""
    P=list(zip(a,A))
    #Substitution in f
    f=f.subs(P)
    #Substitution in f_p
    for i in range(0,len(A)):
        f_p[i]=f_p[i].subs(P)
    return (f,f_p) #First element is a function and the 2nd is an array
    
#Module for finding the D-Matrix
def D_Mat(xd,yd,n,f,f_p,A):
    D=np.zeros(n)
    f=P_Sub(f,f_p,A)[0]
    for i in range(0,n):
        D[i]=yd[i]-f.subs(x,xd[i])
    return D

#Module to find the Z-Matrix
def Z_Mat(xd,nop,n,f,f_p,A):
    Z=np.zeros(shape=(n,nop))
    f_p=P_Sub(f,f_p,A)[1]
    for i in range(0,n):
        for j in range(0,nop):
            Z[i][j]=f_p[j].subs(x,xd[i])
    return Z

#Plotting the fitted function
A,i=NL_Reg(xd,yd,A0,t0,t1,f,f_p) #The results
f=P_Sub(f,f_p,A)[0]
print("\n The function to be fitted as obtained after {} iterations is :\n {}".format(i,f))
sym.plot(f,(x,09.58*10**7,9.78*10**7))

#Superposing the Experimental and Theoretical data
y=np.zeros(l)
for i in range(0,l):
    y[i]=f.subs(x,xd[i])
plt.scatter(xd,yd,color='red')
plt.plot(xd,y,color='green')
plt.title("Experimental vs Theoretical")
plt.xlabel("x-axis")
plt.ylabel("f(x)/y-axis")
plt.show()