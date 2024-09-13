def check(n):
   no = n
   string = len(str(n))
   sum = 0

   while n > 0:
      lastdigit = n % 10  #153 3 
      sum += lastdigit**string # 3 ** 
      n = n//10
   
   if sum == no:
      print("True")
   else:
      print("false")
check(153)


