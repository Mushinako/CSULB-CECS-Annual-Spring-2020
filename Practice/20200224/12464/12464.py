#!/usr/bin/env python3
def main():
    while True:
        a, b, n = [int(x) for x in input().split()]
        if a == b == n == 0:
            break
        if n % 5 == 0:
            print(a)
            continue
        if n % 5 == 1:
            print(b)
            continue
        if n % 5 == 2:
            print(int((1 + b) / a))
            continue
        if n % 5 == 3:
            print(int((1 + a + b) / (a * b)))
            continue
        if n % 5 == 4:
            print(int((1 + a) / b))
            continue
        raise ValueError()


if __name__ == '__main__':
    res = main()
