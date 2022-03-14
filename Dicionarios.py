import sys

"""valores=['haroldo','fátima','bianca','bruna']
tabela=dict()

for i in range(len(valores)):
    tabela[i]=valores[i]

print(tabela)

d = dict()
s='hfbibru'
for c in s:
    if c not in d:
        d[c]=1
    else:
        d[c]+=1

d2=d
print(d)
print(d.get(s, d))

for i in sorted(d, key=d.get(i)):
    print(i,d[i])

print();inverso = dict()
for key in d2:
    val = d2[key]
#    print(f'd2= {d2}, key= {key}, val= {val}')
    if val not in inverso:
        inverso[val] = [key]
    else:
        inverso[val].append(key)

print(d2); print(inverso)

known = {0:0, 1:1, 2:2, 3:3, 4:4}; n=4
if n in known:
    print(known[n])
    sys.exit()
res = known[n-1] + known[n-2]
print(res)
"""


def exemplo3():
    global contagem
    contagem += 1
    return contagem

def exemplo4():
    known[2] = 1
    return known

if __name__ == '__main__':
    contagem=10
    known = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
    print(exemplo3())
    print(exemplo4())
