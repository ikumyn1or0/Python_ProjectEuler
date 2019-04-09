#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
    power = 2**1000
    result = 0
    while power > 0:
        result = result + power%10
        power = power//10
    print(result)

if __name__ == '__main__':
    main()
