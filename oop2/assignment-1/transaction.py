from datetime import datetime


class Transaction:
    """Represents a single financial transaction."""

    def __init__(self, amount, budget_category, shop_name):
        """Initialize a Transaction.

        :param amount: the dollar amount as a float
        :param budget_category: a BudgetCategory enum value
        :param shop_name: name of the shop/website
        """
        self._timestamp = datetime.now()
        self._amount = amount
        self._budget_category = budget_category
        self._shop_name = shop_name

    @property
    def timestamp(self):
        """Return the transaction timestamp."""
        return self._timestamp

    @property
    def amount(self):
        """Return the transaction amount."""
        return self._amount

    @property
    def budget_category(self):
        """Return the budget category."""
        return self._budget_category

    @property
    def shop_name(self):
        """Return the shop name."""
        return self._shop_name

    def __str__(self):
        """Return a formatted string of the transaction."""
        formatted_time = self._timestamp.strftime("%Y-%m-%d %H:%M:%S")
        return (
            f"{formatted_time} | ${self._amount:.2f} | "
            f"{self._budget_category.value} | {self._shop_name}"
        )


class TransactionRecorder:
    """Helper class to validate and record transactions for a user."""

    @staticmethod
    def record_transaction(user, amount, budget_category, shop_name):
        """Validate and record a transaction and update the relevant budget.

        :param user: the purchaser as a User object
        :param amount: the dollar amount as a float
        :param budget_category: a BudgetCategory enum value
        :param shop_name: name of the shop/website as a String
        :return: True if successful, False otherwise
        """

        if user.is_budget_locked(budget_category):
            print(f"{budget_category.value} - category locked!")
            return False

        if not user.has_sufficient_funds(amount):
            print(f"Insufficient funds!")
            return False

        transaction = Transaction(amount, budget_category, shop_name)

        user.withdraw_funds(amount)

        user.add_transaction(transaction)

        user.record_budget_spending(budget_category, amount)

        user.check_budget_notifications(budget_category)

        return True
