# def check(arr):
#    disc = {}
#    for i in arr:
#       if i in disc:
#          disc[i]+=1
#       else:
#          disc[i]=1
      
#    maxi = -100000000000000000
#    mini = 100000000000000000
#    for key , value in disc.items():
#       if value > maxi:
#          maxi = key
#       if value < mini:
#          mini = key
#    print(maxi,mini)

# arr = [10,5,10,15,10,5]
# check(arr)


# ---------------------------

# Another Approach

# --------------------------
def check(arr):
    disc = {}
    for i in arr:
        if i in disc:
            disc[i] += 1  
        else:
            disc[i] = 1  
    
    maxi = -float('inf') 
    mini = float('inf')  
    max_key = None  
    min_key = None  
    
    for key, value in disc.items():
        if value > maxi:
            maxi = value
            max_key = key  
        if value < mini:
            mini = value
            min_key = key 
    print(f"Element with max frequency: {max_key}, Element with min frequency: {min_key}")

arr = [10, 5, 10, 15, 10, 5]
check(arr)
