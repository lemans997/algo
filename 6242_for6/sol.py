# blooy_type = {
    # 'A':3,
    # 'B':2,
    # 'O':3,
    # 'AB':2,
# }
# for key in blooy_type:
    # print(key)
# result = 0

# for value in blooy_type.values():
    # result = result + value
# for key, value in blooy_type.items():
    # print((key): (result))

blooy_list = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

blood_dict = {
    'A':0,
    'B':0,
    'O':0,
    'AB':0,
}

for blood in blooy_list:
    blood_dict[blood] += 1

print(blood_dict)


############################


location_list = ['서울', '부산', '부산', '서울', '대전', '광주', '제주']

location_dict = {}

for location in location_list:

    if location in location_dict.keys():
        location_dict[location] += 1
    else:
        location_dict[location] = 1

print(location_dict)