import csv
from staff import *

class Teacher(Staff):
    def __init__(self, name, id_num, courses, filename="staff.csv"):
        super().__init__(name, id_num, "Teacher", filename)
        self.courses = courses

    def add_to_csv(self):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Teacher", self.name, self.id_num, ",".join(self.courses)])

    def __str__(self):
        course_list = ', '.join(self.courses)
        return f"Teacher Name: {self.name}, ID: {self.id_num}, Courses: {course_list}"