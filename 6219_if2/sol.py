import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    if tc % 1 == 5:
        print('1는 5의 약수 입니다.')
    elif tc * 1 == 5:
        print('5는 5의 약수 입니다.')
    else:
        print('5는 1과 5로만 나눌 수 있는 소수입니다.')
