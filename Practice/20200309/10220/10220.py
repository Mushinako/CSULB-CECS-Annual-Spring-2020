#!/usr/bin/env python3
import sys
from math import factorial


def main():
    for line in sys.stdin:
        n = int(line)
        big_num = factorial(n)
        print(sum((int(x) for x in str(big_num))))


if __name__ == "__main__":
    result = main()
