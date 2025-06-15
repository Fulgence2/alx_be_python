import unittest
from bank_account import BankAccount
from io import StringIO
import sys

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)

    def test_initial_balance(self):
        self.assertEqual(self.account.account_balance, 100)

    def test_deposit_positive_amount(self):
        result = self.account.deposit(50)
        self.assertTrue(result)
        self.assertEqual(self.account.account_balance, 150)

    def test_deposit_zero_amount(self):
        result = self.account.deposit(0)
        self.assertTrue(result)
        self.assertEqual(self.account.account_balance, 100)

    def test_deposit_negative_amount(self):
        result = self.account.deposit(-10)
        self.assertFalse(result)
        self.assertEqual(self.account.account_balance, 100)

    def test_withdraw_valid_amount(self):
        result = self.account.withdraw(50)
        self.assertTrue(result)
        self.assertEqual(self.account.account_balance, 50)

    def test_withdraw_zero_amount(self):
        result = self.account.withdraw(0)
        self.assertFalse(result)
        self.assertEqual(self.account.account_balance, 100)

    def test_withdraw_negative_amount(self):
        result = self.account.withdraw(-10)
        self.assertFalse(result)
        self.assertEqual(self.account.account_balance, 100)

    def test_withdraw_more_than_balance(self):
        result = self.account.withdraw(200)
        self.assertFalse(result)
        self.assertEqual(self.account.account_balance, 100)

    def test_withdraw_entire_balance(self):
        result = self.account.withdraw(100)
        self.assertTrue(result)
        self.assertEqual(self.account.account_balance, 0)

    def test_display_balance_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.account.display_balance()
        sys.stdout = sys.__stdout__
        self.assertIn("Current Balance: $100.00", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()