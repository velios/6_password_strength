# Password Strength Calculator

Script calculates the reliability of the password on a ten-point scale. Checklist contains:
* the use of both upper-case and lower-case letters (case sensitivity)
* inclusion of one or more numerical digits
* inclusion of special characters, such as @, #, $
* prohibition of words found in a password blacklist (10k words included in the repository)
* check with regexp password not domain name, email or date

### How to use
```bash
#Run
$ python3 password_strength.py
Enter the password and I will analyze its strength:
```
```bash
#Output
INFO:root:Test check_upper_and_lower_case_in_string: PASSED
INFO:root:Test check_digits_in_string: PASSED
INFO:root:Test check_punctuation_in_string: PASSED
INFO:root:Test check_length_more_5_chars: PASSED
INFO:root:Test check_no_regexp_in_string: PASSED
Strong of your password 10 of 10
```

# Project Goals

This README made with [Dilinger](http://dillinger.io/)
The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
