# Make a programme that calculates an average height from the list of heights
# YOU ARE NOT ALLOWED TO USE SUM() AND LEN() FUNCTIONS!
student_heights = input("Input a list of student height\n").split()
student_heights_number = 0  # Total number of student heights
sum_student_height = 0  # A sum of student heights
for student_height in student_heights:
    student_heights_number += 1
    sum_student_height += int(student_height)

average_height = round(sum_student_height/student_heights_number)
print(f"The average height of  {student_heights_number} students is {average_height}")
