import os
from selene import have, command
from selene.support.shared import browser


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.phone_number = browser.element('#userNumber')
        self.subject_input = browser.element('#subjectsInput')
        self.hobby = browser.element('//*[@id="hobbiesWrapper"]/div[2]/div[2]/label')
        self.photo = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.state = browser.element('#react-select-3-input')
        self.city = browser.element('#react-select-4-input')
        self.gender = browser.element('label[for="gender-radio-2')

    def open(self):
        browser.open('/automation-practice-form')
        # browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
        #     have.size_greater_than_or_equal(3)
        # )
        # browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        # return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        self.email.type(value)
        return self

    def fill_phone_number(self, value):
        self.phone_number.type(value)
        return self

    def gender_select(self):
        self.gender.click()

    def fill_subject(self, value):
        self.subject_input.type(value).press_enter()
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click().element(f'option[value="{year}"]').click()
        browser.element('.react-datepicker__month-select').click().element(f'option[value="{month}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def select_hobby(self):
        self.hobby.with_(timeout=10).click()
        return self

    def add_photo(self, path):
        self.photo.send_keys(os.path.abspath(f'{path}'))
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def state_select(self, value):
        self.state.type(value).press_enter()
        return self

    def city_select(self, value):
        self.city.type(value).press_enter()

    def should_registrated_user_with(self, student):
        browser.all(".table-dark>tbody>tr>td:nth-child(2)").should(have.texts(
        f'{student.first_name} {student.last_name}',
            student.email,
            student.gender,
            student.phone_number,
            f'{student.day_of_birth} {student.month_of_birth},{student.year_of_birth}',
            student.subject,
            student.hobby,
            student.picture,
            student.current_address,
            f'{student.state} {student.city}'
        ))
        return self


