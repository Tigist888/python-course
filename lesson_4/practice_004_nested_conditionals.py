# Write a Python program to provide feedback based on a student's test score.
# Follow these steps:

# Get the user input as an integer of the student's score.
student_score=int(input("Enter your score: "))
if student_score>0:
    if student_score>90:
       print("Excellent!")
    elif 70< student_score<90:
       print("inclusive")
    elif student_score<70:
       print("keep working hard!")
else:
       print("No test score available")

# Use a primary if statement to check if the score is higher than 0.
# Inside this if statement, use nested conditionals to determine the feedback message based on these conditions:
# - If the score is greater than 90, print 'Excellent!'.
# - If the score is between 70 and 90 (inclusive), print 'Good job!'.
# - If the score is less than 70, print 'Keep working hard!'.
# If no score is provided (score equals 0), print 'No test score available'.
