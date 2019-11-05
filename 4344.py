test = int(input())

for i in range(1,test+1):
    n = input().split()
    sum = 0
    count = 0
    for j in range(1, len(n)):
        sum += int(n[j])
    avg = sum / int(n[0])
    for x in range(1, len(n)):
        if avg<int(n[x]):
            count += 1
    percent = count/int(n[0])*100
    print("%.3f%%"%(round(percent,3)))