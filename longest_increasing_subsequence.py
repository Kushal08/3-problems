
import sys


def f(x, y, n):
    a = x
    b = y
    for i in range(0, n-1):
        a, b = b, a + b
    return a

line = sys.stdin.readline()
line = line.split(' ')
print (line)
x = int(line[0])
y = int(line[1])
n = int(line[2])

g = f(x,y,n)
print g
