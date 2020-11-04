student_list = [
    'Alice', 
    'Bob', 
    'Charlie', 
    'David', 
    'Eve', 
    'Fred', 
    'Ginny', 
    'Harriet', 
    'Ileana', 
    'Joseph',
    'Kincaid',
    'Larry'
]

class Garden:
    PLANT_CODES = {
        'G' : 'Grass',
        'C' : 'Clover',
        'R' : 'Radishes',
        'V' : 'Violets'
    }

    def __init__(self, diagram, students=student_list):
        self.students_to_plants = self.students_plants(sorted(students), diagram)
    

    def students_plants(self, students, diagram):
        students_plants = {}
        for student in students:
            students_plants[student] = []

        rows = diagram.splitlines()
        for i in range(int(len(rows[0])/2)):
            for row in rows:
                students_plants[students[i]].extend((self.PLANT_CODES[row[2*i]], self.PLANT_CODES[row[2*i+1]]))
        return students_plants
    

    def plants(self, student):
        return self.students_to_plants[student]

