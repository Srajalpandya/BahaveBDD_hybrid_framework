from behave import *

@given(u'I Navigated to login page')
def step_impl(context):
    print('STEP: Given I Navigated to login page')


@when(u'I enter valid email address and password into the fields')
def step_impl(context):
    print('STEP: When I enter valid email address and password into the fields')


@when(u'I click on login button')
def step_impl(context):
    print('STEP: When I click on login button')


@then(u'I should get logged in')
def step_impl(context):
    print('STEP: Then I should get logged in')





@when(u'I enter invalid mail and valid password into the fields')
def step_impl(context):
    print('STEP: When I enter invalid mail and valid password into the fields')


@then(u'I should get a proper warning message')
def step_impl(context):
    print('STEP: Then I should get a proper warning message')


@when(u'I enter valid email and invali password into the fieds')
def step_impl(context):
    print('STEP: When I enter valid email and invali password into the fieds')


@when(u'I enter invalid email password into the fields')
def step_impl(context):
    print('STEP: When I enter invalid email password into the fields')


@when(u'I dont enter anything into email and password fields')
def step_impl(context):
    print('STEP: When I dont enter anything into email and password fields')