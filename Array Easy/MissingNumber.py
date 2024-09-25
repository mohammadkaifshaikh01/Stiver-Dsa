def check (arr):
   n  = len(arr)+1
   sumOfLength = n*(n+1)//2
   sumOfArray = sum(arr)

   return sumOfLength - sumOfArray
   


arr = [1,2,3,4,5,6,8]

missingNum = check(arr)

print(missingNum)