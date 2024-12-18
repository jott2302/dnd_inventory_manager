
import pandas as pd
from openpyxl.styles.builtins import total

from manage_wallet_funcs import manage_currencies, convert_between_currencies, convert_to_excel_wallet
import unittest
from unittest.mock import patch


class TestManageCurrencies(unittest.TestCase):
    def setUp(self):
        self.data_frame =pd.DataFrame({"Currency": ["CP", "SP", "GP", "PP"],
                "Amount": [10, 10, 10, 10]})


    @patch("builtins.input", side_effect=["CP", "+10", "0"])
    def test_add_to_valid_currency(self, mock_input):
        manage_currencies(self.data_frame)
        updated_cp_value = self.data_frame.loc[self.data_frame["Currency"] == "CP", "Amount"].iloc[0]
        self.assertEqual(updated_cp_value, 20)

    @patch("builtins.input", side_effect=["SP", "-10", "0"])
    def test_remove_from_valid_currency(self, mock_input):
        manage_currencies(self.data_frame)
        updated_sp_value = self.data_frame.loc[self.data_frame["Currency"] == "SP", "Amount"].iloc[0]
        self.assertEqual(updated_sp_value, 0)

    @patch("builtins.input", side_effect=["gp", "0", "0"])
    def test_lowercase_currency(self, mock_input):
        manage_currencies(self.data_frame)
        gp_value = self.data_frame.loc[self.data_frame["Currency"] == "GP", "Amount"].iloc[0]
        self.assertEqual(gp_value, 10)

    @patch("builtins.input", side_effect=["PP", "-2","PP","-3", "PP", "-5", "0"])
    def test_remove_multiple_times_from_valid_currency(self, mock_input):
        manage_currencies(self.data_frame)
        updated_pp_value = self.data_frame.loc[self.data_frame["Currency"] == "PP", "Amount"].iloc[0]
        self.assertEqual(updated_pp_value, 0)

    @patch("builtins.input", side_effect=["EE", "SP", "+8", "0"])
    @patch("builtins.print")
    def test_wrong_currency_name(self, mock_input, mock_print):
        manage_currencies(self.data_frame)
        updated_sp_value = self.data_frame.loc[self.data_frame["Currency"] == "SP", "Amount"].iloc[0]
        self.assertEqual(updated_sp_value, 18)

    @patch("builtins.input", side_effect=["xx", "x", ".", "1", "0"])
    def test_unfamiliar_func_inputs(self, mock_input):
        manage_currencies(self.data_frame)
        cp_value = self.data_frame.loc[self.data_frame["Currency"] == "CP", "Amount"].iloc[0]
        sp_value = self.data_frame.loc[self.data_frame["Currency"] == "SP", "Amount"].iloc[0]
        gp_value = self.data_frame.loc[self.data_frame["Currency"] == "GP", "Amount"].iloc[0]
        pp_value = self.data_frame.loc[self.data_frame["Currency"] == "PP", "Amount"].iloc[0]
        self.assertEqual(cp_value, 10)
        self.assertEqual(sp_value, 10)
        self.assertEqual(gp_value, 10)
        self.assertEqual(pp_value, 10)

    @patch("builtins.input", side_effect=["GP", "-11", "0"])
    def test_total_negative_amount(self, mock_input):
        manage_currencies(self.data_frame)
        gp_value = self.data_frame.loc[self.data_frame["Currency"] == "GP", "Amount"].iloc[0]
        self.assertEqual(gp_value, 10)


class TestConvertBetweenCurrencies(unittest.TestCase):
    def test_valid_conversion_upwards(self):
        sp_amount = convert_between_currencies("CP", "SP", 10)
        self.assertEqual(sp_amount,1)

    def test_valid_conversion_downwards(self):
        gp_amount = convert_between_currencies("PP", "GP", 20)
        self.assertEqual(gp_amount, 200)

    def test_unknown_currency(self):
        unknown_from_currency = convert_between_currencies("XX", "SP", 10)
        unknown_to_currency = convert_between_currencies("CP", "XX", 10)
        self.assertFalse(unknown_from_currency)
        self.assertFalse(unknown_to_currency)

    def test_negative_int_amount(self):
        negative_int_amount = convert_between_currencies("SP", "GP", -1)
        string_amount = convert_between_currencies("SP", "GP", "10")
        self.assertFalse(negative_int_amount)
        self.assertFalse(string_amount)

    def test_conversion_from_same_currency(self):
        same_currency = convert_between_currencies("GP", "GP", 2)
        self.assertFalse(same_currency)

    def test_conversion_currency_type_integer(self):
        type_integer_currency = convert_between_currencies(1, "CP", 10)
        self.assertFalse(type_integer_currency)


class TestConvertToExcelWallet(unittest.TestCase):
    def setUp(self):
        self.data_frame = pd.DataFrame({"Currency": ["CP", "SP", "GP", "PP"],
            "Amount": [10, 10, 10, 10]})

    def test_valid_conversion_upwards(self):
        convert_to_excel_wallet(self.data_frame, "CP", "SP", 10)
        remaining_cp = self.data_frame.loc[self.data_frame["Currency"] == "CP", "Amount"].iloc[0]
        total_sp = self.data_frame.loc[self.data_frame["Currency"] == "SP", "Amount"].iloc[0]
        self.assertEqual(remaining_cp, 0)
        self.assertEqual(total_sp, 11)
    def test_valid_conversion_downwards(self):
        convert_to_excel_wallet(self.data_frame, "SP", "CP", 10)
        remaining_sp = self.data_frame.loc[self.data_frame["Currency"] == "SP", "Amount"].iloc[0]
        total_cp = self.data_frame.loc[self.data_frame["Currency"] == "CP", "Amount"].iloc[0]
        self.assertEqual(remaining_sp, 0)
        self.assertEqual(total_cp, 110)
    def test_same_currency_conversion(self):
        convert_to_excel_wallet(self.data_frame, "CP", "CP", 10)
        total_and_remaining_cp = self.data_frame.loc[self.data_frame["Currency"] == "CP", "Amount"].iloc[0]
        self.assertEqual(total_and_remaining_cp,10)
    def test_negative_amount_input(self):
        convert_to_excel_wallet(self.data_frame, "GP", "SP", -10)
        total_sp = self.data_frame.loc[self.data_frame["Currency"] == "SP", "Amount"].iloc[0]
        self.assertEqual(total_sp,10)
    def test_non_integer_amount(self):
        func_return = convert_to_excel_wallet(self.data_frame, "PP", "GP", 9.5)
        self.assertFalse(func_return)
    def test_insufficient_amount(self):
        convert_to_excel_wallet(self.data_frame, "SP", "GP", 11)
        total_sp = self.data_frame.loc[self.data_frame["Currency"] == "SP", "Amount"].iloc[0]
        total_gp = self.data_frame.loc[self.data_frame["Currency"] == "CP", "Amount"].iloc[0]
        self.assertEqual(total_sp, 10)
        self.assertEqual(total_gp, 10)

    def test_invalid_currency(self):
        func_return = convert_to_excel_wallet(self.data_frame, "XX", "XX", 10)
        self.assertFalse(func_return)
