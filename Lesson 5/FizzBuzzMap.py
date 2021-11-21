file1 = 'fizzbuzz.txt'
file2 = 'void.txt'
f1 = open(file1, 'r')
f2 = open(file2, 'w')
i = 0
for line in f1:
    fizz, buzz, number3 = list(map(int, line.split()))
    for i in range(0, number3):
        i = i + 1
        if i % fizz == 0 and i % buzz == 0:
            f2.write(' FB ')
        elif i % fizz == 0:
            f2.write(' F ')
        elif i % buzz == 0:
            f2.write(' B ')
        else:
            f2.write(str(i))
    f2.write('\n')
f1.close()
f2.close()