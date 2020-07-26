#!/usr/bin/env python3
import math


def is_prime(n, known_primes):
    top = math.floor(math.sqrt(n))
    for i in (x for x in known_primes if x <= top):
        if not n % i:
            return
    known_primes.append(n)


def main():
    end = int(input('Upper limit: '))
    primes = [2, 3]
    try:
        for n in range(4, end):
            is_prime(n, primes)
    except KeyboardInterrupt:
        print(n)
    # print(primes)
    print(len(primes))
    print(sum(primes))


if __name__ == "__main__":
    res = main()
