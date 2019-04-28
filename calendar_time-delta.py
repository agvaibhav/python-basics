#!/bin/python3

import calendar
from datetime import date

def month_no(month):
    month_list = ['january','february','march','april','may','june','july','august','september','october','november','december']
    for i in month_list:
        if month.lower() in i:
            return(month_list.index(i)+1)

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1 = t1.split()
    t2 = t2.split()

    m1 = month_no(t1[2])
    m2 = month_no(t2[2])

    date1 = date(int(t1[3]),m1,int(t1[1]))
    date2 = date(int(t2[3]),m2,int(t2[1]))

    days_diff = ((date1-date2).days)*24*3600
    
    time1=list(map(int, t1[4].split(':')))
    time2 = list(map(int, t2[4].split(':')))
    time_diff = (time1[0]-time2[0])*3600 + (time1[1]-time2[1])*60 + (time1[2]-time2[2])
    
    if t1[-1][0]==t2[-1][0]:
        zone_diff = abs(int(t1[-1][1:3]) - int(t2[-1][1:3]))*3600 + (abs(int(t1[-1][3:5]) - int(t2[-1][3:5])))*60
        diff = days_diff + time_diff + zone_diff
    
    else:
        zone_diff = abs(int(t1[-1][1:3]) + int(t2[-1][1:3]))*3600 + (abs(int(t1[-1][3:5]) + int(t2[-1][3:5])))*60
    
        if t1[-1][0]=='-':
            diff = days_diff + time_diff + zone_diff
        elif t1[-1][0]=='+':
            diff = days_diff + time_diff - zone_diff

    
    return str(diff)

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
        print(delta)
