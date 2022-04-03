import re


def addition(a, b) -> object:
    return a + b


def subtraction(a, b):
    return b - a


def mutiplication(a, b):
    return a * b


def division(a, b):
    return a // b


def to_lower_case(user_input):
    return user_input.lower()


def to_upper_case(user_input):
    return user_input.upper()


def to_sentence_case(user_input):
    return user_input.title()


def to_camel_case(user_input):
    user_input = (re.sub(r"(_|-)+", "", user_input))
    user_input = to_sentence_case(user_input).replace(" ", "")
    return user_input.swapcase()

