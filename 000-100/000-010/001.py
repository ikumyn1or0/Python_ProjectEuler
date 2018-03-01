#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
    sum = 0
    for n in range(1000):
        if n%3 == 0:
            sum += n
        if n%5 == 0:
            sum += n
        if n%15 == 0:
            sum -= n
    print(sum)

if __name__ == '__main__':
    main()