import dataclasses

@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    first_subject: str
    second_subject: str
    current_address: str
    state: str
    city: str
    day_birth: str
    month_birth: str
    year_birth: str
    file_name: str
    hobbies: str


