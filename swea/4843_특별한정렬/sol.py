import sys
 sys.stdin = open('input.txt')

 T = int(input())

for t in range(int(input())):
    n=int(input())
    lst=sorted(list(map(int,input().split())))
    l=len(lst)
    new_a,new_b,new=[],[],[]
 
    for i in range(l):
        if i<(l//2):
            new_a.append(lst[i])
        elif i>(l//2)-1:
            new_b.append(lst[i])
    new_b.sort(reverse=True)
 
    for i in range(5):
        new.append(new_b[i])
        new.append(new_a[i])
        
    print("#{} {}".format(t+1," ".join(map(str,new))))

# 강사님꺼
import sys
 sys.stdin = open('input.txt')

 T = int(input())

 for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 1. 가장 큰수를 찾는다
    # 2. 가장 큰수를 새로운 배열에 넣는다.
    # 3. 기존에 데이터에서 고른 숫자를 지운다.

    # 1. 가장 작은수를 찾는다.
    # 2. 가장 작은수를 새로운 배열에 넣는다.
    # 3. 기존에 데이터에서 고른 숫자를 지운다.
result = []

while True:
    max_num = 0
    for i in range(len(numbers)):
        if max_num < numbers[i]:
            max_num = numbers[i]
    result.append(max_num)
    numbers.remove(max_num)

    min_num = 100000000
    for j in range(len(numbers)):
        if numbers[j] < min_num:
            min_num = numbers[j]
    result.append(min_num)
    numbers.remove(min_num)

    if len(result) == 10:
        break

# print(result)
temp = list(map(str, result))
result = ' 'join(temp)
print(result)