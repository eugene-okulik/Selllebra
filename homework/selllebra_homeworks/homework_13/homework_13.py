import os

import datetime


homework_dir = os.path.dirname(__file__)
file_dir = os.path.dirname(os.path.dirname(homework_dir))
file_path = os.path.join(file_dir, 'eugene_okulik', 'hw_13', 'data.txt')

print(file_path)


def read_file():
    with open(file_path, encoding="utf-8") as work_file:
        for line in work_file.readlines():
            yield line


for data_line in read_file():
    now = datetime.datetime.now()
    date_format = "%Y-%m-%d %H:%M:%S.%f"
    if data_line.startswith('1'):
        date1 = data_line[3:29]
        date1 = datetime.datetime.strptime(date1, date_format)
        print(date1 + datetime.timedelta(days=7))
    if data_line.startswith('2'):
        date2 = data_line[3:29]
        date2 = datetime.datetime.strptime(date2, date_format)
        print(date2.weekday())
    if data_line.startswith('3'):
        date3 = data_line[3:29]
        date3 = datetime.datetime.strptime(date3, date_format)
        diff = (now - date3)
        print(diff.days)
