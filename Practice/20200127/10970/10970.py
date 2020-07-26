# /usr/bin/env python3
from sys import stdin


def main():
    for line in stdin:
        m, n = [int(x) for x in line.split()]
        res = m * n - 1
        print(res)


if __name__ == '__main__':
    res = main()
