#!/usr/bin/python
# -*- coding: utf-8 -*-

def collatz_next(num):
    if num%2 == 0:
        return num//2
    else:
        return 3*num+1

def len_of_collatz_chain(num):
    len = 1
    n = num
    while n != 1:
        n = collatz_next(n)
        len += 1
    return len

def main():
    result = 0
    length_max = 0
    for i in range(1, 1000000):
        length_i = len_of_collatz_chain(i)
        if length_i > length_max:
            length_max = length_i
            result = i
        if (i-1)%10000 == 0:
            print(i)
    print(result)


if __name__ == '__main__':
    main()
