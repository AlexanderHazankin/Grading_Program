student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,

}

student_grades = {}

for key in student_scores:
    if 0 <= student_scores[key] <= 70:
        student_grades[key] = "Fail"
    elif 71 <= student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    elif 81 <= student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif 91 <= student_scores[key] <= 100:
        student_grades[key] = "Outstanding"
    if student_scores[key] > 100 or student_scores[key] < 0:
        print(f"\033[1m\033[31mWrong score error! \033[22m\033[39mThe Score of \033[1m\033[31m{key} \033[22m\033[39mis out of range 0-100")

print(student_grades)
