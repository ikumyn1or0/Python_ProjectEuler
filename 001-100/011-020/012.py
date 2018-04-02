#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

def count_divisors(num):
    count = 0
    for d in range(1, int(math.sqrt(num))):
        if num%d == 0:
            count += 2
    return count

def triangle_num(i):
    return i*(i+1)//2

def main():
    i = 2
    while count_divisors(triangle_num(i)) < 500:
        i += 1
    print(triangle_num(i))

if __name__ == '__main__':
    main()
