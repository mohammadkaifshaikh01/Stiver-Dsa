def check(arr,n):

   # print(maxi,mini)
   # arr1 = arr.sort()
   # maxi = arr[-3]
   # mini = arr[1]
   # print(maxi,mini)

   dup = sorted(set(arr))
   if len(dup) < 2:
      print(-1)
   
   small = dup[1]
   large = dup[-2]

   print(large,small)

arr = [1,2,4,7,7,5]
n = len(arr)
check(arr,n)