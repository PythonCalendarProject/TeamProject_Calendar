import datetime,time

date_test = datetime.date.today()

date_test_day = date_test.day
date_test_month=date_test.month
date_test_year=date_test.year

date_test_start = datetime.date(date_test.year, date_test.month,1)

date_test_start_point = date_test_start.weekday()
print(date_test_start_point)

