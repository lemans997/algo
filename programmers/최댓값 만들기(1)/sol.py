def solution(numbers):
    answer = 0
    
    for i in range(len(numbers)):
        for j in range(len(numbers)-1, i, -1):
            multi = numbers[i] * numbers[j]

            if answer < multi:
                answer = multi

    return answer

def solution(numbers):
    answer = 0
    
    numbers.sort()

    answer = numbers[-1] * numbers[-2]
    
    return answer


print(solution([1, 2 ,3 ,4, 5]))
print(solution([0, 31, 24, 10, 1, 0]))