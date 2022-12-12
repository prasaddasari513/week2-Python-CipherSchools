def li(l):
    k = 0
    for i in l:
        if type(i)==list:
            k+=1
    return k
l = [1,2,[3,4],5,[6,7]]
print(li(l))