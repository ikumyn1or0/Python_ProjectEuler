#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
    f = open(r'.\001-100\021-030\p022_names.txt', "r", encoding="utf-8")
    file_string = f.read()
    f.close()
    string_list = [s.strip('\"') for s in file_string.split(',')]
    string_list.sort()
    for index, string, in enumerate(string_list):
        


if __name__ == '__main__':
    main()
