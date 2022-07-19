student_scores = {
    "harry": 81,
    "ron":78,
    "hermione":99,
    "draco":74,
    "neville":62,
}
for student in student_scores:
    score = student_scores[student]
    
    if score > 90:
        student_grade="Outstanding"
    elif score >80:
        student_grade="Exceeds Expectation"
    elif score > 70:
        student_grade="Acceptable"
    else:
        student_grade="Fail"

    print(student_grade)
    