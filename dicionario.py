d1 = {'key1': 1, 'key2': 2, 'key3': 3}
print(d1)
d1['key4']=0
d1['key4']+=1
print(d1)

for i in d1.values():
    print(f'key{i}: {i}')

d1.update({'key4': 5})
print(d1)

d2=d1
for i in range(5):
        if f'key{i}' in d2:
            print(f'key{i} presente')
        else:
            print(f'key{i} não presente')

for i in d1.keys():
    for j in d2.keys():
        if d1[i] == d2[j]:
            print(d1[i]+d2[j])
