l = list(range(2 , 10))
def square(x):
    i = 2
    while x % i != 0:
        i = i + 1
        if x == i:
            return i*i
print(list(map(square, l)))