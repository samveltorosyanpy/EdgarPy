a = "Duq @ntrel eq {car_name}"
cars = ['Mercedes', "BMW", "Toyota", "Ford", 'Nisan']

while True:
    user_input = input("Xndrum enq grel meqenayi anun@: - ")

    print(user_input[0])



    if user_input == '/durs':
        break
    elif user_input == "/help":
        print("""
Duq karox eq ogtagorcel hetevyal hramaner@
[/durs] - hraman@ dzez durs khani cragric
[/help] - hraman@ dzez kogni chisht ogtvel cragric
        """)
    else:
        print(f"{user_input} ayspisi hraman goyutyun chuni")

    for x in cars:
        if user_input == x:
             print(a.format(car_name=user_input))
        # else:
        #     print("Meqenan chka bazayum, kam gouytyun chuni")

