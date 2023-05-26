year, month, day = map(int, input().split())
count_year, count_month, count_day = map(int, input().split())
man_old = 0
if month < count_month:
    man_old = count_year-year
elif month == count_month:
    if day <= count_day:
        man_old = count_year-year
    else:
        man_old = count_year-year-1
else:
    man_old = count_year-year-1
count_old = count_year-year+1
year_old = count_year-year
print(man_old)
print(count_old)
print(year_old)
