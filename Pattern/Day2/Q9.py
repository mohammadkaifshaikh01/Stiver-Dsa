def check(num):
   for i in range(num+1):
      for j in range(num+1-1-i):
         print(" " , end = " ")

      for k in range(2*i-1):
         print("*" , end = " ")
      for l in range(num+1-1-i):
         print(" " , end = " ")
         
      print()

   for i in range(num+1):
      for j in range(i):
         print(" " , end = " ")
      for k in range(num*2 - (2*i+1)):
         print("*" ,end = " ")
      for l in range(i):
         print(" " , end = " ")
      
 
      print()

check(5)