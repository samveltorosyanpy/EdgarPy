age = 25
name = 'Samvel'
city = "AMN"

def country(f_age, f_name, f_city):
    print("Edgar: {age}, {name}, {city}".format(age=f_age, name=f_name, city=f_city))

# country(age, name, city)



def country(f_age, f_name, f_postcode="0001", f_city="Yerevan"):
    print("Edgar: {age}, {name}, {city}, {postcode}".format(age=f_age, name=f_name, city=f_city, postcode=f_postcode))

# country(f_age=age, f_name=name, f_city=city)


# print('Samvel', "Torosyan", end='+')
# print('Samvel +', "Torosyan", sep='_')
# print('Samvel', "Torosyan")

# def fprint(end, *args):
#     args_list = list(args)
#     print(args_list[1])
#     print(args)
#     print(end)
#
#
# fprint('Junior', 'middle', 'sinor', 1, 5, 6, 5, 1)


# def price_muxloj(*args, pluse=10):
#     for x in args:
#         print(x + pluse)


# price_muxloj(450, 680, 325, 754, pluse=15)

def args_kwargs(*args, price, **kwargs):
    print("p", price)
    print("*args", args)
    print("**kwargs", kwargs)

args_kwargs(6, 7, 8, 1, 3, name="Samvel", lastName="Torosyan", age=25, price=99)

