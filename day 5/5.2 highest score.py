# Find the highest score in the list
# YOU ARE NOT ALLOWED TO USE MAX() FUNCTION
student_scores = input("Input a list of student scores here\n").split()
potential_highest = 0
for individual_score in student_scores:
    individual_score = int(individual_score)
    if individual_score > potential_highest:
        potential_highest = individual_score
print(f"The highest score in the list is {potential_highest}")