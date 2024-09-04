text = "Hello World"  # string, str
text2 = 'Hello World Hello World'
text3 = """
Hello World
Hello World
Hello World
Hello World
Hello World
"""

numb = 10  # int, integer
floats = 1.10  # float
boolian1 = False  # bool
boolian2 = True  # bool
undefind = None  # None Type

list1 = ['Anush', "Grigoryan", '096453726']  # List
list2 = ("Hello World", 10, False, 0.3)  # tuple
list3 = {"age": 25, "name": 'Samvel', 'man': True}  # dict
list4 = {1, 2, 3, 4, 5, 5}  # set {1, 2, 3, 4, 5}

print(type(text))
print(type(numb))
print(type(floats))
print(type(boolian1))
print(type(boolian2))
print(type(undefind))
print(type(list1))
print(type(list2))
print(type(list3))
print(type(list4))

# print(list3["age"])

# result = f"""
# name: {list1[0]}
# surname: {list1[1]}
# phone: {list1[2]}
# """
#
# print(result)

#
# print()
#
# text = "Hello World"
#
# print(text[0:5])


# Ստեխծել փոփոխականեր lastname որի մեջ կլինի անուն և surname որի մեջ կլինի ազգանուն
# տպիր այտ տեռմինալում
# output: Armen Galstyan
# ինֆորմացիայի տեսակը իմանալու համար ոգտագործվում է type ֆունկցիան օգտագործիր այն տպելով բոլոր քո իմացած ինֆորմացիայի տեսակները
# Օրինակ type(text)
# output
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# <class 'NoneType'>
# <class 'list'>
# <class 'tuple'>
# <class 'dict'>
# <class 'set'>
# Ստեխծել փոփոխականեր numbers որի մեջ կլինի "0123456789" և տպել նրա 6, 8, 3 թվերը, ինդեկսների օգնությամբ
# Օրինակ print(numbers[1]) output: 1


name = 'Armen'
name1 = 'Galstyan'
print(name + name1)

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list[6])
print(list[8])
print(list[3])

list = ['Edgar', 'Lrjikyan', 'edgar.lrjikyan.03@mail.ru', 'shahumyan 4rd poxoc 71 tun']
result = f"""
name: {list[0]}
surname: {list[1]}
mail: {list[2]}
address: {list[3]}
"""
print(result)

x = 10
print(type(x))  # output: <class 'int'>
y = 3.14
print(type(y))  # output: <class 'float'>
name = 'John'
print(type(name))  # output: <class 'str'>
numbers = [1, 2, 3, 4, 5]
print(type(numbers))
person = {'name': 'john', 'age': 30}
print(type(person))
is_valid = True
print(type(is_valid))
