def check(arr):
   count = 0
   maximum = 0
   for i in range(len(arr)):
      if arr[i] == 1:
         count+=1
         maximum = max(maximum,count)
      else:
         count = 0
   return maximum
   



arr = [1, 1, 0, 1]
print(check(arr))