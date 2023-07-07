def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  res = is_leap(year)
  if res == True:
      if month == 2:
        days_in_month = month_days[month - 1] + 1
        return days_in_month
      else:
          days_in_month = month_days[month - 1]
          return days_in_month
  else:
      days_in_month = month_days[month - 1]
      return days_in_month
    

  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







