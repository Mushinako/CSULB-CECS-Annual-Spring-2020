#!/usr/bin/env python3
import sys


def main():
    for line in sys.stdin:
        n = int(line)
        big_num = 1
        for i in range(2, n + 1):
            big_num = digit_sum(i * big_num)
        print(big_num)


def digit_sum(n):
    return sum((int(x) for x in str(n)))


if __name__ == "__main__":
    result = main()
