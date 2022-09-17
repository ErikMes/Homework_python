# Ex4
# mydict = {'Anun1':45,'Anun2':69,'Anun3':31}
# def func(x = input('Enter the name--->'), y = int(input('Enter the age--->'))):
#     for i in mydict:
#         if x in mydict and y == mydict[x]:
#             return 'yes'
        
# print(func())

# Ex 5
# import math
# y = '6 * x ** 2 + 10 * x - 1 = 0'
# a = 6
# b = 10
# c = -1
# d = b ** 2 -  4 * a * c
# def func():
#     if d > 0:
#         x1 = (-b + math.sqrt(d)) / 2 * a
#         x2 = (-b - math.sqrt(d)) / 2 * a
#         return x1,x2
#     elif d == 0:
#         x = -b / 2 * a
#         return x
# print(func())Ex 24

# Ex 6
# x = int(input('Enter the number--->'))
# y = int(input('Enter the number--->'))
# z = int(input('Enter the number--->'))
# p = (x + y + z) / 2
# s = (p * (p - x) * (p - y) * (p - z)) * 0.5
# print(s)

# Ex 7
# import time
# import random
# print(f'--------------------------Hi!!!!!!!----------------------, \n---------------Are you ready for the game??------------' )
# x = input('Enter Yes/No---->')
# if x == 'Yes':
#     time.sleep(2)
#     print('---------Well lets start the game-----------')
#     while True:
#         list = ['Rock', 'Paper', 'Scissors']
#         user = input('Enter:  ')
#         pc = random.choice(list)
#         pcpoints = 0
#         userpoints = 0
#         if (user == 'Rock' and pc == 'Scissors') or (user == 'Paper' and pc == 'Rock') or (user == 'Scissors' and pc == 'Paper'):
#             userpoints += 1
#             print(f'user-----{user}, pc-----{pc}, \nuserpoints------{userpoints}, pcpoints----{pcpoints}')
#             print('----------Congratulations you win the game!!!!!!-----------')
#         elif (user == 'Paper' and pc == 'Paper') or (user == 'Rock' and pc == 'Rock') or (user == 'Scissors' and pc == 'Scissors'):
#             print(f'user------------{user}, pc----------{pc}, \nuserpoints-------{userpoints}, pcpoints-------{pcpoints}, \n----------Draw---------')  
#         else:
#             pcpoints += 1
#             print(f'user------{user}, pc---------{pc}, \nuserpoints-------{userpoints}, pcpoints------{pcpoints}')
#             print('----------You failed pc won-----------')
# else:
#     print('---------------Bye---------------')                



# Ex 14
# mydict = {}
# for i in mydict:
#     print(mydict[i])

# Ex 15
# newdict = {}
# mydict = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# x = sorted(mydict, key = mydict.get, reverse = True)[:3]
# for i in x:
#     newdict[i] = mydict[i]
# print(newdict)

# Ex 24
#  a = [1, 2, 3, 4, 5]
# result = 1
# for i in a:
#     result = i * result
# print(result)
