from models.people import Member
from models.activities import Activity
from models.schools import Owner
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
            payer: Union[Member,Owner],
            receiver: Union[Member, Owner],
            activity: Activity,
            date: str
    ) -> None:
        self.amount: float = amount
        self.payer: Member = payer
        self.activity: Activity = activity
        self.receiver: Union[Member, Owner] = receiver
        self.date: datetime = datetime.strptime(date, '%Y-%m-%d')
