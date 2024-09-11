#for integer

# def ReverseNumber(n):
#    result = 0
#    # lastDigit = 0

#    while n > 0:
#       lastDigit =  n % 10
#       result = (result*10)+lastDigit

#       n = n // 10

#    print(result)

# ReverseNumber(125358)



# for String 

# def ReverseNumber(string):
#    result = ""
#    for i in range(len(string)-1,-1,-1):
#       result+=string[i]
   
#    print(result)
      
  

# ReverseNumber("Kaif")


#For Inhance Loop

def ReverseNumber(string):
   result = ""
   for i in reversed(string):
      result = result+i
   print(result)





ReverseNumber("Kaif")
