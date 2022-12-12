def reverse_(num):
    k = []
    for i in range(len(num)):
        p = num.pop()
        k.append(p)
    return k
num = [1,2,3,4]
print(reverse_(num))