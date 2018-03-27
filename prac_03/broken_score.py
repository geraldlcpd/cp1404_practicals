def score_calc(in_score):
    if in_score < 0:
        result = "Invalid Score"
    elif in_score > 100:
        result = "Invalid Score"
    elif in_score > 90:
        result = "Excellent"
    elif in_score > 50:
        result = "Acceptable"
    else:
        result = "Bad"

    return result


score = float(input("Enter Score: "))
grade = score_calc(score)
print(grade)

