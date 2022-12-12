def greater(a,b):
    if a>b:
        return a
    return b
def new_greatest(a,b,c):
    bigger = greater(a, b)
    return greater(bigger,c)
a = int(input())
b = int(input())
c = int(input())
print(new_greatest(a, b, c))