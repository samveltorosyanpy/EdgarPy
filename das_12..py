# food = ['Apelsin', "ananas", "xndzor", "kivi", 'tandz']
#
# x = 0
#
# while x < len(food):
#     print(food[x])
#     x += 1

# k = []
#
# for x in range(1, 100, 2):
#     k.append(x)
#
# print(k)
#
#
# person = {
#     "name": "Alik",
#     "age": 24,
#     "status": "worker"
# }

from test_modul.modul1 import name as j


def calc(name, last_name):
    result = f"hi {name} {last_name}"

    return result

msg = calc("Samvel", "Torosyan")

print(msg)
