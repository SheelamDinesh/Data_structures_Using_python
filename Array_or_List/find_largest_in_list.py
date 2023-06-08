# Python program to find largest
# number in a list
 
 
def myMax(list1):
 
    # Assume first number in list is largest
    # initially and assign it to variable "max"
    max = list1[0]
# Now traverse through the list and compare
    # each number with "max" value. Whichever is
    # largest assign that value to "max'.
    for x in list1:
        if x > max:
            max = x
 
    # after complete traversing the list
    # return the "max" value
    return max
 
 
# Driver code
list1 = [10, 20, 4, 45, 99]
print("Largest element is:", myMax(list1))
