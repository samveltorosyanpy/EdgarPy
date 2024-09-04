from db.User import UserClass
from validators.register_vals import val_date, val_login, val_password, val_phone
from config import ADMINS
from db.Cars import Cars



def admin_func():
    while True:
        print("""
1. add car
2. update car
3. delete car
             """)
        choose = input('-> : ')
        if choose == '1':
            print('Greq dzer naxntrac meqenayi anvanumy')

            poisk = input('poisk cars name: -> ')
            while True:
                car_data = Cars().get_cars_by_name(name=poisk)
                if car_data:
                    print(car_data)
                    break
                else:
                    print('nman anunov meqena goyutyun chuni porceq mek urish')
                    poisk = input('krkin porcel: -> ')

        elif choose == '2':
            print('update car')
            break
        elif choose == '3':
            print('delete car')
            break
        else:
            print('no')
            continue

def login():
    login = input("greq dzer login: -> ")
    while True:
        if login in UserClass().get_user_logins():
            password = input("greq dzer parol@")
            if password == UserClass().get_user_password_by_login(login):
                if UserClass().get_user_by_login(login)['id'] in ADMINS:
                    admin_func()
                break
            else:
                print('user interface')
        else:
            print("ayd anunov user goyutyun chuni porceq krkin")
            login = input('Login: -> ')

def register():
    phone = input("greq heraxosahamary: -> ")
    val_phone(phone)
    login = input("stexceq login: -> ")
    val_login(login)
    user_date = input("greq dzer cnndyan amis amsativ@ (YYYY-MM-DD): ->  ")

    if val_date(msg=user_date):
        password1 = input("stexceq parol: -> ")
        password2 = input("krkneq nor paroly: -> ")

        if val_password(password1, password2) is True:
            UserClass().create_now_user(login=login, password=password2, phone=phone, user_date=user_date)
    else:
        return


def start():
    print("""grancvel kam mutq linel
1) login
2) grancvel
    """)
    while True:
        c = input("yntreq: -> ")
        if c == "1":
            login()
            break
        elif c == '2':
            register()
            break
        else:
            print("chka nman hraman skseq noric")



if __name__ == "__main__":
    start()
