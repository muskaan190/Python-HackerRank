# Dr. John Wesley has a spreadsheet containing a list of student's name,marks,class and Ids .
# Your task is to help Dr. Wesley calculate the average marks of the students.


from collections import namedtuple
n = int(input())
a = input()
total = 0
Student = namedtuple('Student', a)
for _ in range(n):
    student = Student(*input().split())
    total += int(student.MARKS)
print('{:.2f}'.format(total/n))


