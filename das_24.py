data = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "batters":
        {
            "batter1":
                [
                    {"id": "1001", "type": "Regular"},
                    {"id": "1002", "type": "Chocolate"},
                    {"id": "1003", "type": "Blueberry"},
                    {"id": "1004", "type": "Devil's Food"}
                ],
            "batter2":
                [
                    {"id": "1001", "type": "Regular"},
                    {"id": "1002", "type": "Chocolate"},
                    {"id": "1003", "type": "Blueberry"},
                    {"id": "1004", "type": "Devil's Food"}
                ]
        },
    "topping":
        [
            {"id": "5001", "type": "None"},
            {"id": "5002", "type": "Glazed"},
            {"id": "5005", "type": "Sugar"},
            {"id": "5007", "type": "Powdered Sugar"},
            {"id": "5006", "type": "Chocolate with Sprinkles"},
            {"id": "5003", "type": "Chocolate"},
            {"id": "5004", "type": "Maple"}
        ]
}


# for x in range(1, 6):
#     print(x)

# count = 1

# for x in data['topping']:
#     print(x, type(x))
#
#     print(x.keys(), type(x.keys()))
#
#
#     print(list(x.keys()), type(list(x.keys())), '\n')
#
#     print(list(x.keys())[0])
#     print(count)
#     count = count + 1



def norma(qash, boy):
    return boy // qash


normal = lambda qash, boy: boy // qash

user_data = {
    "qash": 43,
    "boy": 176,
    "norma": normal(43, 176)
}

print(user_data)
