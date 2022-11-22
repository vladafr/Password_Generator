N = int(input())
d = dict()
for i in range(N):
    k = input()
    v = int(input())
    if k in d:
        d[k] += v
    else:
        d[k] = v
print(d)
