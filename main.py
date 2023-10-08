import csv
from students import *
from courses import *
from grade import *
from teacher import *
from staff import *



def main():
    # Create and add courses
    course1 = Course("Math", "MATH101")
    course2 = Course("Science", "SCI101")
    course3 = Course("History", "HIST101")

    course1.add_to_csv("Courses_data.csv")
    course2.add_to_csv("Courses_data.csv")
    course3.add_to_csv("Courses_data.csv")

    # Create staff members (teachers)
    teacher1 = Teacher("ali 1", "T101", ["Math", "Science"])
    teacher2 = Teacher("ali 2", "T102", ["History"])

    teacher1.add_to_csv()
    teacher2.add_to_csv()

    # Create students
    student1 = Student("ali 1", "S101")
    student2 = Student("ali 2", "S102")

    # Add courses and grades for students
    student1.add_course(course1)
    student1.add_course(course2)
    student1.add_grade(course1, "A")
    student1.add_grade(course2, "B")

    student2.add_course(course3)
    student2.add_grade(course3, "A")

    student1.add_to_csv("Students_data.csv")
    student2.add_to_csv("Students_data.csv")

if __name__ == "__main__":
    main()
