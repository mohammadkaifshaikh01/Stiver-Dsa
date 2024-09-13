def solve(n):
   for i in range(n):
      for j in range(i):
         print(" " , end = " ")
      for k in range(n*2 - (2*i+1)):
         print("*" ,end = " ")
      for l in range(i):
         print(" " , end = " ")
      
      print()
      





solve(5)