def solution(angle):
    answer = 0
    # angle(70, 90, 180)
    # result(1, 3, 4)
    # if angle(70) = result(1):
        # print(f'(angle)이 70이므로 예각입니다.')
    # elif angle(90) =result(3):
        # print(f'')
    if angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif 90 < angle < 180:
        answer = 3
    else:
        answer = 4
        
    return answer

print(solution(70))
print(solution(90))
print(solution(180))