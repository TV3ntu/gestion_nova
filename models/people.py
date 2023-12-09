"""
People module
"""
from __future__ import annotations
from datetime import datetime

from models.payments import Payment
from models.activities import Activity
from profiles import ProfileEnum
from abc import ABC, abstractmethod

from typing import Union, Type


class Member:
    """
    Class Member
    """

    def __init__(self, name: str):
        self.name: str = name
        self.payments: list[Payment] = []
        self.profiles: set[ProfileEnum] = set()

    def __str__(self):
        return f'Member: {self.name}'

    def __eq__(self, other):
        return self.name == other.name

    def full_name(self) -> str:
        """
        Return the full name of the person
        :return:
        """
        return f'{self.name} {self.surname}'

    def add_profile(self, profile: str) -> None:
        """
        Add a profile to the person
        :param profile:
        """
        if ProfileEnum.id_a_valid_profile(profile):
            self.profiles.add(ProfileEnum(profile))
        else:
            print(f'{profile} is not a valid profile. Available profiles: {", ".join(e.value for e in ProfileEnum)}')

    def remove_profile(self, profile: str) -> None:
        """
        Remove a profile from the person
        :param profile:
        """
        if ProfileEnum.id_a_valid_profile(profile):
            self.profiles.remove(ProfileEnum(profile))
        else:
            print(f'{profile} is not a valid profile. Available profiles: {", ".join(e.value for e in ProfileEnum)}')

    def receive_payment(self, payment: Payment) -> None:
        """
        Receive a payment
        :param payment:
        :return:
        """
        self.payments.append(payment)

    def make_payment(self, activity: Activity, receiver: Member, date: str) -> None:
        """
        Make a payment for an activity
        :param receiver:
        :param activity:
        :param date:
        :return:
        """
        payment = Payment(amount=activity.price,
                          payer=self,
                          receiver=receiver,
                          activity=activity,
                          date=date)
        receiver.receive_payment(payment)


class Person(Member):
    """
    Class Person
    """

    def __init__(self, name: str, surname: str, birth_date: str):
        super().__init__(name)
        self.surname: str = surname
        self.birth_date: datetime = datetime.strptime(birth_date, '%Y-%m-%d')
        self.profile: set[str] = set()

    def __str__(self):
        return f'Person: {self.name} {self.surname}'

    def __eq__(self, other):
        return self.name == other.name and self.surname == other.surname and self.birth_date == other.birth_date

    def age(self) -> int:
        """
        Return the age of the student
        :return:
        """
        today = datetime.today()
        return today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    def is_owner(self):
        """
        Return True if the person is an owner
        :return:
        """
        return ProfileEnum.OWNER in self.profiles

    def is_teacher(self):
        """
        Return True if the person is a teacher
        :return:
        """
        return ProfileEnum.TEACHER in self.profiles

    def is_student(self):
        """
        Return True if the person is a student
        :return:
        """
        return ProfileEnum.STUDENT in self.profiles
