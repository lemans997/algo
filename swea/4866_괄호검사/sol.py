T = int(input())

for tc in range(1, T + 1):
    s = input()
    stack = []
    resulf = 0
    for c in s:
        if c in '{(':
            stack.append(c)
        elif c in '})':
            if stack and ((stack[-1] == '{' and c == '}' or (stack[-1] == '(' and c == ')'))):
                stack.pop()
            else:
                break
    else:
        if not stack:
            resulf = 1
    print(f'#{tc} {resulf}')

    import sys
    sys.stdin = open('input.txt')

    T = int(input())

    for tc in range(1, T+1):
        code = input()

        # for char in code:
            # if char == '(' or char == ')' or char == '{' or == char '}'
        stack = []

        for char in code:
            if char == '(' or char == '{':
                stack.append(char)
            elif len(stack) and char == ')' and stack[-1] == '(':
                stack.pop()
            elif len(stack) and char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(char)

        if len(stack) == 0:
            resulf = 1
        else:
            resulf = 0

        print(resulf)