from models.people import Member
from models.activities import Activity
from datetime import datetime
from typing import Union
from dataclasses import dataclass


@dataclass
class Payment:
    """
    Class Payment
    """
    def __init__(
            self,
            amount: float,
            payer: Member,
            receiver: Member,
            activity: Activity,
            date: str
    ) -> None:
        self.amount: float = amount
        self.payer: Member = payer
        self.activity: Activity = activity
        self.receiver: Member = receiver
        self.date: datetime = datetime.strptime(date, '%Y-%m-%d')

    def __eq__(self, other):
        return (self.amount == other.amount
                and self.payer == other.payer
                and self.receiver == other.receiver
                and self.activity == other.activity
                and self.date == other.date)
