#تمرین_شماره_سوم 
students_list = [
    {
        "student_id": 1,
        "name": "nana",
        "grades": [18, 19, 20]        
    },
    {
        "student_id": 2,
        "name": "nazi",
        "grades": [15, 17, 13.5]
    },
    {
        "student_id": 3,
        "name": "yasi",
        "grades": [20, 16, 18]       
    }         
]

def calculate_student_avg(student_data):
    grades_list = student_data["grades"]
    average = sum(grades_list) / len(grades_list)
    return average 

for student in students_list:
    avg = calculate_student_avg(student) 
    print(f"Name: {student['name']} | Avg: {avg:.2f}")
