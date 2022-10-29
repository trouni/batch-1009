from datetime import date


class Student:  # UpperCamelCase
    school = "Le Wagon"
    # DATA
    # name, age, sex, student_id, nationality, address, etc.
    def __init__(self, name, age):  # constructor
        self.name = name.capitalize()
        self.age = age

    # BEHAVIOR
    # instance method
    def says(self, message):
        print(f"{self.name} says {message}")

    # class method
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = date.today().year - birth_year
        return cls(name, age)
