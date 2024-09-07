def check(num):
   for i in range(num):
      for j in range(1,num+1):
         print(" " ,end = " ")

      for k in range(2*i-1):
         print("*" ,end = " ")
   
      for l in range(1,num+1):
         print(" ",end= " ")
   
      print()

check(5)