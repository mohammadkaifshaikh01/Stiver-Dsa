def check(arr):
   removeDuplicates = []
   for i in range(len(arr)-1):
      if arr[i] not in removeDuplicates:
         removeDuplicates.append(arr[i])
   return removeDuplicates


arr =  [1,1,2,2,2,3,3]
print(check(arr))