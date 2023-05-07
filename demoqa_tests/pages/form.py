import os

from selene import browser, have

from demoqa_tests.data.users import User


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))

    def register(self, student: User):
        browser.element('#firstName').type(student.first_name)
        browser.element('#lastName').type(student.last_name)
        browser.element('#userEmail').type(student.email)
        browser.element(f'[value={student.gender}]').double_click()
        browser.element('#userNumber').type(student.mobile)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(student.birthday.year)
        browser.element('.react-datepicker__month-select').type(student.birthday.strftime('%B'))
        browser.element(f'[aria-label="Choose Friday, {student.birthday.strftime("%B")} '
                        f'{student.birthday.strftime("%d").lstrip("0")}th, {student.birthday.year}"]').click()
        for subject in student.subjects:
            browser.element('#subjectsInput').type(subject).press_enter()
        browser.element(f'label[for="hobbies-checkbox-{student.hobby}"]').click()
        browser.element('#uploadPicture').send_keys(os.getcwd() + f"/{student.picture}")
        browser.element('#currentAddress').type(student.address)
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(student.state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(student.city)).click()
        browser.element('#submit').execute_script('element.click()')

    def should_have_registered(self, student: User):
        full_name = f'{student.first_name} {student.last_name}'
        birthday = f'{student.birthday.strftime("%d")} {student.birthday.strftime("%B")},{student.birthday.year}'
        state_and_city = f'{student.state} {student.city}'
        subject = ', '.join([subject for subject in student.subjects])
        browser.all('tbody tr').should(have.exact_texts(
            f'Student Name {full_name}',
            f'Student Email {student.email}',
            f'Gender {student.gender}',
            f'Mobile {student.mobile}',
            f'Date of Birth {birthday}',
            f'Subjects {subject}',
            f'Hobbies {student.hobbies}',
            f'Picture {student.picture}',
            f'Address {student.address}',
            f'State and City {state_and_city}')
        )

    def close_modal(self):
        browser.element('#closeLargeModal').click()
