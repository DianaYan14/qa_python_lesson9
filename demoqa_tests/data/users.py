import dataclasses
from typing import List
from datetime import date


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    birthday: date
    subjects: List[str]
    hobby: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str


student = User(
    first_name='Sherlock',
    last_name='Holmes',
    email='HolmsTest@gmail.com',
    gender='Male',
    mobile='8977777575',
    birthday=date(1984, 1, 6),
    subjects=['Maths', 'English'],
    hobby='2',
    hobbies='Reading',
    picture='picture.jpg',
    address='221B Baker Street',
    state='NCR',
    city='Delhi'
)


