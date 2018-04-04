#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
    # 40C20 = 40!/20!/20!
    size = 20
    result = 1
    for i in range(1, size+1):
        result = result*(size+i)/i
    print(int(result))

if __name__ == '__main__':
    main()
