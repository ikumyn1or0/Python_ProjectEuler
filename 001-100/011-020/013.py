#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
    data = []
    for line in open('013data.txt', 'r'):
        column = []
        for s in line[:-1]:
            column.append(int(s))
        data.append(column)
    result_backward = []
    digit = 0
    for j in range(49, -1, -1):
        for i in range(0, 100):
            digit += data[i][j]
        result_backward.append(digit%10)
        digit = digit//10
    result_backward.append(digit)
    result_string = ""
    for d in reversed(result_backward):
        result_string = result_string + str(d)
    print(result_string[0:10])

if __name__ == '__main__':
    main()
