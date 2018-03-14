#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
    max = 1000
    for a in range(1, max//3):
        for b in range(a+1, (max-a)//2):
            c = max-(a+b)
            if a*a+b*b-c*c == 0:
                print(a,b,c)
                print(a*b*c)

if __name__ == '__main__':
    main()
