# Ex 85

# def func(x = float(input('Enter the number--->')), y = float(input('Enter the number--->'))):
    # z = ((x ** 2) + (y ** 2)) ** 0.5
    # return z
# print(func())

# Ex 86
# def func(x = float(input('Enter the number--->'))):
    # y = x * 1000
    # z = 4 + (int(y / 140) * 0.25)
    # return z
# print(f'{func()}$')

# Ex 87
# def func(x = int(input('Enter the number--->'))):
    # if x > 1:
        # y = ((x - 1) * 2.95) + 10.95
        # return y
# print(f'{func()}$')

# Ex 88
# def func(x = int(input('Enter the number--->')), y = int(input('Enter the number--->')), z = int(input('Enter the number--->'))) -> int:
#     if x > y > z:
#         return y
#     elif y > x > z:
#         return x
#     elif x > z > y:
#         return z
#     elif y > z > x:
#         return z
#     elif z > x > y:
#         return x
#     elif z > y > x:
#         return y
# print(func())

# Ex 89
# z = {1:'first', 2:'second', 3:'third', 4:'fourth', 5:'fifth', 6:'sixth', 7:'seventh', 8:'eight', 9:'ninth', 10:'tenth', 11:'eleventh', 12:'tweleweth'}
# def func(x = int(input('Enter the number--->'))):
#     # for i in z:
#     if x in z.keys():
#         return z[x]
# print(func())

# Ex 90
# z = {
    # 1:'On the first day of Christmas'
# }

# Ex 91
# import calendar
# leap_year = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
# non_leap_year = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
# def func(x = int(input('Enter the year--->')), y = int(input('Enter the month--->')),z = int(input('Enter the day--->'))):
#     if calendar.isleap(x):
#         sum = 0
#         for i in leap_year:
#             if i in range(1, y ):
#                 sum += leap_year[i] 
#         return sum + z
#     else:
#         sum = 0
#         for i in non_leap_year:
#             if i in range(1, y):
#                 sum += non_leap_year[i]
#         return sum + z
# print(func())

# Ex 92
# import calendar
# leap_year = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
# non_leap_year = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
# month = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
# def func(x = int(input('Enter the year--->')), y = int(input('Enter the number--->'))):
#     if calendar.isleap(x):
#         if y in range(1,32):
#             return month[1],y
#         if y in range(32, 62):
#             return month[2], y - leap_year[1]
#         if y in range(62, 94):
#             return month[3], y - leap_year[1] - leap_year[2]
#         if y in range(94, 115):
#             return month[4], y - leap_year[1] - leap_year[2] - leap_year[3]
#         if y in range(115, 147):
#             return month[5], y - leap_year[1] - leap_year[2] - leap_year[3] - leap_year[4]
#         if y in range(147, 178):
#             return month[6], y - leap_year[1] - leap_year[2] - leap_year[3] - leap_year[4] - leap_year[5]
#         if y in range(178, 210):
#             return month[7], y - leap_year[1] - leap_year[2] - leap_year[3] - leap_year[4] - leap_year[5] - leap_year[6]
#         if y in range(210, 242):
#             return month[8],y - leap_year[1] - leap_year[2] - leap_year[3] - leap_year[4] - leap_year[5] - leap_year[6] - leap_year[7]
#         if y in range(242, 273):
#             return month[9],y - leap_year[1] - leap_year[2] - leap_year[3] - leap_year[4] - leap_year[5] - leap_year[6] - leap_year[7] - leap_year[8]
#         if y in range(273, 305):
#             return month[10],y - leap_year[1] - leap_year[2] - leap_year[3] - leap_year[4] - leap_year[5] - leap_year[6] - leap_year[7] - leap_year[8] - leap_year[9]
#         if y in range(305, 336):
#             return month[11],y - leap_year[1] - leap_year[2] - leap_year[3] - leap_year[4] - leap_year[5] - leap_year[6] - leap_year[7] - leap_year[8] - leap_year[9] - leap_year[10]
#         if y in range(336, 367):
#             return month[12],y - leap_year[1] - leap_year[2] - leap_year[3] - leap_year[4] - leap_year[5] - leap_year[6] - leap_year[7] - leap_year[8] - leap_year[9] - leap_year[10] - leap_year[11]
#     else:        
#         if y in range(1,32):
#             return month[1],y
#         if y in range(32, 62):
#             return month[2], y - non_leap_year[1]
#         if y in range(62, 94):
#             return month[3], y - non_leap_year[1] - non_leap_year[2]
#         if y in range(94, 115):
#             return month[4], y - non_leap_year[1] - non_leap_year[2] - non_leap_year[3]
#         if y in range(115, 147):
#             return month[5], y - non_leap_year[1] - non_leap_year[2] - non_leap_year[3] - non_leap_year[4]
#         if y in range(147, 178):
#             return month[6], y - non_leap_year[1] - non_leap_year[2] - non_leap_year[3] - non_leap_year[4] - non_leap_year[5]
#         if y in range(178, 210):
#             return month[7], y - non_leap_year[1] - non_leap_year[2] - non_leap_year[3] - non_leap_year[4] - non_leap_year[5] - non_leap_year[6]
#         if y in range(210, 242):
#             return month[8],y - non_leap_year[1] - non_leap_year[2] - non_leap_year[3] - non_leap_year[4] - non_leap_year[5] - non_leap_year[6] - non_leap_year[7]
#         if y in range(242, 273):
#             return month[9],y - non_leap_year[1] - non_leap_year[2] - non_leap_year[3] - non_leap_year[4] - non_leap_year[5] - non_leap_year[6] - non_leap_year[7] - non_leap_year[8]
#         if y in range(273, 305):
#             return month[10],y - non_leap_year[1] - non_leap_year[2] - non_leap_year[3] - non_leap_year[4] - non_leap_year[5] - non_leap_year[6] - non_leap_year[7] - non_leap_year[8] - non_leap_year[9]
#         if y in range(305, 336):
#             return month[11],y - non_leap_year[1] - non_leap_year[2] - non_leap_year[3] - non_leap_year[4] - non_leap_year[5] - non_leap_year[6] - non_leap_year[7] - non_leap_year[8] - non_leap_year[9] - non_leap_year[10]
#         if y in range(336, 367):
#             return month[12],y - non_leap_year[1] - non_leap_year[2] - non_leap_year[3] - non_leap_year[4] - non_leap_year[5] - non_leap_year[6] - non_leap_year[7] - non_leap_year[8] - non_leap_year[9] - non_leap_year[10] - non_leap_year[11]
# print(func())
        




# Ex 94
# def func(x = int(input('Enter the number--->')), y = int(input('Enter the number--->')), z = int(input('Enter the number--->'))) -> int:
#     if x >= y + z:
#         return False
#     elif y >= x + z:
#         return False
#     elif z >= x + y:
#         return False
#     else:
#         return True
# print(func()) 

# Ex 95


# z = '!?.'
# def func(x = input('Enter the text--->')):
    # y = x[0].upper()
    # for i in x:
        # if i in z:
            # print(x.upper())
        # return y + x[1 :]
# print(func())
# Ex 96
# def func(x = input('Enter the sentence--->')):
#     x = x.strip()
#     if x[0] == '+' or x[0] == '-' and x[1:].isdigit():
#         return True
#     else:
#         return False
# print(func())

# Ex 97
# y = []
# def func(x = input('Enter the sentence---')):
#     for i in x:
#         if i == '+' or i == '-':
#             y.append(1)
#             # print(y)            
#         elif  i == '/' or i == '*':
#             y.append(2)
#             # print(y)
#         elif i == '^':
#             y.append(3)
#             # print(y)    
#     else:
#         print(-1)
#     return y        
# print(func())



# Ex 98
# def func(x = int(input('Enter the number--->'))):
    # if x > 3 and x % 2 != 0 and x % 3 != 0:
        # return True
    # elif 1 < x <= 3:
        # return True
    # else:
        # return False
# print(func())

# Ex 99
# def func(x = int(input('Enter the number--->'))):
#     for i in range(1, 1000000000):
#         if i > x and i % 2 != 0 and i % 3 != 0:
#             return i 
#         elif x == 3:
#             return 3        
# print(func())

# # Ex 100

# import random 
# y = []
# def func(x = random.randint(ord('!'), ord('~'))):
    
# print(func())

# x = random.randint(ord('!'), ord('~'))
# print(x)

# Ex 108

def func(x = int(input('Enter the number of teaspoons--->'))):
    m = 0
    n = 0
    l = 0
    while True:
        if x > 48 and x - 48 > 48:
            m += 1
        elif x < 48 and x - 3 > 3:
            n += 1
        elif x < 3:
            l += x
            return m,'cups', n, 'tablespoons', l,'teaspoons'
        else:
            print(func())
# EX 109
# mydict = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6, 'july':7, 'august':8, 'september':9, 'october':10, 'november':11, 'december':12}
# def func(x = input('Enter the year--->'), y = input('Enter the month--->'), z = int(input('Enter the day--->'))):
#     m = int(x[2:])
#     for i in mydict:
#         if y in mydict and mydict[y] * z == m:    
#             return 'Yes, this date is magic'
#         else:
#             return 'No, the date does not magic'
# print(func())