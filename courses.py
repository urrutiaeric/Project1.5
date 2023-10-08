import csv

class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id

    def add_to_csv(self, filename):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Course", self.course_name, self.course_id])

    def __str__(self):
        return f"Course Name: {self.course_name}, Course ID: {self.course_id}"
