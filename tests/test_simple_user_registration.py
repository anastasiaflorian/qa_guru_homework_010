from data.users import User
from model.registration_page import RegistrationPage

def test_registers_user():
    registration_page = RegistrationPage

    student = User(
            first_name='Анастасия',
            last_name='Фло',
            email='testmail@mail.gg',
            gender='Female',
            phone_number='9999999999',
            month_of_birth='November',
            year_of_birth='1995',
            day_of_birth='11',
            subject='Computer Science',
            hobby='Reading',
            picture='pngwing.com (1).png',
            current_address='1337 Nice Avenue 13B',
            state='Uttar Pradesh',
            city='Agra'
        )

        registration_page.open()
        registration_page.__init__(student)
        registration_page.should_registrated_user_with(student)