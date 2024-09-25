def check(arr):
   maxi = arr[0]
   for i in range(1,len(arr)):
      if arr[i] > maxi:
         maxi = arr[i]
   print(maxi)


arr = [2,5,1,3,0]
check(arr)
   #farhan Approach
   # for i in arr:
   #    if i > maxi:
   #       maxi = i



   # mine approach
   # print(maxi)
   # # sore = arr.sort()
   # # print(arr[-1])


   # maxi = max(arr)
   # print(maxi)
   # arr = [2,5,1,3,0]
 


