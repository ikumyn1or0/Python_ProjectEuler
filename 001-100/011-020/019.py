#!/usr/bin/python
# -*- coding: utf-8 -*-

def count_days_in(year, month):
    if month in [4,6,9,11]:
        return 30
    elif month == 2:
        if year%400 == 0:
            return 29
        elif year%100 == 0:
            return 28
        elif year%4 == 0:
            return 29
        else:
            return 28
    else:
        return 31

weeks = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

def main():
    # 1990年12月31日の曜日を計算
    week_1900 = 0
    for month in range(1, 12+1):
        week_1900 += count_days_in(1900, month)
    days = week_1900%7
    count = 0
    for year in range(1901, 2000+1):
        for month in range(1, 12+1):
            if days%7 == 6:
                print(year, month)
                count += 1
            days += count_days_in(year, month)
    print(count)

if __name__ == '__main__':
    main()
