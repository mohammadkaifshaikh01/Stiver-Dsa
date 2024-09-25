def check(arr):
   disc = {}
   for i in arr:
      if i in disc:
         disc[i]+=1
      else:
         disc[i] = 1

   for key,value in disc.items():
      if value == 1:
         print(key)
arr = [2,2,3]
check(arr)