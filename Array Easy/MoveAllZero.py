def check(arr):
   temp = []
   zero = []

   result = []
   for i in range(len(arr)-1):
      if arr[i] > 0:
         temp.append(arr[i])
      else:
         zero.append(arr[i])
   # return temp
   # return zero
   result = temp +zero
   return result



arr = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
print(check(arr))



# def check(arr):
#    temp = []
#    zero = []

#    result = []
#    for i in range(len(arr)-1):
#       if arr[i] > 0:
#          temp.insert(0,arr[i])
#       else:
#          temp.append(arr[i])
#    # return temp
#    # return zero
#    result = temp + zero
#    return result



# arr = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
# print(check(arr))