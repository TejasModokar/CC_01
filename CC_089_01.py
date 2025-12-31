from dataclasses import dataclass, field

@dataclass
class Student:
    name: str
    age: int
    grades: list[int] = field(default_factory=list)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def show_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.average():.2f}")

if __name__ == "__main__":
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grades_input = input("Enter grades separated by space: ").strip().split()

    grades = [int(g) for g in grades_input if g.isdigit()]

    student = Student(name, age, grades)
    student.show_info()
