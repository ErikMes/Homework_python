# calculator
# def gumarum(a:int, b:int):
#     x = a + b
#     return x
# def hanum(a:int, b:int):
#     x = a - b
#     return x
# def bazmapatakum(a:int, b:int):
#     x = a * b
#     return x
# def bajanum(a:int, b:int):
#     x = a / b
#     return x
# def armat(a):
#     x = a ** 0.5
#     return x
# def astichan(a, b):
#     x = a ** b
#     return x
# def logaritm(a, b):
#     y = 1
#     while  b != int(round(a ** y)):
#             y += 0.1
#     return int(round(y))
# def floor(a):
#     return int(a)
# def ceil(a):
#     return int(a + 1)
# def max(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# def gumarum1(a, b):
#     return a + b
# def multiply(a, b, c, d):
#     return(a * b * c * d)
# def string() -> list:
#     y = []
#     x = input('Enter the string--->')
#     for i in x:
#         y = y.append(i)
#         return y
# print(string())

# slide ex
# Ex 1
# newlist = []
# def func(x = int(input('Enter the number--->')), y = int(input('Enter the number--->')), z = int(input('Enter the number--->'))):
    # for i in range(x, y, z):
        # newlist.append(i)
    # return newlist
# print(func())

# Ex 2
# newlist = []
# mylist = [12, 3, 4, 25, 0, 89, 31, 6]
# def func():
    # for i in range(0, len(mylist) - 1):
        # newlist.append(mylist[i] * mylist[i + 1])
    # return newlist
# print(func())

# Ex 3

# Ex 4
# newlist = []
# def func():
    # x = ['Python', 'Ai', 'Django', 'Programming']
    # for i in x:
        # m = len(i)
        # newlist.append(m)
        # n = max(newlist)
        # l = min(newlist)
        # z = n + l
    # return z    
# print(func())

# Ex 5
# mylist = [45, 23, 2, 98, 65, 34, 2, 67, 3658, 78, 123]
# def func(x = int(input('Enter the number--->'))):
#     for i in mylist:
#         if i == x:
#             return('Yes,the number is in the list')
#     else:
#         return('No, the nuber is not in the list')
# print(func())


# Ex 7
# def func():
    # mydict = {}
    # mylist = [1, 65, 23]
    # for i in mylist:
        # if i not in  mydict:
            # mydict = {i: i ** 2}
    # return mydict
# print(func())


# Ex 27
# mylist = [1, 6, 2, 2, 2, 7, 2]
# val = 2
# for i in mylist[:]:
    # if i == val:
        # mylist.remove(i)
# print(mylist)

# import random
# y = []
# mylist = [1, -1, 0, 2, 1]
# x = random.choice(mylist)
# y.append(x)
# while True:
    # if len(y) == 4:
        # print(y)
      


