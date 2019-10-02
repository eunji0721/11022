# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
n = int(input())
for i in range(1, n+1, 1):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print("Case #%d: %d + %d = %d" %(i, a, b, a+b))