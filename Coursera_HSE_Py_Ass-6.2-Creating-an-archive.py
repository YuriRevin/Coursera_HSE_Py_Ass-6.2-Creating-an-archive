sn = list(map(int, input().split()))
n = []
j = 0

for i in range(0, sn[1]):
    n.append(int(input()))

n.sort()
p = 0

for i in range(0, sn[1]):
    p = p + n[i]
    if p <= sn[0]:
        j = j + 1

print(j)
