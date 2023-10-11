def solution(n):
    answer = 0

    while n > 0:
        a = n //10
        b = n % 10

        n = answer
        answer += b

    return answer

print(solution)