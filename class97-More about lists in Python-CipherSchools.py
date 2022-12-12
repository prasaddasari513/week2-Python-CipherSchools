num = list(range(21))
print(num)
print(num.pop())
print(num.index(3,1,4))
def nege(l):
    neg = []
    for i in l:
        neg.append(-i)
    print(neg)
nege(num)