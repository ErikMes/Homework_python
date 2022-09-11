# calculator
def gumarum(a:int, b:int):
    x = a + b
    return x
def hanum(a:int, b:int):
    x = a - b
    return x
def bazmapatakum(a:int, b:int):
    x = a * b
    return x
def bajanum(a:int, b:int):
    x = a / b
    return x
def armat(a):
    x = a ** 0.5
    return x
def astichan(a, b):
    x = a ** b
    return x
def logaritm(a, b):
    y = 1
    while  b != int(round(a ** y)):
            y += 0.1
    return int(round(y))
def floor(a):
    return int(a)
def ceil(a):
    return int(a + 1)


