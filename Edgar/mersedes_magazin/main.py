from cod_creator.registration import creator_login,creator_phone,creator_parol
from Creator_user.user_creator import UserMost
from cod_creator.Creator_Cars import Car_name_creator,Car_date_creator,Car_info_creator,Car_price_creator
from creator_cars.cars_creator import Cars

def grancum():
    print('voxchuyn sireli ogtater: \n')
    print('kayqum grancvelu hamar yntreq grancum hramany:')
    print('1.grancum')
    print('2.mutq ej \n')

def command():
    command = int(input('yntreq tarberaky: - '))

    while True:
        if command == 1:
            login = input('Login: - ')
            creator_login(msg=login)

            phone = input('Phone: (+374) - ')
            creator_phone(msg=phone)

            password = input('Password: - ')
            creator_parol(msg1=password)
            UserMost().users_add(login=login,phone=phone,password=password)
            break

        elif command == 2:
            print('arach gnalu hamar mutqagreq dzer phone ev passwordy')
            phone = input('Phone: (+374) - ')
            while True:
                if phone in UserMost().Creator_user_phone():
                    print('good')
                    break
                else:
                    print('nman hamarov grancvac ogtater goyutyun chuni')
                    phone = input('krkin porceq: (+374) - ')

            password = input('password: - ')
            while True:
                if password in UserMost().Creator_user_password():
                    print('good')
                    print('bari galust Mersedes salon')
                    break
                else:
                    print('nman password goyutyun chuni bazayum')
                    password = input('krkin porceq: - ')
            break
        else:
            print('nman hraman goyutyun chuni')
            command = int(input('krkin porceq: - '))

def cars_magazin():
    print('1. avelacnel meqena')
    print('2. nayel meqenaner')
    print('3. gnel meqena')
    print('4. Het gnal menu')


######################################### KISATA ED JAN
def command_cars():
    command = int(input('yntreq tarberaky: - '))
    while True:
        if command == 1:
            car_name = input('Car name: - ')
            Car_name_creator(msg=car_name)

            car_date = input('Car date: - ')
            Car_date_creator(msg=car_date)

            car_info = input('Car info: - ')
            Car_info_creator(msg=car_info)

            car_price = input('Car price: - ')
            Car_price_creator(msg=car_price)
            Cars().Cars_add_creator(name=car_name,date=car_date,info=car_info,price=car_price)
            break
################################################################

if __name__ == '__main__':
    grancum()
    command()
    cars_magazin()
    command_cars()
