# /usr/bin/env python3
def factor(n):
    i = 2
    res = []
    while True:
        if i * i > n:
            if n != 1:
                res.append(str(n))
            return res
        if n % i:
            i += 1
        else:
            res.append(str(i))
            n //= i


def smith(n):
    while True:
        n += 1
        factors = factor(n)
        if len(factors) == 1:
            continue
        if sum(int(x) for x in str(n)) == sum(int(x) for x in ''.join(factors)):
            return n


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        res = smith(n)
        print(res)


if __name__ == '__main__':
    res = main()
