a = int(input())
n = input().split()

min=int(n[0])
max=int(n[0])

for i in range(0,a):
    if min>int(n[i]):
        min=int(n[i])
    if max<int(n[i]):
        max=int(n[i])

print(min, max)