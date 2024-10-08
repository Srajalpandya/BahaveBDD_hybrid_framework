from behave import *
from selenium.webdriver.common.by import By
from datetime import datetime

from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage
from features.pages.AcountPage import AccountPage


@given(u'I Navigated to login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.home_page.select_login_option()


@when(u'I enter valid email address and password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("zoro@gmail.com")
    context.login_page.enter_password("1234")


@when(u'I click on login button')
def step_impl(context):
    context.login_page.click_on_login_button()

@then(u'I should get logged in')
def step_impl(context):
    context.account_page = AccountPage(context.driver)
    assert context.account_page.display_status_of_edit_your_account_information_option()



@when(u'I enter invalid mail and valid password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("zoro1@gmail.com")
    context.login_page.enter_password("1234")


@then(u'I should get a proper warning message')
def step_impl(context):
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    assert context.driver.find_element(By.XPATH,"//div[@id='account-login']/div[1]").text.__contains__(expected_warning_message)


@when(u'I enter valid email and invalid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID,"input-email").send_keys("zoro@gmail.com")
    context.driver.find_element(By.ID,"input-password").send_keys("12345")


@when(u'I enter invalid email password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID,"input-email").send_keys("zoro1@gmail.com")
    context.driver.find_element(By.ID,"input-password").send_keys("12345")

@when(u'I dont enter anything into email and password fields')
def step_impl(context):
    context.driver.find_element(By.ID,"input-email").send_keys("")
    context.driver.find_element(By.ID,"input-password").send_keys("")
