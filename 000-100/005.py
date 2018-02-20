#!/usr/bin/python
# -*- coding: utf-8 -*-

def lcm(a, b):
    if a > b:
        large = a
        small = b
    else:
        large = b
        small = a
    while small > 0:
        temp = large%small
        large = small
        small = temp
    return large

def main():
    result = 1
    for i in range(1, 20+1):
        if result%i != 0:
            result = result * i // lcm(result, i)
    print(result)

if __name__ == '__main__':
    main()