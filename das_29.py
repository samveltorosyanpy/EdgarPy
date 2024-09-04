from add_users import add_users

def user_text_log(text):
    return text.isalpha()

def user_int_log(text):
    try:
        int(text)
        return True
    except ValueError as err:
        return False


while True:

    try:
        command = input("/START to begin: ")
        if command == "/START":
            print("Hello! Choose one of the options:")
            print("1. Registration")
            print("2. Exit Program")

            option = int(input("Enter your choice: "))
            if option == 1:
                p_name = input("Please enter your full name: ")
                if user_text_log(p_name):
                    [add_users].append(p_name)
                else:
                    print('Please enter your name with word')
                    name = input('Enter your full name : ')
                    print(name.isalpha)

                age = int(input("Please enter your age : "))
                if user_int_log(age):
                    [add_users].append(age)
                else:
                    print('Please enter your age again ')
                    age = int(input("Enter your age : "))


                last_name = input("Enter your last name : ")
                if user_text_log(last_name):
                    [add_users].append(last_name)
                else:
                    print('Please enter your last name with word')
                    last_name = input("Enter your last name : ")


                country = input('Enter your country : ')
                if user_text_log(country):
                    [add_users].append(country)
                else:
                    print('Please enter your country with word ')
                    country = input('Enter your country :')
                    print('WOW youve done a flawless')
                break
    except ValueError as err:
        print('Please enter your age with number')
        age = int(input('Enter your age :'))


def log_pas_users():
        max_login_lenght = 20
        max_password_lenght = 12
        min_password_lenght = 4
        max_phone_lenght = 8


        while True:
            login = input("Enter a Login : ")[:max_login_lenght]
            password = input("Enter a Password : ")[:max_password_lenght][:min_password_lenght]
            phone = int(input('Enter a phone number: +374-'))[:max_phone_lenght]


            with open("Log_Pas.py", "a") as file:
                file.write(f"{'Login',login},{'Password',password},{'Phone', phone}\n")
            print("Registration successful!")
            break

log_pas_users()