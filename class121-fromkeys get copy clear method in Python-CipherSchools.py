d = dict.fromkeys(['name','age','k'],'unknown')
print(d)
k = dict.fromkeys(range(1,11),'nothing')
print(k)
print(d.get('names'))
if d.get('name'):
    print("yes")
else:
    print("no")
d3 = d.copy()
print(d3.popitem())
print(d)