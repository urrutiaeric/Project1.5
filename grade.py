import csv

class Grade:
    def __init__(self, course, grade):
        self.course = course
        self.grade = grade

    def add_grade_to_csv(self, filename):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Grade", self.course.course_name, self.grade])

    def __str__(self):
        return f"Course: {self.course.course_name}, Grade: {self.grade}"
