def fibonacci(n):
    a = 0
    b = 1
    c = 0
    curr = 3
    for i in range(n):
        c =a+b
        a = b
        b = c
        curr +=1
        print(c)
n = int(input())
fibonacci(n)