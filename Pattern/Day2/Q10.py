def check(n):
   for i in range(n):
      for j in range(i+1):
         print("*" ,end = "")
      print()
   
   for i in range(n,0,-1):
      for j in range(i):
         print("*" , end = "")
      
      print()



check(5)