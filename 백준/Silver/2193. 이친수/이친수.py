n = int(input())
d = [0, 1, 1]
for i in range(3, 91):
    result = d[i-1] + d[i-2]
    d.append(result)

print(d[n])