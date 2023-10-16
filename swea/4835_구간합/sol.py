# 내가 한것
 import sys
 sys.stdin = open('input.txt')

 T = int(input())

 for i in range(1, T+1):
     N, M = map(int, input().split())
     N_list = list(map(int, input().split()))
     new_list = []

     for j in range(N-M+1):
         result = 0
         for k in range(j, j+M):
             result += N_list[k]
         new_list.append(result)

     print(f'#{i}, {max(new_list)-min(new_list)}')
# 유건님
import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    TC = list(map(int, input().split()))


    max_value = 0
    min_value = 123456

    for i in range(N-M+1):
        temp = 0
        for j in range(M):
            temp += TC[i+j]

        if temp > max_value:
            max_value = temp
        if temp < min_value:
            min_value = temp

    ans = max_value - min_value

    print('#{} {}'.format(tc, ans))
# 곽승준님 
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):

    N,M = list(map(int, input().split())) 

    numbers = list(map(int, input().split()))

    blank = []

    for i in range(N-M+1):
        temp_value =0
        for j in range(i,i+M):
            temp_value += numbers[j]

        blank.append(temp_value)

    answer = max(blank) - min(blank)

        


    print(f'#{tc} {answer}')

# 오창희강사님
mport sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    
    min_tobal = 1000000000
    max_tobal = 0
    # 구간합늘 구하기 위한1(시작점)
    # => 뒤에 M개의 데이터를 더하기 위한 시작점
    for i in range(N+M1):
        total = 0

        # 시작점을 기준으로 오른쪽 M개의 숫자의 합
        for j in range(N-M+1):
            total = 0

            # 시작점을 기준으로 오른쪽 M개의 숫자의 합
            for j in range(M):
                total = total + numbers[i+j]
                # tobal += numbers[i+j]

            if total < min_tobal:
                min_tobal = tobal

            if tobal > max_tobal:
                max_tobal = tobal

        result = max_tobal - min_tobal

        print(f'{result}')