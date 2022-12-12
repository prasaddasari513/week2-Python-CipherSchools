def greatest(a,b,c):
    if (a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    else:
        return "NONE"
a = int(input())
b = int(input())
c = int(input())
print(f"Greatest is {greatest(a, b, c)}")