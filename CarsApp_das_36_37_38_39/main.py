from db.User import UserClass
from validators.register_vals import val_date, val_login, val_password, val_phone
from config import ADMINS
from db.Cars import CarsClass
from validators.cars_validator import create_at,car_name,car_model,car_description

def admin_func():
    while True:
        print("""
1. search car
2. update car
3. delete car
             """)
        choose = input('-> : ')
        if choose == '1':
            print('Greq dzer naxntrac meqenayi anvanumy')

            search = input('search cars name: -> ')
            while True:
                car_data = CarsClass().get_cars_by_name(name=search)
                if car_data:
                    print(car_data)
                    break
                else:
                    print('nman anunov meqena goyutyun chuni porceq mek urish')
                    search = input('krkin porcel: -> ')

        elif choose == '2':

            cars_date = input('date of cars: -> ')
            create_at(msg=cars_date)

            cars_name = input('car name: -> ')
            car_name(msg=cars_name)

            cars_model = input('car model: -> ')
            car_model(msg=cars_model)

            cars_decription = input('car description: -> ')
            car_description(msg=cars_decription)
            CarsClass().creator_new_cars(create_at=cars_date, name=car_name, model=cars_model, description=cars_decription)
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
            password = input("greq dzer parol@: -> ")
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
