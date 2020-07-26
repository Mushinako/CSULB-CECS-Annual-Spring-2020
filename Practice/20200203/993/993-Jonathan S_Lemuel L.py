#!/usr/bin/env python3
def factors(n):
    if n == 1:
        return ['1']
    factors = []
    i = 9
    while n != 1:
        if i < 2:
            return []
        if n % i:
            i -= 1
        else:
            factors.append(str(i))
            n //= i
    return sorted(factors)


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        f = factors(n)
        if f:
            print(''.join(f))
        else:
            print(-1)


if __name__ == '__main__':
    res = main()
