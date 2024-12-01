
import pandas as pd
from manage_wallet_funcs import manage_currencies
import unittest
from unittest.mock import patch

data = {"Currency": ["CP","SP","GP","PP"],
                "Amount": [10,10,10,10]}
data_frame = pd.DataFrame(data)



class TestManageCurrencies(unittest.TestCase):
    @patch("builtins.input", side_effect=["CP", "+10", "0"])
    def test_add_to_valid_currency(self, mock_input):
        manage_currencies(data_frame)
        updated_cp_value = data_frame.loc[data_frame["Currency"] == "CP", "Amount"].iloc[0]
        self.assertEqual(updated_cp_value, 20)

    @patch("builtins.input", side_effect=["SP", "-10", "0"])
    def test_remove_from_valid_currency(self, mock_input):
        manage_currencies(data_frame)
        updated_sp_value = data_frame.loc[data_frame["Currency"] == "SP", "Amount"].iloc[0]
        self.assertEqual(updated_sp_value, 0)

    @patch("builtins.input", side_effect=["gp", "0", "0"])
    def test_lowercase_currency(self, mock_input):
        manage_currencies(data_frame)
        gp_value = data_frame.loc[data_frame["Currency"] == "GP", "Amount"].iloc[0]
        self.assertEqual(gp_value, 10)

    @patch("builtins.input", side_effect=["PP", "-2","PP","-3", "PP", "-5", "0"])
    def test_remove_multiple_times_from_valid_currency(self, mock_input):
        manage_currencies(data_frame)
        updated_pp_value = data_frame.loc[data_frame["Currency"] == "PP", "Amount"].iloc[0]
        self.assertEqual(updated_pp_value, 0)

    @patch("builtins.input", side_effect=["EE", "SP", "+8", "0"])
    @patch("builtins.print")
    def test_wrong_currency_name(self, mock_input, mock_print):
        manage_currencies(data_frame)
        updated_sp_value = data_frame.loc[data_frame["Currency"] == "SP", "Amount"].iloc[0]
        self.assertEqual(updated_sp_value, 8)

#data_frame nach jedem unittest clearen und mock_print recherchieren um expected prints mit actual prints zu vergleichen