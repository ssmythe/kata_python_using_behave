from behave import *
from hamcrest import assert_that, equal_to
from lib.fizzbuzz import FizzBuzz


@given('the number "{number}"')
def step_given_the_number(context, number):
    context.number = number


@when("we run do_fizz with the number")
def step_when_we_run_do_fizz_with_the_number(context):
    fb = FizzBuzz()
    context.results = fb.do_fizz(context.number)


@then('we expect back "{text}"')
def step_then_we_get_back(context, text):
    assert_that(context.results, equal_to(text))
