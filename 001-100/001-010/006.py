#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
    result = 0
    N = 100
    for i in range(1, N):
        for j in range(i+1, N+1):
            result += i*j*2
    print(result)

if __name__ == '__main__':
    main()
