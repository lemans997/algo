def solution(n):
    answer = 0

    numbers = range(1, n+1)

    for number in numbers:
        if number % 2 == 0:
            answer = answer + number

    # for i in range(n +1):
        # if i % 2 == 0:
            # answer += i

    return answer

 print(solution(10)) # => 30
 print(solution(4)) # => 6


def solution(n):
    numbers = range(2, n+1, 2)
    return sum(numbers)