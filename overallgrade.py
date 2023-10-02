def calculate_grade(marks):
    if marks >= 90: return 'A+'
    elif 80 <= marks < 90: return 'A'
    elif 70 <= marks < 80: return 'B'
    elif 60 <= marks < 70: return 'C'
    elif 50 <= marks < 60: return 'D'
    else: return 'F'

subject_marks = []

for i in range(6):
    marks = float(input(f"Enter marks for subject {i+1}: "))
    if 0 <= marks <= 100:
        subject_marks.append(marks)
    else:
        print("Invalid input. Marks should be between 0 and 100.")
        exit()

average_marks = sum(subject_marks) / len(subject_marks)
overall_grade = calculate_grade(average_marks)
print(f"Overall Grade: {overall_grade}")
