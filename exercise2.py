#تمرین_شماره_دوم 
def average_calculator(grade_list):
    total = sum(grade_list)
    natije = total / len(grade_list)
    return natije
lessons = int(input("Enter the number of lessons: "))
grades = []
for i in range(lessons):
    n = float(input(f"Enter grade of {i+1}: "))
    grades.append(n) 
final_grade = average_calculator(grades)
print(f"Your average score is {final_grade:.2f}")
if final_grade >= 17:
    print("Great!!")
elif final_grade >= 12:
    print("Weak")
else:
    print("Failed")