#!/usr/bin/python
# -*- coding: utf-8 -*-

def score(string):
    result = 0
    for char in string:
        result = result + ord(char)-ord('A')+1
    return result

def main():
    f = open(r'.\001-100\021-030\p022_names.txt', "r", encoding="utf-8")
    file_string = f.read()
    f.close()
    string_list = [s.strip('\"') for s in file_string.split(',')]
    string_list.sort()
    result = 0
    for index, string in enumerate(string_list):
        result = result + (index+1)*score(string)
    print(result)

if __name__ == '__main__':
    main()
