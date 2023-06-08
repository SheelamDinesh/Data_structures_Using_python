def isSorted(l):
    l2 = sorted(l)
    
    if l==l2:
        return True
    else:
        return False

    
l = [10,20,30,15,40]

if isSorted(l):
    print("Yes")
else:
    print("No")
 
