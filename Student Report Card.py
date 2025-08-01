class Subject:
    def __init__(self, name, max_marks):  
        self.name = name
        self.max_marks = max_marks

    def get_name(self):
        return self.name

    def get_max_marks(self):
        return self.max_marks


class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def get_name(self):
        return self.name

    def get_roll_number(self):
        return self.roll_number

    def get_grade(self):
        return self.grade


class ReportCard:
    def __init__(self, student):
        self.student = student
        self.marks = {} 
        self.subjects = {}  

    def add_mark(self, subject_obj, score):
        if isinstance(subject_obj, Subject):
            subject_name = subject_obj.get_name()
            self.marks[subject_name] = score
            self.subjects[subject_name] = subject_obj
        else:
            print("Invalid subject object provided.")

    def calculate_percentage(self):
        total_obtained_marks = sum(self.marks.values())
        total_max_marks = sum(subject.get_max_marks() for subject in self.subjects.values())
        if total_max_marks > 0:
            return (total_obtained_marks / total_max_marks) * 100
        return 0

    def get_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 90:
            return "A"
        elif percentage >= 80:
            return "B"
        elif percentage >= 70:
            return "C"
        else:
            return "D"

    def display_report_card(self):
        print(f"\n-- Report Card for {self.student.get_name()} --")
        print(f"Roll Number: {self.student.get_roll_number()}")
        print(f"Class: {self.student.get_grade()}")
        print("\nSubject Marks:")
        for subject, score in self.marks.items():
            print(f"{subject}: {score}")
        print(f"\nOverall Percentage: {self.calculate_percentage():.2f}%")
        print(f"Overall Grade: {self.get_grade()}")
        print("---------------------------------")


# Subjects
math = Subject("Mathematics", 100)
physics = Subject("Physics", 100)
chemistry = Subject("Chemistry", 100)

# Student 1
student1 = Student("Mayur Tupe", "001", "12th")
report_card1 = ReportCard(student1)
report_card1.add_mark(math, 85)
report_card1.add_mark(physics, 70)
report_card1.add_mark(chemistry, 95)
report_card1.display_report_card()

# Student 2
student2 = Student("Mohit Dive", "002", "12th")
report_card2 = ReportCard(student2)
report_card2.add_mark(math, 89)
report_card2.add_mark(physics, 77)
report_card2.add_mark(chemistry, 90)
report_card2.display_report_card()
