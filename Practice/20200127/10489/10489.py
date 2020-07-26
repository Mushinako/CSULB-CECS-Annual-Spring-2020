# /usr/bin/env python3
from math import prod


def main():
    t = int(input())
    for _ in range(t):
        n, b = [int(x) for x in input().split()]
        tot = 0
        for _ in range(b):
            tot += prod([int(x) for x in input().split()[1:]]) % n
        print(tot % n)


if __name__ == '__main__':
    res = main()
