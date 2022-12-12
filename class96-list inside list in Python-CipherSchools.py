k = [1,2,[3,4,[5,6,[7]]]]
print(k[0],',',k[1],',',k[2])
print(k[2][0])
print(k[2][2])
print(k[2][2][1])
print(k[2][2][2][0])
m = [[1,2,3],[4,5,6]]
print("NEXT")
for sub in m:
    for i in sub:
        print(i)