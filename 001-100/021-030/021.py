#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

def divisor(num):
    result = 1
    for n in range(2, math.floor(math.sqrt(num))+1):
        if num%n == 0:
            result = result + n + num // n
    return result

if __name__ == "__main__":
    result = 0
    for n in range(2, 10000):
        if divisor(n) < n:
            if divisor(divisor(n))==n:
                result = result + n + divisor(n)
    print(result)
