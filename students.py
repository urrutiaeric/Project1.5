import csv

class Student:
    def __init__(self, name, id_num):
        self.name = name
        self.id_num = id_num
        self.courses = []
        self.grades = {}

    def add_course(self, course):
        self.courses.append(course)

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def calculate_gpa(self):
        grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
        total_grade_points = sum(grade_points.get(grade, 0) for grade in self.grades.values())
        if not self.grades:
            return 0.0
        return total_grade_points / len(self.grades)

    def add_to_csv(self, filename):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Student", self.name, self.id_num])

    def __str__(self):
        course_names = [course.course_name for course in self.courses]
        result = f"Name: {self.name}, ID: {self.id_num}, Courses: {', '.join(course_names)}, GPA: {self.calculate_gpa():.2f}"
        return result

