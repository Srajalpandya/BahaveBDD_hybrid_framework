from behave import *


@given(u'I got navigated to Home page')
def step_impl(context):
    print('STEP: Given I got navigated to Home page')


@when(u'I enter valid product into the Search box field')
def step_impl(context):
    print('STEP: When I enter valid product into the Search box field')


@when(u'I click on Search button')
def step_impl(context):
    print('STEP: When I click on Search button')


@then(u'Valid product should get displayed in Search results')
def step_impl(context):
    print('STEP: Then Valid product should get displayed in Search results')


@when(u'I enter invalid product into the Search box field')
def step_impl(context):
    print('STEP: When I enter invalid product into the Search box field')


@then(u'Proper message should be displayed in Search results')
def step_impl(context):
    print('STEP: Then Proper message should be displayed in Search results')


@when(u'I don\'t enter anything into the search box field')
def step_impl(context):
    print('STEP: When I don\'t enter anything into the search box field')


