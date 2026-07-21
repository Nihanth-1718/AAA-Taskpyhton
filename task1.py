# 1. Student Grade Checker

score = int(input("Enter marks: "))

if score >= 0 and score <= 100:
    if score >= 90:
        print("Grade: A")
        print("Remark: Outstanding!")
    elif score >= 80:
        print("Grade: B")
        print("Remark: Excellent!")
    elif score >= 70:
        print("Grade: C")
        print("Remark: Good")
    elif score >= 60:
        print("Grade: D")
        print("Remark: Fair, Needs Improvement")
    elif score >= 50:
        print("Grade: E")
        print("Remark: Poor, Needs Serious Improvement")
    else:
        print("Grade: F")
        print("Remark: Failed, Needs to Reappear")
else:
    print("Invalid marks entered")
