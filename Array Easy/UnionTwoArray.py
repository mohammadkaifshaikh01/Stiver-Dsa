# def check(arr1,arr2):
#    union = arr1 + arr2 
#    result = set(union)
#    return result
# arr1 = [1,2,3,4,5]
# arr2 = [2,3,4,4,5]

# print(check(arr1,arr2))

def check(arr1,arr2):
   remove = set()
   union = []
   for i in range(len(arr1)):
      remove.add(arr1[i])
   for j in range(len(arr2)):
      remove.add(arr2[j])
   for k in remove:
      union.append(k)
   
   return union
   
   
      


arr1 = [1,2,3,4,5]
arr2 = [2,3,4,4,5]

print(check(arr1,arr2))