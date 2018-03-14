#!/usr/bin/python
# -*- coding: utf-8 -*-

# I coded
def main():
    sum = 0
    prev_f = 1
    f = 2
    while f <= 4e+6:
        if f%2 == 0:
            sum += f
        temp = f
        f += prev_f
        prev_f = temp
    print(sum)


# code which calculate sum of sequence E(n)=4*E(n-1)+E(n-2)
def main2():
    num = 4e+6
    a = 2
    b = 8
    sum = a
    while b <= num:
        sum += b
        temp = b
        b = 4*temp + a
        a = temp
    print(sum)


if __name__ == '__main__':
    main()
