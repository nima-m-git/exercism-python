from collections import defaultdict

class School:
    def __init__(self):
        self.school_list = defaultdict(lambda: [])

    def add_student(self, name, grade):
        self.school_list[grade].append(name)

    def roster(self):
        return [name for grade in sorted(self.school_list) for name in sorted(self.school_list[grade]) ]

    def grade(self, grade_number):
        return sorted(self.school_list[grade_number])