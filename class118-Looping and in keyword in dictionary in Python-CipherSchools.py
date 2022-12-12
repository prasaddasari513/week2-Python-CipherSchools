k = {'key':'value'}
if 'key' in k:
    print("YES")
else:
    print("NO")
if 'value' in k.values():
    print(True)
else:
    print(False)
for i in k.values():
    print(i)
print(type(k))
k1=k.items()
print(k1)
for key,value in k.items():
    print(f'key={key} and value={value}')