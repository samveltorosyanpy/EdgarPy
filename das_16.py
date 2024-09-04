# x = 10
# y = 11
# a = y
#
# y = x
# x = a
#
# print(x, y)


# file = open('db/users.json', 'a+')

# print(file.write("23"))

def add_user(user_data):
    with open('db/users.json', 'a+') as file:
        file.write(user_data)



firs_name, last_name, age = input("Enter your first name: "), input('Enter your last name: '), input('Enter your age: ')

new_user = f"{firs_name} | {last_name} | {age}\n"

add_user(user_data=new_user)
