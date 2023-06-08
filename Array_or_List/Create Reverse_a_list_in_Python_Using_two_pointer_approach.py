def reverseList(l):
    s = 0
    e = len(l) - 1

    while s < e:
        l[s], l[e] = l[e], l[s] 
        s = s + 1
        e = e - 1


l = [int(x) for x in input().split(',')]
reverseList(l)
print(l)
