# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
date = list(map(int, input().split()))

day = calendar.weekday(date[-1], date[0], date[1])
print(calendar.day_name[day].upper())
