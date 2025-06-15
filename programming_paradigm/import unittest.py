import unittest
from bank_account import BankAccount

#python

class TestBankAccount(unittest.TestCase):
    def test_initialization(self):
        acc = BankAccount("12345", 100)
        self.assertEqual(acc.account_number, "12345")
        self.assertEqual(acc.account_balance, 100)
        acc2 = BankAccount("67890")
        self.assertEqual(acc2.account_balance, 0)

    def test_deposit_positive(self):
        acc = BankAccount("111", 50)
        result = acc.deposit(100)
        self.assertTrue(result)
        self.assertEqual(acc.account_balance, 150)

    def test_deposit_zero_negative(self):
        acc = BankAccount("222", 20)
        self.assertFalse(acc.deposit(0))
        self.assertFalse(acc.deposit(-10))
        self.assertEqual(acc.account_balance, 20)

    def test_withdraw_valid(self):
        acc = BankAccount("333", 200)
        result = acc.withdraw(50)
        self.assertTrue(result)
        self.assertEqual(acc.account_balance, 150)

    def test_withdraw_exact_balance(self):
        acc = BankAccount("444", 75)
        self.assertTrue(acc.withdraw(75))
        self.assertEqual(acc.account_balance, 0)

    def test_withdraw_insufficient_funds(self):
        acc = BankAccount("555", 30)
        self.assertFalse(acc.withdraw(40))
        self.assertEqual(acc.account_balance, 30)

    def test_withdraw_zero_negative(self):
        acc = BankAccount("666", 60)
        self.assertFalse(acc.withdraw(0))
        self.assertFalse(acc.withdraw(-5))
        self.assertEqual(acc.account_balance, 60)

    def test_display_balance(self):
        acc = BankAccount("777", 10)
        acc.deposit(90)
        acc.withdraw(50)
        self.assertEqual(acc.display_balance(), 50)

    def test_str_method(self):
        acc = BankAccount("888", 123.45)
        self.assertEqual(str(acc), "Account 888: Current Balance: 123.45")

    def test_deposit_withdraw_float(self):
        acc = BankAccount("999", 0)
        acc.deposit(100.75)
        self.assertEqual(acc.account_balance, 100.75)
        acc.withdraw(50.25)
        self.assertEqual(acc.account_balance, 50.5)

    def test_sequence_operations(self):
        acc = BankAccount("000", 10)
        acc.deposit(40)
        acc.withdraw(25)
        self.assertEqual(acc.display_balance(), 25)

if __name__ == '__main__':
    unittest.main()