#Task 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

#Task 2
line1 = 'результат операции: 42'
index_start = line1.index(':')
number = int(line1[index_start+2:])+10
print(number)

line2 = 'результат операции: 514'
index_start = line2.index(':')
number = int(line2[index_start+2:])+10
print(number)

line3 = 'результат работы программы: 9'
index_start = line3.index(':')
number = int(line3[index_start+2:])+10
print(number)

#Task 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students_list = ', '.join(students)
subjects_list = ', '.join(subjects)
print(f'Students {students_list} study these subjects: {subjects_list}')