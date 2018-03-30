#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    grid = []
    size = 0
    for line in open('011data.txt', 'r'):
        size += 1
        column = []
        for str in line[:-1].split(' '):
            column.append(int(str))
        grid.append(column)
    result = 0
    res_i = 0
    res_j = 0
    # tate
    for i in range(size-3):
        for j in range(size):
            temp = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
            if temp > result:
                res_i = i
                res_j = j
                result = temp
    # yoko
    for i in range(size):
        for j in range(size-3):
            temp = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
            if temp > result:
                res_i = i
                res_j = j
                result = temp
    # naname
    for i in range(size-3):
        for j in range(size-3):
            temp = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
            if temp > result:
                res_i = i
                res_j = j
                result = temp
            temp = grid[i+3][j]*grid[i+2][j+1]*grid[i+1][j+2]*grid[i][j+3]
            if temp > result:
                res_i = i+3
                res_j = j+1
                result = temp
    print(res_i)
    print(res_j)
    print(result)


if __name__ == '__main__':
    main()
