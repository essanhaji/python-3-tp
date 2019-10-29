class Student:
    id: int
    first_name: str
    last_name: str
    note: float

    def __init__(self, id, first_name, last_name, note):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.note = note


student_first = Student(1, "El houcine", "Essanhaji", 18.21)
