from selene import have
from demoqa_tests.data.users import student
from demoqa_tests.pages.form import RegistrationPage


def test_filling_form(browser_go):
    registration_page = RegistrationPage()
    # открыть форму
    registration_page.open()
    # заполнить форму
    registration_page.register(student)
    # проверка данных
    registration_page.should_have_registered(student)
    registration_page.close_modal()
