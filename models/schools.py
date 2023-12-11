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
        self.commission: float = 0.5

    def __str__(self) -> str:
        return f'School: {self.name}'

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.address == other.address

    def full_name(self) -> str:
        """
        Return the full name of the school
        :return:
        """
        return f'{self.name} - {self.address}'

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

    def pay_teacher(self, activity: Activity, amount: float, date: str) -> None:
        """
        Pay the teacher of an activity
        :param activity:
        :param amount:
        :param date:
        """
        if activity.teacher is not None:
            total_teacher = amount * self.commission
            total_owner = amount - total_teacher
            self.make_payment(total_teacher, activity, activity.teacher, date)
            self.pay_owner(activity, total_owner, date)
        else:
            print('The activity does not have a teacher')

    def pay_owner(self,activity: Activity, amount: float, date: str) -> None:
        """
        Pay the owner of the school
        :param activity:
        :param amount:
        :param date:
        """
        self.make_payment(amount, activity, self.owner, date)

    def make_monthly_payment(self) -> None:
        """
        Make a monthly payment to the teachers
        """
        for activity in self.activities:
            total_amount = 0
            for payment in self.payments:
                if payment.activity == activity and payment.date.month == datetime.now().month:
                    total_amount += payment.amount
            if activity.teacher == self.owner:
                self.pay_owner(activity, total_amount, datetime.now().strftime('%Y-%m-%d'))
            else:
                self.pay_teacher(activity, total_amount, datetime.now().strftime('%Y-%m-%d'))
