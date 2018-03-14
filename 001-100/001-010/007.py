#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

def main():
    primes_list = [2]
    num = primes_list[-1]+1
    count_flag = True
    while count_flag:
        prime_flag = True
        for n in primes_list:
            if num%n == 0:
                prime_flag = False
        if prime_flag:
            primes_list.append(num)
            num = primes_list[-1]+1
        else:
            num += 1
        if len(primes_list) == 10001:
            count_flag = False
    print(primes_list[-1])

if __name__ == '__main__':
    main()
