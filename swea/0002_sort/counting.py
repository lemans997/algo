my_list = [1, 5, 7, 4, 9, 1, 3, 2, 7, 2]

counter = [0 for i in range(10)]

for num in my_list:
    counter[num] += 1

# print(counter)

for value, count in enumerate(counter):
    # print(value, count)
    for i in range(count):
        result.append(value)

print(result)