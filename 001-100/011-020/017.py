#!/usr/bin/python
# -*- coding: utf-8 -*-

def count_letters(number):
    letters1_9 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]# [0, 1, ..., 9]
    letters10_19 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]# [10, 11, ..., 19]
    letters20_90 = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]# [0, 0, 20, 30, ..., 90]
    string = ""
    if number >= 1000:
        string = string + letters1_9[(number//1000)%10] + "thousand"
    if number%1000 >= 100:
        string = string + letters1_9[(number//100)%10] + "hundred"
        if number%100 != 0:
            string = string + "and"
    if number%100 >= 20:
        string = string + letters20_90[(number//10)%10] + letters1_9[number%10]
    elif number%100 >= 10:
        string = string + letters10_19[(number%100)-10]
    else:
        string = string + letters1_9[number%10]
    return len(string)

def main():
    result = 0
    for i in range(1, 1001):
        result = result + count_letters(i)
    print(result)

if __name__ == '__main__':
    main()
