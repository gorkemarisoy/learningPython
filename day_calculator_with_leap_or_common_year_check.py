leap = [31,29,31,30,31,30,31,31,30,31,30,31]
common = [31,28,31,30,31,30,31,31,30,31,30,31]

def is_year_leap(year):
    if (year%4) == 0 and (year%100)!= 0 or year%400==0:
        return True
    else:
        return False


def days_in_month(year, month):
    if is_year_leap(year)==True:
        return leap[month-1]
    if is_year_leap(year)==False:
        return common[month-1]


def day_of_year(year, month, day):
    if year <=0 and month <=0 or month >=13 and day <=0 or day >=32:
        return
    
    günler = []
    s=0
    for i in range(month-1):
        günler.insert(0,days_in_month(year,i))
    for j in range(len(günler)):
        s+=günler[j]
    return s+day
    


print(day_of_year(2001, 12, 30))
