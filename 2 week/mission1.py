name = input("Enter student's name: ")
score = input("Enter student's score: ")

try:
    name = name
    score = int(score)
except:
    print("Error, please enter numeric input")
    quit()

print("student's name:", name)
print("student's score:", score)
if score >= 95:
    grade = "A+"
elif score >= 90:
    grade = "A"
elif score >= 85:
    grade = "B+"
elif score >= 80:
    grade = "B"
elif score >= 75:
    grade = "C+"
elif score >= 70:
    grade = "C"
elif score >= 65:
    grade = "D+"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("student's grade:", grade)