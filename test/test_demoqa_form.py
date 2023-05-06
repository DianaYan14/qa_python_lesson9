from demoqa_tests.pages.demoqa_form import RegistrationPage
from selene import have


def test_send_form(browser_go):
    registration_page = RegistrationPage()
    # открыть форму
    registration_page.open()
    # заполнить форму
    registration_page.fill_first_name('Sherlock')
    registration_page.fill_last_name('Holmes')
    registration_page.fill_email('HolmsTest@gmail.com')
    registration_page.choose('Male')
    registration_page.fill_number('8977777575')
    registration_page.fill_date_of_Birth('January 6th, 1984')
    registration_page.assert_date_of_Birth().should(have.value('06 Jan 1984'))
    registration_page.select_subjects('Maths', 'Eng')
    registration_page.set_checkbox('2')
    registration_page.upload_picture('picture.jpg')
    registration_page.fill_address('221B Baker Street')
    registration_page.select_state_and_city('NCR', 'Delhi')
    # отправить форму
    registration_page.send_form().should(have.text('Thanks for submitting the form'))
    registration_page.user_info().should(
        have.exact_texts('Student Name Sherlock Holmes', 'Student Email HolmsTest@gmail.com', 'Gender Male',
                         'Mobile 8977777575',
                         'Date of Birth 06 January,1984', 'Subjects Maths, English', 'Hobbies Reading',
                         'Picture picture.jpg', 'Address 221B Baker Street',
                         'State and City NCR Delhi'))
    registration_page.close_modal()
