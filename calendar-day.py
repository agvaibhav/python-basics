import calendar
date=list(map(int,input().split()))
year=date[2]
month=date[0]
day=date[1]
a=calendar.weekday(year,month,day)      
print(calendar.day_name[a].upper())        
