def rev(k):
    v = []
    for i in k:
        v.append(i[::-1])
    return v
k = ['abc','xyz','stu']
print(rev(k))