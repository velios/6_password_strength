import re
from string import (ascii_lowercase,
                    ascii_uppercase,
                    punctuation,
                    digits)
from getpass import getpass
from os import path


def check_upper_and_lower_case_in_string(string):
    return any(char in string for char in ascii_uppercase) and \
           any(char in string for char in ascii_lowercase)


def check_digits_in_string(string):
    return any(char in string for char in digits)


def check_punctuation_in_string(string):
    return any(char in string for char in punctuation)


def check_10k_most_common_passwords_equal_string(string):
    check_file = '10k_most_common.txt'
    if not path.exists(check_file):
        return None
    with open(check_file, 'r') as bad_passwords_file:
        return any(word.rstrip('\n') == string for word in bad_passwords_file)


def check_string_length(string, min_length=5):
    return len(string) > min_length


def check_no_regexp_in_string(string):
    regexp_checks = {
        'iso_data': re.compile(r'[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])'),
        'email': re.compile(r'^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$'),
        'domain_name': re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9]\.[a-zA-Z]{2,}$')
    }
    return all([re.match(check, string) is None for check in regexp_checks.values()])


def get_password_strength(password):
    checks = [check_upper_and_lower_case_in_string,
              check_digits_in_string,
              check_punctuation_in_string,
              check_string_length,
              check_no_regexp_in_string]
    check_results_list = [check_func(password) for check_func in checks]
    positive_check_count = check_results_list.count(True)
    all_check_count = sum([check_results_list.count(True), check_results_list.count(False)])

    min_password_strength = 1
    max_password_strength = 9
    calculated_password_strength = min_password_strength + int(round(positive_check_count / all_check_count * max_password_strength))
    return min_password_strength if check_10k_most_common_passwords_equal_string(password) \
        else calculated_password_strength


if __name__ == '__main__':
    password = getpass('Enter the password and I will analyze its strength: ')
    print('Strong of your password {} of 10'.format(get_password_strength(password)))
