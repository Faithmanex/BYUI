students = []

student_name = ''
while student_name != 'end':
    student_name = input('Input name of student: ')
    if student_name != 'end':
        students.append(student_name)

for student in students:
    print(student)