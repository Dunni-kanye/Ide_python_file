number_of_students = int(input("Enter the number of students: "))
number_of_subjects = int(input("Enter the number of subjects: "))

students_scores = []
for students in range(number_of_students):
    print(f"\nEntering scores for student {students + 1}")
    student_scores = []
    for subject in range(number_of_subjects):
        while True:
            score = float(input(f"Enter score for subject{subject + 1}: "))
            if 0 <= score <= 100:
                student_scores.append(score)
                break
            else:
                print("Invalid score,score must be between 0 and 100")
        students_scores.append(student_scores)
    print("\nClass Summary:")
    for student in range(number_of_students):
        print(f"{students_scores[student]}")

