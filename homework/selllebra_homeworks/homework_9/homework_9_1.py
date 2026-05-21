import datetime


date_from = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(date_from, "%b %d, %Y - %H:%M:%S")

print(datetime.datetime.strftime(python_date, "%B"))
print(datetime.datetime.strftime(python_date, "%d.%m.%Y, %H:%M"))
