a = "Duq @ntrel eq {car_name}"
cars = ['Mercedes', "BMW", "Toyota", "Ford", 'Nisan']

def command_hend(command):
    if command == "/help":
        print("""
    Duq karox eq ogtagorcel hetevyal hramaner@
    [/durs] - hraman@ dzez durs khani cragric
    [/help] - hraman@ dzez kogni chisht ogtvel cragric
    [/add] - hramany avelacnum e meqema /add [car_name]
            """)
    if "/add" in command:
        new_car = command[5:]
        cars.append(new_car)
        print("Meqenan hajoxabar avelacav")
    else:
        print(f"{command} ayspisi hraman goyutyun chuni")



while True:
    user_input = input("Xndrum enq grel meqenayi anun@: - ")

    if user_input[0] == '/':
        if user_input == '/durs':
            break

        command_hend(user_input)

    elif user_input in cars:
        for x in cars:
            if user_input == x:
                 print(a.format(car_name=user_input))
            else:
                continue
    else:
        print("Meqenan chka bazayum, kam gouytyun chuni")


