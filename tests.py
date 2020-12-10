# Names: John-Francis Caccamo, Jacob Mast, Esther Park
# Date: 11 / 30 / 20
# Description: The tests.py file contains the testing suite
# for conv_num, my_datetime and conv_endian functions for
# the portfolio project of CS 362.

import unittest
from datetime import datetime
from task import conv_num, conv_endian, my_datetime


class TestCase(unittest.TestCase):

    # Function 1 - conv_num - testing suite, testing int, float and hexadecimal str input
    def test_integer_input_1_conv_num(self):
        test_str = "12345"
        message = "Incorrect conversion of ({}) string to integer".format(test_str)
        self.assertEqual(conv_num(test_str), 12345, msg=message)

    def test_neg_float_input_1_conv_num(self):
        test_str = "-123.45"
        message = "Incorrect conversion of ({}) string to float".format(test_str)
        self.assertEqual(conv_num(test_str), -123.45, msg=message)

    def test_zero_int_input_conv_num(self):
        test_str = '0'
        message = "Incorrect conversion of ({}) string to int".format(test_str)
        self.assertEqual(conv_num(test_str), 0, msg=message)

    def test_zero_float_input_conv_num(self):
        test_str = "0.0"
        message = "Incorrect conversion of ({}) string to float".format(test_str)
        self.assertEqual(conv_num(test_str), 0.0, msg=message)

    def test_zero_float_input_1_conv_num(self):
        test_str = "0.45"
        message = "Incorrect conversion of ({}) string to float".format(test_str)
        self.assertEqual(conv_num(test_str), 0.45, msg=message)

    def test_zero_float_input_2_conv_num(self):
        test_str = ".45"
        message = "Incorrect conversion of ({}) string to float".format(test_str)
        self.assertEqual(conv_num(test_str), 0.45, msg=message)

    def test_neg_zero_float_input_1_conv_num(self):
        test_str = "-0.45"
        message = "Incorrect conversion of ({}) string to negative float".format(test_str)
        self.assertEqual(conv_num(test_str), -0.45, msg=message)

    def test_neg_zero_float_input_2_conv_num(self):
        test_str = "-.45"
        message = "Incorrect conversion of ({}) string to negative float".format(test_str)
        self.assertEqual(conv_num(test_str), -0.45, msg=message)

    def test_long_float_input_conv_num(self):
        test_str = "123.32543215"
        message = "Incorrect conversion of ({}) string to long float".format(test_str)
        self.assertEqual(conv_num(test_str), 123.32543215, msg=message)

    def test_neg_long_float_input_conv_num(self):
        test_str = "-123.32543215"
        message = "Incorrect conversion of ({}) string to long float".format(test_str)
        self.assertEqual(conv_num(test_str), -123.32543215, msg=message)

    def test_ending_decimal_float_conv_num(self):
        test_str = "123."
        message = "Incorrect conversion of ({}) string to float".format(test_str)
        self.assertEqual(conv_num(test_str), 123.0, msg=message)

    def test_invalid_decimal_conv_num(self):
        test_str = "12.3.45"
        message = "Incorrect flagging of ({}) invalid float and not returning None".format(test_str)
        self.assertEqual(conv_num(test_str), None, msg=message)

    def test_invalid_decimal_consec_points_conv_num(self):
        test_str = "12..45"
        message = "Incorrect flagging of ({}) invalid decimal and not returning None".format(test_str)
        self.assertEqual(conv_num(test_str), None, msg=message)

    def test_invalid_int_conv_num(self):
        test_str = 123
        message = "Incorrect flagging of ({}) invalid decimal and not returning None".format(test_str)
        self.assertEqual(conv_num(test_str), None, msg=message)

    def test_invalid_float_conv_num(self):
        test_str = 123.45
        message = "Incorrect flagging of ({}) invalid float and not returning None".format(test_str)
        self.assertEqual(conv_num(test_str), None, msg=message)

    def test_valid_hexa_conv_num(self):
        test_str = "0xAD4"
        message = "Incorrect conversion of ({}) hexadecimal string to integer".format(test_str)
        self.assertEqual(conv_num(test_str), 2772, msg=message)

    def test_valid_hexa_conv_num_2(self):
        test_str = "0XFA"
        message = "Incorrect flagging of ({}) - Should be 250".format(test_str)
        self.assertEqual(conv_num(test_str), 250, msg=message)

    def test_valid_hexa_lower_case_conv_num(self):
        test_str = "0xaabbccddeeff"
        message = "Incorrect flagging of ({}) - Should be 187723572702975".format(test_str)
        self.assertEqual(conv_num(test_str), 187723572702975, msg=message)

    def test_valid_neg_hexa_lower_case_conv_num(self):
        test_str = "-0xaabbccddeeff"
        message = "Incorrect flagging of ({}) - Should be 187723572702975".format(test_str)
        self.assertEqual(conv_num(test_str), -187723572702975, msg=message)

    def test_valid_hexa_mixed_case_conv_num(self):
        test_str = "0xaABbcCdDEeFf"
        message = "Incorrect conversion of ({}) - Should be 187723572702975".format(test_str)
        self.assertEqual(conv_num(test_str), 187723572702975, msg=message)

    def test_valid_neg_hexa_mixed_case_conv_num(self):
        test_str = "-0XaABbcCdDEeFf"
        message = "Incorrect conversion of ({}) - Should be 187723572702975".format(test_str)
        self.assertEqual(conv_num(test_str), -187723572702975, msg=message)

    def test_valid_neg_hexadecimal_conv_num(self):
        test_str = "-0xFF"
        message = "Incorrect conversion of ({}) to integer -255".format(test_str)
        self.assertEqual(conv_num(test_str), -255, msg=message)

    def test_invalid_hexa_conv_num(self):
        test_str = "0xAZ4"
        message = "Incorrect flagging of ({}) hexadecimal and not returning None".format(test_str)
        self.assertEqual(conv_num(test_str), None, msg=message)

    def test_invalid_hexa_prefix_conv_num(self):
        test_str = "12345A"
        message = "Incorrect flagging of ({}) hexadecimal with incorrect pref and not returning None".format(test_str)
        self.assertEqual(conv_num(test_str), None, msg=message)

    def test_invalid_hexa_pref_pos_conv_num(self):
        test_str = "1230xFB"
        message = "Incorrect flagging of ({}) - Should be None".format(test_str)
        self.assertEqual(conv_num(test_str), None, msg=message)

    def test_invalid_hexa_pref_pos_2_conv_num(self):
        test_str = "FA0X"
        message = "Incorrect flagging of ({}) - Should be None".format(test_str)
        self.assertEqual(conv_num(test_str), None, msg=message)

    def test_invalid_hexa_int_conv_num(self):
        test_str = 0xABC
        message = "Incorrect flagging of ({}) - Should be None".format(test_str)
        self.assertEqual(conv_num(test_str), None, msg=message)

    def test_invalid_hexa_pref_only_conv_num(self):
        test_str = "0X"
        message = "Incorrect flagging of ({}) - Should be None".format(test_str)
        self.assertEqual(conv_num(test_str), None, msg=message)

    def test_invalid_hexa_neg_pref_only_conv_num(self):
        test_str = "-0x"
        message = "Incorrect flagging of ({}) - Should be None".format(test_str)
        self.assertEqual(conv_num(test_str), None, msg=message)

    def test_empty_str_conv_num(self):
        test_str = "     "
        message = "Incorrect flagging of ({}) - Should be None".format(test_str)
        self.assertEqual(conv_num(test_str), None, msg=message)

    def test_empty_str_2_conv_num(self):
        test_str = ""
        message = "Incorrect flagging of ({}) - Should be None".format(test_str)
        self.assertEqual(conv_num(test_str), None, msg=message)

    def test_empty_str_3_conv_num(self):
        test_str = " "
        message = "Incorrect flagging of ({}) - Should be None".format(test_str)
        self.assertEqual(conv_num(test_str), None, msg=message)

    # send tests test test
    # FUNCTION 3 TEST CASES
    def test1(self):
        num = 954786
        endian = 'big'
        expected = '0E 91 A2'
        self.assertEqual(conv_endian(num, endian), expected)

    def test2(self):
        num = 954786
        expected = '0E 91 A2'
        self.assertEqual(conv_endian(num), expected)

    def test3(self):
        num = -954786
        expected = '-0E 91 A2'
        self.assertEqual(conv_endian(num), expected)

    def test4(self):
        num = 954786
        expected = 'A2 91 0E'
        endian = 'little'
        self.assertEqual(conv_endian(num, endian), expected)

    def test5(self):
        num = -954786
        expected = '-A2 91 0E'
        endian = 'little'
        self.assertEqual(conv_endian(num, endian), expected)

    def test6(self):
        num = num = -954786
        expected = '-A2 91 0E'
        endian = 'little'
        self.assertEqual(conv_endian(num, endian), expected)

    # random numbers
    def test7(self):
        num = 2609
        expected = '0A 31'
        endian = 'big'
        self.assertEqual(conv_endian(num, endian), expected)

    def test8(self):
        num = 2609
        expected = '31 0A'
        endian = 'little'
        self.assertEqual(conv_endian(num, endian), expected)

    def test9(self):
        num = -2609
        expected = '-31 0A'
        endian = 'little'
        self.assertEqual(conv_endian(num, endian), expected)

    def test10(self):
        num = -2609
        expected = '-0A 31'
        endian = 'big'
        self.assertEqual(conv_endian(num, endian), expected)

    def test11(self):
        num = 1
        expected = '01'
        endian = 'big'
        self.assertEqual(conv_endian(num, endian), expected)

    def test12(self):
        num = -1
        expected = '-01'
        endian = 'big'
        self.assertEqual(conv_endian(num, endian), expected)

    def test13(self):
        num = 1
        expected = '01'
        endian = 'little'
        self.assertEqual(conv_endian(num, endian), expected)

    def test14(self):
        num = -1
        expected = '-01'
        endian = 'little'
        self.assertEqual(conv_endian(num, endian), expected)

    def test15(self):
        num = -999999
        expected = '-0F 42 3F'
        endian = 'big'
        self.assertEqual(conv_endian(num, endian), expected)

    def test16(self):
        num = 999999
        expected = '0F 42 3F'
        endian = 'big'
        self.assertEqual(conv_endian(num, endian), expected)

    def test17(self):
        num = -999999
        expected = '-3F 42 0F'
        endian = 'little'
        self.assertEqual(conv_endian(num, endian), expected)

    def test18(self):
        num = 999999
        expected = '3F 42 0F'
        endian = 'little'
        self.assertEqual(conv_endian(num, endian), expected)

    def test19(self):
        num = 0
        expected = '00'
        endian = 'little'
        self.assertEqual(conv_endian(num, endian), expected)

    def test20(self):
        num = 0
        expected = '00'
        endian = 'big'
        self.assertEqual(conv_endian(num, endian), expected)

    def test21(self):
        num = -0
        expected = '00'
        endian = 'big'
        self.assertEqual(conv_endian(num, endian), expected)

    def test22(self):
        num = 9223372036854775807
        expected = '7F FF FF FF FF FF FF FF'
        endian = 'big'
        self.assertEqual(conv_endian(num, endian), expected)

    def test23(self):
        num = 9999999999999999999
        expected = '8A C7 23 04 89 E7 FF FF'
        endian = 'big'
        self.assertEqual(conv_endian(num, endian), expected)

    def test24(self):
        num = -9999999999999999999
        expected = '-8A C7 23 04 89 E7 FF FF'
        endian = 'big'
        self.assertEqual(conv_endian(num, endian), expected)

    def test25(self):
        num = -9999999999999999999
        expected = '-8A C7 23 04 89 E7 FF FF'
        endian = 'big'
        self.assertEqual(conv_endian(num, endian), expected)

    def test26(self):
        num = -99999998
        expected = '-05 F5 E0 FE'
        endian = 'big'
        self.assertEqual(conv_endian(num, endian), expected)

    def test27(self):
        num = 1523
        expected = None
        endian = 'Big'
        self.assertEqual(conv_endian(num, endian), expected)

    def test28(self):
        num = 1523
        expected = None
        endian = 'lil'
        self.assertEqual(conv_endian(num, endian), expected)

    def test29(self):
        num = None
        expected = None
        endian = None
        self.assertEqual(conv_endian(num, endian), expected)

    def test30(self):
        num = 1234
        expected = None
        endian = 'other'
        self.assertEqual(conv_endian(num, endian), expected)

    # Function 2 Tests
    def test31(self):
        val = 0
        expected = datetime.strftime(datetime.utcfromtimestamp(val), "%m-%d-%Y")
        self.assertEqual(my_datetime(val), expected)

    def test32(self):
        val = 123456789
        expected = datetime.strftime(datetime.utcfromtimestamp(val), "%m-%d-%Y")
        self.assertEqual(my_datetime(val), expected)

    def test33(self):
        val = 9876543210
        expected = datetime.strftime(datetime.utcfromtimestamp(val), "%m-%d-%Y")
        self.assertEqual(my_datetime(val), expected)

    def test34(self):
        val = 13727318400
        # 01-01-2405, first day first second in year after a leap year
        expected = datetime.strftime(datetime.utcfromtimestamp(val), "%m-%d-%Y")
        self.assertEqual(my_datetime(val), expected)

    def test35(self):
        val = 165547756800
        # 01-01-7216, first day first second in a leap year
        expected = datetime.strftime(datetime.utcfromtimestamp(val), "%m-%d-%Y")
        self.assertEqual(my_datetime(val), expected)

    def test36(self):
        val = 108903052799
        # 12-31-5420, last day last second in a leap year
        expected = datetime.strftime(datetime.utcfromtimestamp(val), "%m-%d-%Y")
        self.assertEqual(my_datetime(val), expected)

    def test37(self):
        val = 43548623999
        # 12-31-3349, last day last second in a non leap year
        expected = datetime.strftime(datetime.utcfromtimestamp(val), "%m-%d-%Y")
        self.assertEqual(my_datetime(val), expected)

    def test38(self):
        val = 86399
        # 01-01-1970, 1 second less than a day
        expected = datetime.strftime(datetime.utcfromtimestamp(val), "%m-%d-%Y")
        self.assertEqual(my_datetime(val), expected)

    def test39(self):
        val = 86400
        # 01-02-1970, exactly one day
        expected = datetime.strftime(datetime.utcfromtimestamp(val), "%m-%d-%Y")
        self.assertEqual(my_datetime(val), expected)

    def test40(self):
        val = 253370764800
        # 01-01-9999, first day first second of last year tested in assignment
        expected = datetime.strftime(datetime.utcfromtimestamp(val), "%m-%d-%Y")
        self.assertEqual(my_datetime(val), expected)

    def test41(self):
        val = 253402214400
        # 12-31-9999, first second of last date tested in assignment
        expected = datetime.strftime(datetime.utcfromtimestamp(val), "%m-%d-%Y")
        self.assertEqual(my_datetime(val), expected)

    def test42(self):
        val = 253402300799
        # 12-31-9999, last second of last date tested in assignment
        expected = datetime.strftime(datetime.utcfromtimestamp(val), "%m-%d-%Y")
        self.assertEqual(my_datetime(val), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
