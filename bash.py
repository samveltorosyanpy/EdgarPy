import json
import os

add_regist = {
    "id" : 0,
    "users_registration" : []
    }


users_data = {
    'users' : []
}

def user_checks(text):
    return text.isalpha()


def user_check(text):
    try:
        int(text)
        return True
    except ValueError as err:
        return False

while True:
    try:
        command = input("Type /START to begin: ")
        if command == "/START":
            print("Hello! Choose one of the options:")
            print("1. Register")
            print("2. Exit")

            option = int(input("Enter your choice: "))
            if option == 1:
                p_name = input("Please enter your full name: ")
                if user_checks(p_name):
                    add_regist["users_registration"].append(p_name)
                else:
                    print('Please enter your name with word')
                    name = input('Enter your full name : ')
                    print(name.isalpha())


                age = int(input("Please enter your age : "))
                if user_check(age):
                    add_regist["users_registration"].append(age)
                else:
                    print('Please enter your age again ')
                    age = int(input("Enter your age : "))


                last_name = input("Enter your last name : ")
                if user_checks(last_name):
                    add_regist["users_registration"].append(last_name)
                else:
                    print('Please enter your last name with word')
                    last_name = input("Enter your last name : ")


                country = input('Enter your country : ')
                if user_checks(country):
                    add_regist["users_registration"].append(country)
                else:
                    print('Please enter your country with word ')
                    country = input('Enter your country :')
                break


            elif option == 2:
                print("Exiting program...")
                break
            else:
                print("Invalid option. Please choose again.")
    except SyntaxError as err:
        print()
    except ValueError as err:
        age = int(input('Please enter your age with numbers : '))
        continue



with open('./users.json', 'a+') as file:
    file.write(json.dumps(add_regist))
    if len(users_data['users']) > 0:
        add_regist['id'] = users_data['users'][-1]['id'] + 1
    else:
        add_regist['id'] = 1