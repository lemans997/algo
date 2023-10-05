import sys
sys.stdin = open('input.txt', encoding='utf-8')

man1 = input()
man2 = input()

# if man1 == '가위' and man2 == '가위':
    # print('Result : Draw')
# elif man1 == '가위' and man2 == '바위':
    # print('Result : Man1 Win!')

rcp = ['가위', '바위', '보']

man1_idx = rcp.index(man1)
man2_idx = rcp.index(man2)

result = man1_idx - man2_idx

if result == 0:
    print('Result : Draw')
elif result > 0:
    print(f'Result : Man1 Win !')
else:
    if result == -1:
        print('Rssult : Man2 Win !')
    else:
        print('Result : Man1 Win !')
