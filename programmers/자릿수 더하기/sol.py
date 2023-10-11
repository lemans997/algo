# 내가 한것
def solution(n):
    answer = 0

    while n > 0:
        a = n //10
        b = n % 10

        n = answer
        answer += b

    return answer

print(solution)

# def solution(n):
#     answer = 0
    
#     while n > 0:
#         # a: 몫, b: 나머지
#         a = n // 10
#         b = n % 10

#         n = a
#         answer += b

#     return answer

def solution(n):
    answer = 0
    
    for i in str(n):
        answer += int(i)

    return answer

print(solution(1234))
print(solution(930211))