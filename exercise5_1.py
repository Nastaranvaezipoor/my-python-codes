#تمرین_شماره_پنجم_بازطراحی_کلاس_Student
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self._grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 20:
            self._grades.append(grade)
            return True
        else:
            print("Error: Grade must be between 0 and 20.")
            return False

    def get_grades(self):
        return self._grades

    def calculate_avg(self):
        grades = self.get_grades()
        if not grades:
            return 0
        return sum(grades) / len(grades)

    def __str__(self):
        avg = self.calculate_avg()
        if avg >= 17:
            status = "Excellent"
        elif avg >= 12:
            status = "Good"
        else:
            status = "Weak"
        return f"Student: {self.name}, ID: {self.student_id}, average: {avg:.2f}, Status: {status}"

name = input("Enter student name: ")
s_id = input("Enter student ID: ")
student1 = Student(name, s_id)

count = int(input("How many courses? "))

for i in range(count):
    while True:
        grade_input = input(f"Enter grade {i+1}: ")
        grade = float(grade_input)
        if student1.add_grade(grade):
            break

print("\n------------------")
print(student1)
