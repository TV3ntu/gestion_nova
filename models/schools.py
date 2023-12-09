from models.activities import Activity
from models.people import Member, Person
from datetime import datetime
from typing import Optional


class School(Member):
    def __init__(self, name: str, address: str):
        super().__init__(name)
        self.address: str = address
        self.activities: list[Activity] = []
        self.owner: Optional[Person] = None

    def __str__(self) -> str:
        return f'School: {self.name}'

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.address == other.address

    def update_owner(self, owner: Person) -> None:
        """
        Add an owner to the school
        :param owner:
        """
        if owner.is_owner():
            self.owner = owner
        else:
            print('The person is not an owner')

    def add_activity(self, activity: Activity) -> None:
        """
        Add an activity to the school
        :param activity:
        """
        if activity not in self.activities:
            self.activities.append(activity)
        else:
            print('Activity already exists')

    def remove_activity(self, activity: Activity) -> None:
        """
        Remove an activity from the school
        :param activity:
        """
        if activity in self.activities:
            self.activities.remove(activity)
        else:
            print('Activity does not exists')

    @property
    def total_activities(self) -> int:
        """
        Return the total of activities in the school
        :return total:
        """
        return len(self.activities)

    @property
    def total_students(self) -> int:
        """
        Return the total of students in the activity
        :return total:
        """
        total = 0
        for activity in self.activities:
            total += activity.total_students
        return total

    def list_students(self) -> list[Person]:
        """
        List all the students in the school
        :return students:
        """
        for activity in self.activities:
            students = []
            for student in activity.students:
                students.append(student)
            return students
