def GCD(N1,N2):
   while N2 > 0:
      N1,N2 = N2 , N1 % N2
   print(N1)



GCD(9,12)