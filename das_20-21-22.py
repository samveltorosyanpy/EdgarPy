# import os
#
# count = int(input("Enter files count: "))
#
#
# try:
#     os.mkdir("./your/files")
#     print('Files is create')
# except FileNotFoundError:
#     os.makedirs("./your/files")
#     print("Files is created")
# except FileExistsError:
#     print("Files exist ...")
# except NameError as err:
#     print(err)
# finally:
#     for x in range(count):
#         file = open(f'./your/files/{x}', 'w')
#         file.close()


# x = 19
#
# print('x')
# print(x)
# print(f"x = {x}")


from datetime import datetime as dt
import json


def is_int(text):
    for x in text:
        try:
            int(x)
            return True
        except ValueError as err:
            continue

    return False



def register():
    data = {
        "id": 0,
        "age": 0,
        "year": 0,
        "user_name": ""
    }

    now_year = dt.now().year

    while True:
        if data['age'] == 0:
            try:
                age = int(input("Enter your age: "))
                data['age'] = age
                data['year'] = now_year - age
            except ValueError as err:
                print('!!! Writer your age with number')
                continue

        user_name = input("Enter your full name: ")

        if is_int(user_name):
            print("!!! Write your full name with later")
            continue
        else:
            data['user_name'] = user_name

        break

    users_data = {
        "users": []
    }

    with open('./db/users.json', 'r') as file:
        users_data["users"] = list(json.loads(file.read())['users'])
        data['id'] = users_data["users"][-1]['id'] + 1
        users_data["users"].append(data)

    with open('./db/users.json', 'w') as file:
        file.write(json.dumps(users_data))


register()
