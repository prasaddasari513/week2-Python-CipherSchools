def oddeven(k):
    o = []
    e = []
    for i in k:
        if i%2==0:
            e.append(i)
        else:
            o.append(i)
    m = [o,e]
    return m
k = [1,2,3,4,5,6,7]
print(oddeven(k))
