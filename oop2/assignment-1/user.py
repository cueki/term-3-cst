from abc import ABC, abstractmethod
from datetime import datetime


class User(ABC):
    """Abstract base class for all user types."""

    def __init__(self, name, date_of_birth, bank_account, budgets):
        """Initialize a User.

        :param name: the user's name
        :param date_of_birth: the user's birthdate as a datetime object
        :param bank_account: a BankAccount object
        :param budgets: a dict mapping BudgetCategory to its budget
        """
        self._name = name
        self._date_of_birth = date_of_birth
        self._bank_account = bank_account
        self._budgets = budgets
        self._transactions = []
        self._account_locked = False

    @property
    def name(self):
        """Return the user's name."""
        return self._name

    @property
    def age(self):
        """Return the user's age in years."""
        today = datetime.now()
        age = today.year - self._date_of_birth.year

        if (today.month, today.day) < (
            self._date_of_birth.month,
            self._date_of_birth.day,
        ):
            age -= 1

        return age

    @property
    def bank_account(self):
        """Return the user's bank account."""
        return self._bank_account

    @property
    def budgets(self):
        """Return the user's budgets."""
        return self._budgets

    @property
    def transactions(self):
        """Return the user's transactions."""
        return self._transactions

    @property
    def account_locked(self):
        """Return whether the account is fully locked."""
        return self._account_locked

    @account_locked.setter
    def account_locked(self, value):
        """Set the account locked status."""
        self._account_locked = value

    @property
    @abstractmethod
    def user_type(self):
        """Return the user type as a string."""
        pass

    @abstractmethod
    def get_warning_threshold(self):
        """Return the warning threshold as a percentage (0-100)."""
        pass

    @abstractmethod
    def get_lockout_threshold(self):
        """Return the lockout threshold as a percentage, or None."""
        pass

    def add_transaction(self, transaction):
        """Add a transaction to the user's transaction list.

        :param transaction: a Transaction object
        """
        self._transactions.append(transaction)

    def get_transactions_all(self):
        """Return a list of all transactions."""
        return [t for t in self._transactions]

    def get_transactions_by_category(self, category):
        """Return all transactions for a given budget category.

        :param category: a BudgetCategory enum value
        :return: list of Transaction objects
        """
        return [t for t in self._transactions if t.budget_category == category]

    def has_sufficient_funds(self, amount):
        """Check if user has sufficient funds for a transaction.

        :param amount: the dollar amount to check
        :return: True if sufficient funds, False otherwise
        """
        return self._bank_account.balance >= amount

    def withdraw_funds(self, amount):
        """Withdraw funds from the user's bank account.

        :param amount: the dollar amount to withdraw
        :return: True if successful, False if insufficient funds
        """
        return self._bank_account.withdraw(amount)

    def is_budget_locked(self, budget_category):
        """Check if a budget category is locked.

        :param budget_category: a BudgetCategory enum value
        :return: True if locked, False otherwise
        """
        return self._budgets[budget_category].locked

    def record_budget_spending(self, budget_category, amount):
        """Record spending in a specific budget category.

        :param budget_category: a BudgetCategory enum value
        :param amount: the dollar amount spent
        """
        self._budgets[budget_category].record_spending(amount)

    def get_bank_account_summary(self):
        """Get a summary of bank account details.

        :return: dictionary with account_number, bank_name, balance
        """
        return {
            "account_number": self._bank_account.account_number,
            "bank_name": self._bank_account.bank_name,
            "balance": self._bank_account.balance,
        }

    def _print_category_transactions(self, category):
        """Print all transactions for a given budget category.

        :param category: a BudgetCategory enum value
        """
        for t in self.get_transactions_by_category(category):
            print(f"  {t}")

    @abstractmethod
    def check_budget_notifications(self, category):
        """Check and issue notifications for the given category.

        :param category: a BudgetCategory enum value
        """
        pass


class Angel(User):
    """Angel user type - minimal restrictions."""

    @property
    def user_type(self):
        """Return the user type."""
        return "Angel"

    def get_warning_threshold(self):
        """Return warning threshold (90%)."""
        return 90

    def get_lockout_threshold(self):
        """Return lockout threshold (never locked)."""
        return None

    def check_budget_notifications(self, category):
        """Check and issue notifications for the given category."""
        budget = self._budgets[category]
        percent = budget.percentage_used()

        if percent > 100:
            print(
                f"\nNotice: {self._name}, you have exceeded your "
                f"{category.value} budget."
            )
            self._print_category_transactions(category)
        elif percent > self.get_warning_threshold():
            print(
                f"\nNotice: {self._name}, you have used {percent:.1f}% of "
                f"your {category.value} budget."
            )
            self._print_category_transactions(category)


class Troublemaker(User):
    """Troublemaker user type - moderate restrictions."""

    @property
    def user_type(self):
        """Return the user type."""
        return "Troublemaker"

    def get_warning_threshold(self):
        """Return warning threshold (75%)."""
        return 75

    def get_lockout_threshold(self):
        """Return lockout threshold (120%)."""
        return 120

    def check_budget_notifications(self, category):
        """Check and issue notifications for the given category."""
        budget = self._budgets[category]
        percent = budget.percentage_used()

        if percent >= self.get_lockout_threshold():
            budget.locked = True
            print(
                f"\nWarning: {self._name}, you have been locked out of "
                f"{category.value}! (spent {percent:.1f}% of budget)"
            )
            self._print_category_transactions(category)
        elif percent > 100:
            print(
                f"\nWarning: {self._name}, you have exceeded your "
                f"{category.value} budget."
            )
            self._print_category_transactions(category)
        elif percent > self.get_warning_threshold():
            print(
                f"\nWarning: {self._name}, you have used {percent:.1f}% of "
                f"your {category.value} budget."
            )
            self._print_category_transactions(category)


class Rebel(User):
    """Rebel user type - strict restrictions."""

    @property
    def user_type(self):
        """Return the user type."""
        return "Rebel"

    def get_warning_threshold(self):
        """Return warning threshold (50%)."""
        return 50

    def get_lockout_threshold(self):
        """Return lockout threshold (100%)."""
        return 100

    def check_budget_notifications(self, category):
        """Check and issue notifications for the given category."""
        budget = self._budgets[category]
        percent = budget.percentage_used()

        if percent >= self.get_lockout_threshold():
            budget.locked = True
            print(
                f"\n{self._name}! You have been locked out of "
                f"{category.value}! (spent {percent:.1f}% of budget)"
            )
            self._print_category_transactions(category)

            # lock entire account if 2+ categories are locked
            locked_count = sum(1 for b in self._budgets.values() if b.locked)
            if locked_count >= 2:
                self._account_locked = True
                print(
                    f"\n{self._name}'s account has been LOCKED. "
                    f"{locked_count} budget categories exceeded."
                )
        elif percent > self.get_warning_threshold():
            print(
                f"\n{self._name}! You have used {percent:.1f}% of "
                f"your {category.value} budget!"
            )
            self._print_category_transactions(category)
