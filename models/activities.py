from models.people import Member, Person
from models.schools import School
from typing import Optional


class Activity:
    """
    Class Activity
    """

    def __init__(self, name: str, price: int, school: School, id_activity=None):
        self.name: str = name
        self.price: int = price
        self.id_activity = id_activity
        self.students: list[Person] = []
        self.teacher: Optional[Person] = None
        self.school: School = school

    def __str__(self) -> str:
        return f'Activity: {self.name}'

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.school == other.school

    def add_student(self, student):
        """
        Add a student to the activity
        :param student:
        """
        if student.is_student() and student not in self.students:
            self.students.append(student)
        else:
            print('The person is not a student or already exists')

    def remove_student(self, student):
        """
        Remove a student from the activity
        :param student:
        """
        if student in self.students:
            self.students.remove(student)
        else:
            print('The person is not in the activity')

    @property
    def total_students(self):
        """
        Return the total of students in the activity
        :return:
        """
        return len(self.students)

    def assign_teacher(self, teacher: Person):
        """
        Add a teacher to the activity
        :param teacher:
        """
        if teacher.is_teacher():
            self.teacher = teacher
        else:
            print('The person is not a teacher')

    def remove_teacher(self):
        """
        Remove a teacher from the activity
        """
        if self.teacher is not None:
            self.teacher = None
