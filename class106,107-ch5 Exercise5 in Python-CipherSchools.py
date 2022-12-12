def common(l,n):
    m = []
    for i in l:
        for j in n:
            if i==j:
                m.append(i)
    return m
l = [1,2,5,8,9]
n = [1,2,7,6,9]
print(common(l, n))