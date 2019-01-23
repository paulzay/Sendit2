import re


def valid_email(self, email):
    """ Validate email format """
    response = False
    if re.match(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)", email) is None:
        return"Invalid email address!"
    return response


def valid_name(sender_name):
    regex = "^[A-Za-z]{4,}$"
    return re.match(regex, sender_name)


def valid_destination(destination):
    regex = "^[a-zA-Z]{1,}$"
    return re.match(regex, destination)


def valid_pickup_location(pickup_location):
    regex = "^[a-zA-Z]{1,}$"
    return re.match(regex, pickup_location)


def valid_input(input):
    regex = "^[a-zA-Z0-9_]{1,20}$"
    return re.match(regex, input)