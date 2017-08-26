import re
import logging
from string import (ascii_lowercase,
                    ascii_uppercase,
                    punctuation,
                    digits)
from getpass import getpass
from os import path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def check_upper_and_lower_case_in_string(string):
    return any(char in string for char in ascii_uppercase) and\
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


def check_length_more_5_chars(string):
    return len(string) > 5


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
              check_length_more_5_chars,
              check_no_regexp_in_string]
    check_results_dict = {check.__name__: check(password) for check in checks}
    check_results_list = list(check_results_dict.values())
    for key, value in check_results_dict.items():
        printed_check_result = 'passed' if value is True else 'failed'
        logger.info('Test {}: {}'.format(key, printed_check_result.upper()))
    positive_check_count = check_results_list.count(True)
    all_check_count = sum([check_results_list.count(True), check_results_list.count(False)])

    min_password_strength = 1
    calculated_password_strength = int(round(positive_check_count / all_check_count * 9, 0)) + 1
    return min_password_strength if check_10k_most_common_passwords_equal_string(password)\
        else calculated_password_strength


if __name__ == '__main__':
    password = getpass('Enter the password and I will analyze its strength: ')
    print('Strong of your password {} of 10'.format(get_password_strength(password)))
