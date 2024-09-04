from pprint import pprint as pp

person = {
    "name": {
        "name": "Samvel",
        "lastname": "Torosyan",
        "age": 24,
        1: 0,
        2: 9,
        13: 0,
        3: 9,
        4: 0,
        5: 9,
        6: 0,
    },
    "lastname": ["Torosyan", "inch vor ban"],
    "age": 24
}

# print(a - b)
# print(person)
# pp(person)

person_1 = {
    "name": "Samvel",
    "lastname": "Torosyan",
    "age": 24
}

print(person_1['age'])

for k in person_1:
    print(person_1['age'])

homework_list = [1, 2, 3, 4, 5]
homework_tuple = (1, 2, 3, 4, 5)
homework_set = {1, 2, 3, 4, 5}

homework_dict = {
    "name": "Edgar",
    "lastname": "Lrjikyan",
    "age": 20
}


for i in homework_list:
    print(i)

print(f"finish {type(homework_list)}")

for i in homework_tuple:
    print(i)

print(f"finish {type(homework_tuple)}")

for i in homework_set:
    print(i)

print(f"finish {type(homework_set)}")

for i in homework_dict:
    print(i)

print(f"finish {type(homework_dict)}")