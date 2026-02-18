class BankAccount:
    """Represents a user's bank account."""

    def __init__(self, account_number, bank_name, balance):
        """Initialize a BankAccount.

        :param account_number: the bank account number as a string
        :param bank_name: name of the bank
        :param balance: the starting balance as a float
        """
        self._account_number = account_number
        self._bank_name = bank_name
        self._balance = balance

    @property
    def account_number(self):
        """Return the account number."""
        return self._account_number

    @property
    def bank_name(self):
        """Return the bank name."""
        return self._bank_name

    @property
    def balance(self):
        """Return the current balance."""
        return self._balance

    def withdraw(self, amount):
        """Withdraw an amount from the balance.

        :param amount: the dollar amount to withdraw
        :return: True if successful, False if insufficient funds
        """
        if amount > self._balance:
            return False
        self._balance -= amount
        return True
