from lewagon.student import Student


class DataStudent(Student):
    # class SubClass(SuperClass):
    # class ChildClass(ParentClass):
    course = "data"

    def __init__(self, name, age, specialty="DL"):
        super().__init__(name, age)
        self.specialty = specialty
