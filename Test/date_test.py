import datetime

print(datetime.date(2011,11,11))

print(datetime.date.today())

new_date = datetime.date(2018,10,25)

# select_day = datetime.date.fromtimestamp(new_date)

print(new_date.isoweekday()) #4?????
print(new_date.weekday())#3?????



