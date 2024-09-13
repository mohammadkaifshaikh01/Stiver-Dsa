def check(arr):
   disc = {}
   for i in arr:
      if i in disc:
         disc[i]+=1
      else:
         disc[i]=1
   # return disc
   for key , value in disc.items():
      print(key,value)
      


arr = [10,5,10,15,10,5,7,5,1]
check(arr)

