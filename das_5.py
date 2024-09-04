# lists = [0,1,2]
# tuples = (0,1,2)
# sets = {0,1,2}
#
# lists[0] = 1
# # tuples[0] = 1
#
# # print(id(lists))
# # print(tuples)
# # print("list", lists)
#
# RAM = {
#     "firsName": "Samvel",
#     "lastname": "Torosyan",
#     "age": 23
# }
#
# print(id(RAM))
#
# RAM['address'] = "Moskovyan 3"
#
# print(id(RAM))
#
# print(RAM)
#
#
# # print(name)
# # print(tuple(lists))
# # print(list(tuples))
# # print(tuple(sets))
# #
# # print(dict(RAM))
#
# name = "Edgar"
#
# print(id(name))
#
# name = name + " Lrjikyan"
#
# print(id(name))
#
# print(name)
# print("_____________________________________________________________")
#
# lastName = 'e' + name[1:5]
#
# print(lastName)


cars_list = ['mersedes', 'bmw', 'cemry', 'ford', 'toyota', 'tesla']
cars_tuple = ('mersedes', 'bmw', 'cemry', 'ford', 'toyota', 'tesla')
cars_set = {'mersedes', 'bmw', 'cemry', 'ford', 'toyota', 'tesla'}

count = 1

for item in cars_list:
    car_name = item.upper()
    print(f"{count}")

    count = count + 1

