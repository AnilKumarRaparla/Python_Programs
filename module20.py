def find_max_average_score(file_data):
    student_scores = {}

    for i in range(0, len(file_data), 4):
        name = file_data[i]
        scores = list(map(int, file_data[i + 1:i + 4]))
        average_score = round(sum(scores) / len(scores))
        student_scores[name] = average_score

    max_student = max(student_scores, key=student_scores.get)
    max_average_score = student_scores[max_student]

    return f"{max_student} {max_average_score}"

file_data = ["Shrikanth", "20", "30", "10", "Ram", "100", "50", "10"]
result = find_max_average_score(file_data)
print(result)
