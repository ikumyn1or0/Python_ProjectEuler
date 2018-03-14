#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

def main():
    n = 600851475143
    result = 1
    for i in range(2, int(np.sqrt(n))):
        while n%i == 0:
            result = i
            n = n//i
    print(result)

if __name__ == '__main__':
    main()
