import sys
sys.stdin = open('input.txt')

T = int(input())

def function(N):
    if N%10==0:
        if N==10:
            return 1
        elif N==20:
            return 3
        else:
            return function(N-10)+(2*function(N-20))
    else:
        print("10의 배수만 입력하세요")

for t in range(1, T+1):
    N=int(input())
    count=function(N)
    print("#{} {}".format(t,count))
# 강사님꺼
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) // 10

    memo = [0, 1, 3]

    while N >= len(memo):
        result = memo[len(memo)-2] * 2 + memo[len(memo)-1]
        memo.append(result)

    print(memo(N))
    