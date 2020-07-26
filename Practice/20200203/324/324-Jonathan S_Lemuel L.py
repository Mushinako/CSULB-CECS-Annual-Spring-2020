#!/usr/bin/env python3
from math import factorial


def main():
    n = int(input())
    while n:
        prod = str(factorial(n))
        result = '{}! --\n'.format(n)
        for i in range(5):
            result += '   ({})'.format(i) + \
                '{:>5}'.format(prod.count(str(i))) + ' '
        result = result.rstrip() + '\n'
        for j in range(5):
            i = 5 + j
            result += '   ({})'.format(i) + \
                '{:>5}'.format(prod.count(str(i))) + ' '
        result = result.rstrip()
        print(result)
        n = int(input())


if __name__ == '__main__':
    main()
