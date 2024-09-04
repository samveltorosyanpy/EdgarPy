# notif = True
#
# def func(x):
#     if x:
#         print("🔔")
#     else:
#         print('🔕')
#
#
# func_l = lambda x: print("🔕") if x is False else print("🔔")


# x = range(1, 10)
# print(list(x))
# x = [i ** 2 for i in range(2, 10, 2)]
#
# print(x)

# l = []
# for i in range(1, 10):
#     l.append(i ** 2)
# print(l)

# func(notif)
# func_l(notif)

tr = map(lambda x: x if x % 2 == 0 else 0, [i for i in range(1, 100)])

print(list(tr))


def trf(l):
    o = list()
    for i in range(len(l)):
        if l[i] % 2 == 0:
            o.append(l[i])
        else:
            o.append(0)
    return o

lists = list()
for i in range(1, 100):
    lists.append(i)

print(trf(lists))

# print(x)

# tr2 = map(
#     lambda x: x ** 2,
#     (5, 6, 3, 7, 2)
# )

# if notif:
#     print("🔔")
# else:
#     print('🔕')


# def functions(n):
#     print(n)

# x = lambda y: print(y)
#
# x(lists)

# s_map = list(map(
#     lambda n: n ** 2,
#     (5, 6, 3, 7, 2)
# ))
#
# print(s_map)
#
#
# lists2 = [5, 6, 3, 7, 2]


# for n in range(len(lists2)):
#     if lists[n] % 2 == 0:
#         continue
#     else:
#         lists2[n] = 0
#
# print(lists2)

