def check(arr , num):

   for i in range(len(arr)): 
      if num == arr[i]:
         return i
   return -1


arr = [1 ,2 ,3 ,4 ,5]
num = 3
print(check(arr,num))