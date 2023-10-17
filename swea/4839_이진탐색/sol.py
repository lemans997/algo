import sys
 sys.stdin = open('input.txt')


def binary_search(start, end, target, count):
    m=(start+end)//2
    if m==target:
        return count
    if target > m:
        return binary_search(m,end,target,count+1)
    else:
        return binary_search(start,m,target,count+1)


Test_case=int(input())

for t in range(1,Test_case+1):
    P, A, B =map(int,input().split())
    count_A=binary_search(1,P,A,0)
    count_B=binary_search(1,P,B,0)
    if count_A>count_B:
        print("#{} B".format(t))
    elif count_A == count_B:
        print("#{} 0".format(t))
    else:
        print("#{} A".format(t))
# 강사님꺼
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 1+T):
    # P : 책의 장수
    # A : A가 찾아야 하는 페이지
    # B : B가 찾아야 하는 페이지
    P, A, B = list(map(int, input().split()))

    left = 1
    right = P

    while True:
        center = int((left+right)/2)

        # A의 목적페이지가 가운데보다 왼쪽에 있는 경우
        # 오른쪽 데이터를 지우기
        if A < center:
            right = center
        # A의 목적페이지가 가운데보다 오른쪽에 있는 경우
        # 왼쪽 데이터를 지우기
        elif center < A:
            left = center
        # A의 목적페이지에 도달한 경우
        else:
            break

        A_count += 1

    left = 1
    right = P
    B_count = 0

    while True:
        center = int((left+right)/2)

        if B < center:
            right = center
        elif center < B:
            left = center
        else:
            break

        B_count += 1

    print(A_count, B_count)
