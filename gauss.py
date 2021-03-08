def linearsolver(A,b):
  n = len(A)
  M = A

  i = 0
  for x in M:
   x.append(b[i])
   i += 1

  for i in range(n):
   for k in range(i,n):
     if abs(M[k][i]) > abs(M[i][i]):
        M[i], M[k] = M[k], M[i]
     else:
        pass

   for j in range(i+1,n):
       fac= float(M[j][i]) / M[i][i]
       for m in range(i , n+1):
          M[j][m] -=  fac * M[i][m]

  x = [0 for i in range(n)]

  x[n-1] =float(M[n-1][n])/M[n-1][n-1]
  for i in range (n-2,-1,-1):
    z = 0
    for j in range(i+1,n):
        z = z  + float(M[i][j])*x[j]
    x[i] = float(M[i][n] - z)/M[i][i]
  print(x)
  
  
Am = [[2, -6, -1], [-3, -2, 7], [-8, 1, -2]]
bm = [-38, -34, -20]


linearsolver(Am,bm)