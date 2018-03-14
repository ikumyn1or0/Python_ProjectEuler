#!/usr/bin/python
# -*- coding: utf-8 -*-

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

if __name__ == '__main__':
    main()