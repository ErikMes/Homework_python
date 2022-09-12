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