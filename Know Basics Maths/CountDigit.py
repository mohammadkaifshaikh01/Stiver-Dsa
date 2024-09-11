def count(n):
   count = 0
   lastDigit  = 0
   while n > 0:
      lastDigit = n % 10
      count = count+1
      n = n//10
   print(count)

count(12345894848454)