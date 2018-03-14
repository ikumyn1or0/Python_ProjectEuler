#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

def is_palnum(num):
    digits = int(np.log10(num))+1
    result = True
    for i in range(digits//2):
        large = (num//10**(digits-1-i))%10
        small = (num//10**i)%10
        if large != small:
            result = False
    return result

def main():
    res_a = 0
    res_b = 0
    result = 0
    for a in range(999, 900, -1):
        for b in range(a, 900, -1):
            temp = a*b
            if is_palnum(temp) and result < temp:
                res_a = a
                res_b = b
                result = temp
    print(res_a)
    print(res_b)
    print(result)

if __name__ == '__main__':
    main()
