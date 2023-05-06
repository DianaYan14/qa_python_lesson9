import os

from selene import browser, be, have


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)

    def fill_email(self, value):
        browser.element("#userEmail").type(value)

    def choose(self, param):
        browser.element(f'[value={param}]').double_click()

    def fill_number(self, param):
        browser.element("#userNumber").type(param)

    def fill_date_of_Birth(self, date):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker-popper').should(be.visible)
        browser.element('.react-datepicker__year-select').click()
        browser.element('[value="1984"]').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('[value="0"]').click()
        browser.element('.react-datepicker__day--006').should(
            have.attribute('aria-label', f'Choose Friday, {date}')).click()

    def assert_date_of_Birth(self):
        return browser.element('#dateOfBirthInput')

    def select_subjects(self, param, param1):
        browser.element("#subjectsInput").type(param).press_enter()
        browser.element("#subjectsInput").type(param1).press_enter()

    def set_checkbox(self, number):
        browser.element(f'label[for="hobbies-checkbox-{number}"]').click()

    def upload_picture(self, path):
        browser.element('#uploadPicture').send_keys(os.getcwd() + f'/{path}')

    def fill_address(self, value):
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        browser.element('#currentAddress').type(value)

    def select_state_and_city(self, state, city):
        browser.element('#state').click()
        browser.element('#react-select-3-input').set_value(state).press_tab()
        browser.element('#react-select-4-input').type(city).press_enter()

    def send_form(self):
        browser.element("footer").execute_script('element.remove()')
        browser.element('#submit').execute_script('element.click()')
        return browser.element('.modal-title')

    def user_info(self):
        return browser.all('tbody tr')
    def close_modal(self):
        browser.element('#closeLargeModal').click()

