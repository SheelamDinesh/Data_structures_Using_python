# Python program to find largest
# number in a list
 
 
def myMax(list1):
    max = list1[0]
    for x in list1:
        if x > max:
            max = x
 
    return max
 
 
# Driver code
list1 = [10, 20, 4, 45, 99]
print("Largest element is:", myMax(list1))
