from selene import command
from selene.support.shared import browser

from model.registration_page import RegistrationPage


def test_register_form():
    registration_page= RegistrationPage()
    registration_page.open()

    registration_page.fill_first_name('Анастасия')
    registration_page.fill_last_name('Фло')
    registration_page.fill_email('testmail@mail.gg')
    registration_page.fill_phone_number('9999999999')
    registration_page.gender_select()
    registration_page.fill_date_of_birth(1995, 10, 11)
    registration_page.select_hobby()
    registration_page.fill_subject('P')
    registration_page.add_photo('image/pngwing.com (1).png')
    registration_page.fill_address('221b', 'Baker Street', 'London', 'NW1 6XE', 'UK')
    registration_page.state_select('NCR').city_select('Delhi')
    browser.element('#submit').perform(command.js.scroll_into_view)
    browser.element('#submit').execute_script('element.click()')
    registration_page.should_registrated_user_with(
        'Анастасия Фло',
        'testmail@mail.gg',
        'Other',
        '9999999999',
        '11 November,1995',
        'Physics',
        'Reading',
        'pngwing.com (1).png',
        '221b, Baker Street, London, NW1 6XE, UK',
        'NCR Delhi'
    )