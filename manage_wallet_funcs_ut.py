import pandas as pd
from manage_wallet_funcs import manage_currencies
import unittest
from unittest.mock import patch

data = {"Currency": ["CP","SP","GP","PP"],
                "Amount": [10,10,10,10]}
data_frame = pd.DataFrame(data)


class TestManageCurrencies(unittest.TestCase):
    @patch("builtins.input", side_effect=["CP", "+10", "0"])
    @patch("builtins.print")
    def test_add_to_valid_currency(self, mock_input, mock_print):
        manage_currencies(data_frame)
        updated_cp_value = data_frame.loc[data_frame["Currency"] == "CP", "Amount"].iloc[0]
        self.assertEqual(updated_cp_value, 20)
