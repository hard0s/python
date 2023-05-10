from math import *


def factorial(x):
    if x == 1:
        return 1
    return factorial(x - 1) * x


def square(x, y):
    c = x * y
    print(c)



def triangleSq(x, y, z):
    c = x + y +z
    p = c /2
    S = sqrt(p *(p-x)*(p-y)*(p-z))
    print(S)

def puas(x, n, p):
    l = n * p
    P1 = l**x / factorial(x)
    p2 = P1 * exp(1)**(-l)
    print('M(x)=', l)
    print('D(x)=', l)
    print('b(x)=', sqrt(l))
    print('P = ', p2)

def binom(x, n, p, q):
    g = n - x
    c1 = factorial(n)
    c2 = factorial(x)
    c3 = factorial(g)
    c4 = c1 / c2
    C = c4 * c3
    # P = C * p**x * q**(n-x)
    p1 = p**x
    p2 = q ** g
    P = C * p1 * p2 
    print('P=', P)
    print('M(x)=', n*p)
    print('D(x)=', n*p*q)
    print('b(x)=', sqrt(n*p*q))









