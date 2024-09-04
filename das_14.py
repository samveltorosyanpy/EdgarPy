# def makeres(erkarutyun=5, laynutyun=5):
#     res = erkarutyun * laynutyun
#     return res
#
#
# mak = makeres(3, 7)
# print(mak)
#
#
# def hashiv(num):
#     return num ** 2
#
#
# num = hashiv(7)
# print(num)


def xndir(num, num1, op='+'):
    if op == '*':
        return num * num1
    elif op == '+':
        return num + num1
    elif op == '/':
        return num / num1
    elif op == '-':
        return num - num1
    else:
        print('sxal voronum')
        exit()


# print(xndir(num=5, num1=6, op='*'))
# print(xndir(num=15, num1=17))

clas = [6, 7, 8, 5, 4, 4, 5, 6]

for x in clas:
    print(x)

while True:
    print(1)