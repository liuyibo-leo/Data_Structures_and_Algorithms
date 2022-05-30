
m = int(input())
changes = list(map(int, input().split(' ')))
changes.sort()
count = 0
for i in range(len(changes)):
    n = int(m / changes[i])
    count = count + n
    m = m - n * changes[i]

print(count)
