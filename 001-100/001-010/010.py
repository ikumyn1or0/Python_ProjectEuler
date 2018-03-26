#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

def check_prime(num, primes):
    prime_flag = True
    for p in primes:
        if p > math.sqrt(num):
            break
        elif num%p == 0:
            prime_flag = False
            break
    return prime_flag

def main():
    primes = [2, 3, 5, 7]
    sum_primes = sum(primes)
    for n in range(10, 2000000):
        if n%2 == 0 or n%3 == 0 or n%5 == 0 or n%7 == 0:
            continue
        else:
            if check_prime(n, primes) == True:
                primes.append(n)
                sum_primes += n
        if len(primes)%100 == 0:
            print(n)
    print(sum_primes)

if __name__ == '__main__':
    main()
