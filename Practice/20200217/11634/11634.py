#!/usr/bin/env python3
def main():
    while True:
        n = input()
        if n == '0':
            break
        t = set()
        t.add(n)
        count = 1
        n = int(n) ** 2
        s = str(n)
        s = '0' * (8 - len(s)) + s
        n = s[2:6]
        while n not in t:
            t.add(n)
            # print('Debug:', count, n, t)
            n = int(n) ** 2
            s = str(n)
            s = '0' * (8 - len(s)) + s
            n = s[2:6]
            count += 1
        print(count)


if __name__ == '__main__':
    res = main()
