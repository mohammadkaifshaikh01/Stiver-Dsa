def check(arr):

   lastElement = arr.pop(0)
   arr.append(lastElement)
   return arr

arr = [1,2,3,4,5]
print(*check(arr))