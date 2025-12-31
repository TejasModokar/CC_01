from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    grades: list[int]

    def average(self):
        return sum(self.grades) / len(self.grades)

s = Student("Alex", 16, [90, 85, 88])
print(s.average())
