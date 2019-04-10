#!/usr/bin/python
# -*- coding: utf-8 -*-

from copy import copy

def main():
    # リストに格納
    number_list = []
    for i in range(1, 100):
        number_list.append(i)
    flag = True
    while flag:
        flag = False
        # 2の倍数*5の倍数をまとめる
        flag25 = False
        index_2 = -1
        index_5 = -1
        for index, number in enumerate(number_list):
            if number%2 == 0 and number%10 != 0:
                index_2 = index
                continue
            if number%5 == 0 and number%10 != 0:
                index_5 = index
                continue
        if index_2 >= 0 and index_5 >= 0:
            flag25 = True
            number_list[index_2] *= copy(number_list[index_5])
            number_list[index_5] = 1
        # 10の倍数を簡単にする
        flag10 = False
        for index, number in enumerate(number_list):
            if number%10 == 0:
                flag10 = True
                number_list[index] = number//10
        flag = flag10+flag25

    digits = 1
    for number in number_list:
        digits *= number
    result = 0
    while digits > 0:
        result += digits%10
        digits = digits//10
    print(result)

if __name__ == '__main__':
    main()
