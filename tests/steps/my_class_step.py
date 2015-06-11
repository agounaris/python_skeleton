from behave import *
from hamcrest import *

from PROJECT_NAME.my_class import MyClass


@given(u'I instantiate my class')
def step_impl(context):
    context.my_class = MyClass()
    assert_that(context.my_class, instance_of(MyClass))


@when(u'I call my method with argument {num:d}')
def step_impl(context, num):
    context.result = context.my_class.my_function(num)


@then(u'I should get back {num:d}')
def step_impl(context, num):
    assert_that(context.result, equal_to(num))
