# Names: John-Francis Caccamo, Jacob Mast, Esther Park
# Date: 11 / 30 / 20
# Description: The task.py file contains three functions make up the
# portfolio project of CS 362.
# Function conv_num takes a string in integer, float, or
# hexadecimal format (including negatives) and converts it to a base-10
# number. my_datetime takes in an integer value representing the number
# of seconds and converting it into a date after the epoch Jan 1, 1970.
# conv_endian takes an integer value and converts it to a hexadecimal number
# as a string.


import constant


# conv_num will handle integer, decimal, hexadecimal inputs
def conv_num(num_str):

    # if not string or empty string passed to function
    if type(num_str) is not str or not num_str:
        return None

    # if num_str is hexadecimal
    if "0x" in num_str or "0X" in num_str:
        return conv_hex(num_str)  # call conv_hex if hexadecimal prefix is found in num_str
    else:
        return conv_int_float(num_str)  # else call conv_int_float for hexadecimal num_str input


# conv_int_float will convert integers and decimals - in order to make conv_num less complex
def conv_int_float(num_str):

    # values dictionary
    values = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    # neg bool will determine if the number is negative
    neg_bool = False

    # splice out the negative from the input
    if num_str[0] == "-":
        neg_bool = True
        num_str = num_str[1:]

    result = 0  # result will hold the number to be returned
    count = 0  # count will hold the iteration increments
    dot_pos = 0  # dot_pos will determine the position of the decimal
    str_len = len(num_str)  # str_len will hold the length of the string
    dot_bool = False  # bool to determine if decimal is encountered

    for dig in num_str:
        if dig not in values.keys() and dig != ".":
            # if the char is not in the dictionary or not a decimal
            return None
        if dig == ".":
            if dot_bool:  # if decimal has already been encountered
                return None
            # determine position from the right of the string
            dot_pos = str_len - count - 1
            dot_bool = True
        else:
            result = 10 * result + values[dig]  # x10 to represent positions
        count += 1  # increment count with each iteration of the loop

    if dot_bool:
        result += 0.0  # convert to a float

        if dot_pos > 0:
            # divide the result dependent on where the decimal was encountered
            result /= exp_power(10, dot_pos)

    if neg_bool:  # if string was negative
        result *= (-1)  # times by negative 1 to convert to a negative number

    return result


def conv_hex(num_str):
    # hex values dictionary
    values = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
              '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'a': 10,
              'B': 11, 'b': 11, 'C': 12, 'c': 12, 'D': 13, 'd': 13,
              'E': 14, 'e': 14, 'F': 15, 'f': 15}

    # neg_bool will determine if the hexadecimal number has a negative prefix
    neg_bool = False

    if num_str[0] == "-":
        neg_bool = True

    result = 0

    if neg_bool:  # loop after the negative and hexadecimal prefix
        if len(num_str) == 3:  # case for solely the negative and prefix
            return None
        for dig in num_str[3:]:
            if dig not in values:  # if the char is not in the dictionary
                return None
            result = 16 * result + values[dig]  # times by 16 to represent the hexadecimal value, a rolling value

    else:  # loop after hexadecimal prefix
        if len(num_str) == 2:  # case for solely the prefix
            return None
        for dig in num_str[2:]:
            if dig not in values:  # if the char is not in the dictionary
                return None
            result = 16 * result + values[dig]  # times by 16 to represent the hexadecimal value, a rolling value

    if neg_bool:
        return -1 * result  # return negative number if negative prefix
    return result


# a power function to establish the decimal position of the return - updating variable names from 1 letter
def exp_power(base, power):
    if power == 1:
        return base
    else:
        return base * (exp_power(base, power - 1))


# FUNCTION 2
def my_datetime(num_sec):
    base_month = 1
    base_day = 1
    years_count = 1970
    months_list = ["01", "02", "03", "04", "05", "06",
                   "07", "08", "09", "10", "11", "12"]
    date_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]

    # divide num_sec by the number of seconds in a day
    days = num_sec // constant.SECS_IN_DAY
    day_count = days
    # while loop determines final year from days while
    # accounting for leap year rule
    while day_count > 365:
        day_count -= 365
        # subtract 366 from day_count for leap years
        if leap_year(years_count):
            day_count -= 1
        years_count += 1

    leap_flag = leap_year(years_count)
    if day_count == 365 and leap_flag == 0:
        # non leap year, jan 1st, 1 year later is date
        years_count += 1
    elif leap_flag == 1:
        # year is a leap year, find month and date
        base_month, base_day = leap_year_date(day_count)
    else:
        # year is not a leap year, find month and date
        base_month, base_day = year_date(day_count)

    # use list to give numbers 1-9 a leading 0
    # in month and date
    final_month = months_list[base_month - 1]
    final_day = str(base_day)
    if base_day < 10:
        final_day = date_list[base_day - 1]

    # arrange string for return from function
    final_date = final_month + "-" + final_day + "-" + str(years_count)
    return final_date


# helper function returns 1 if curr_yr is a
# leap year, 0 if curr_yr is not a leap year
def leap_year(curr_yr):
    leap_flag = 0
    # if year is a multiple of 4
    if (curr_yr % 4) == 0:
        leap_flag = 1
    # if year is a non leap year multiple of 100
    if (curr_yr % 100) == 0 and (curr_yr % 400) != 0:
        leap_flag = 0
    return leap_flag


# helper function returns the month and
# date given the day_year, days in the
# year since 01-01.  Works for non leap
# years
def year_date(day_year):
    # add 1 to give date since day_year is days since 01-01
    day_year += 1
    curr_month = 1
    long_month_list = {1, 3, 5, 7, 8, 10, 12}
    short_month_list = {4, 6, 9, 11}
    # subtract days and increment month counter, depending
    # on number of days in curr_month
    while day_year > 31:
        day_year -= 28
        if curr_month in long_month_list:
            day_year -= 3
        elif curr_month in short_month_list:
            day_year -= 2
        curr_month += 1

    # 31 days left on counter and curr_month has 30 days
    if curr_month in short_month_list and day_year == 31:
        day_year -= 30
        curr_month += 1

    # 29+ days left on counter and curr_month has 28 days
    if curr_month == 2 and day_year > 28:
        day_year -= 28
        curr_month += 1

    return curr_month, day_year


# helper function returns the month and
# date given the day_year, days in the
# year since 01-01.  Works leap years
def leap_year_date(day_year):
    day_year += 1
    curr_month = 1
    long_month_list = {1, 3, 5, 7, 8, 10, 12}
    short_month_list = {4, 6, 9, 11}
    # subtract days and increment month counter, depending
    # on number of days in curr_month
    while day_year > 31:
        day_year -= 29
        if curr_month in long_month_list:
            day_year -= 2
        elif curr_month in short_month_list:
            day_year -= 1
        curr_month += 1

    if curr_month in short_month_list and day_year == 31:
        day_year -= 30
        curr_month += 1

    # 30+ days left on counter and curr_month has 29 days
    if curr_month == 2 and day_year > 29:
        day_year -= 29
        curr_month += 1

    return curr_month, day_year


# FUNCTION 3
def conv_endian(num, endian='big'):
    hex_list = []
    hex_string = ""
    negFlag = 0

    if endian != 'big' and endian != 'little':
        return None

    if num < 0:
        num = num * (-1)
        negFlag = 1

    hex_string = decToHex(num)

    # reverse order for default big endian
    hex_string = hex_string[::-1]
    # add required 0s to pad the hex
    hex_length = len(hex_string) % 2
    if hex_length != 0:
        hex_string = '0' + hex_string

    # insert every 2 char of string as elements of list
    for i in range(0, len(hex_string), 2):
        hex_list.append(hex_string[i:i + 2])

    # if endian is little, reverse list elements
    if endian == 'little':
        hex_list = hex_list[::-1]

    # combine elements of list into a string with space in between
    hex_string = " ".join(hex_list)

    # if negative number, add '-'
    if negFlag == 1:
        hex_string = "-" + hex_string

    return hex_string


# helper function converts decimal to hex
# returns string version
def decToHex(num):
    char_list = []
    charToString = ""

    if num == 0:
        char_list.append(0)

    while num > 0:
        hex_value = num % 16
        num = num // 16

        # conversion helper function
        char = hexConversion(hex_value)

        # append each char to the list
        char_list.append(char)

    # convert hex int into a string
    for x in char_list:
        charToString += str(x)

    return charToString


def hexConversion(hex_value):
    if hex_value < 10:
        char = hex_value
    elif hex_value == 10:
        char = 'A'
    elif hex_value == 11:
        char = 'B'
    elif hex_value == 12:
        char = 'C'
    elif hex_value == 13:
        char = 'D'
    elif hex_value == 14:
        char = 'E'
    elif hex_value == 15:
        char = 'F'

    return char
