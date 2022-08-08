# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg=student_marks[query_name][0]+student_marks[query_name][1]+student_marks[query_name][2]
    final=avg/3
    res = "{:.2f}".format(final)
    print(res)
