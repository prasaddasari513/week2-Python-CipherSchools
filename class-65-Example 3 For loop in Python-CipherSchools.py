name = input()
for i in range(len(name)):
    sum = ""
    if name[i] not in sum:
        print(name[i],":",name.count(name[i]))
        sum+=name[i]