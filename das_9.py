# amisner = {
#     '1': "hunvar",
#     '2': 'petrvar',
#     '3': "mart",
#     '4': 'april',
#     '5': 'mayis',
# }
#
# for x in amisner:
#     amis = amisner[x]
#     print(amis)
#     if amis == "mart":
#         for y in range(1, 32):
#             if y == 28:
#                 print("Dzer cnundy shorhavor")


f = lambda x: x + 2

g = [y := f(3), y ** 2, y ** 3]
print(g)

a = [[1, 2, ], [3, 4]]

a.append([5, 6])
print(a)
