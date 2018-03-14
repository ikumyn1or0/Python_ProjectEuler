#!/usr/bin/python
# -*- coding: utf-8 -*-

# I coded
def main():
    sum = 0
    for n in range(1000):
        if n%3 == 0 or n%5 == 0:
            sum += n
    print(sum)


# code which can calculate O(1)
def main2():
    num = 1000 - 1
    sum_to = lambda n: (n*(n+1))//2
    result = 3*sum_to(num//3) + 5*sum_to(num//5) - 15*sum_to(num//15)
    print(result)


if __name__ == '__main__':
    main2()
