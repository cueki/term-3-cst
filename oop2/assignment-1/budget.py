from enum import Enum


class BudgetCategory(Enum):
    """Represents the different budget categories."""

    GAMES_ENTERTAINMENT = "Games and Entertainment"
    CLOTHING_ACCESSORIES = "Clothing and Accessories"
    EATING_OUT = "Eating Out"
    MISCELLANEOUS = "Miscellaneous"


class Budget:
    """Represents a budget for a specific category."""

    def __init__(self, category, total_amount):
        """Initialize a Budget.

        :param category: a BudgetCategory enum value
        :param total_amount: the total budget amount as a float
        """
        self._category = category
        self._total_amount = total_amount
        self._amount_spent = 0.0
        self._locked = False

    @property
    def category(self):
        """Return the budget category."""
        return self._category

    @property
    def total_amount(self):
        """Return the total budget amount."""
        return self._total_amount

    @property
    def amount_spent(self):
        """Return the amount spent so far."""
        return self._amount_spent

    @property
    def amount_remaining(self):
        """Return the remaining budget amount."""
        return self._total_amount - self._amount_spent

    @property
    def locked(self):
        """Return whether this budget is locked."""
        return self._locked

    @locked.setter
    def locked(self, value):
        """Set the locked status."""
        self._locked = value

    def __str__(self):
        """Return a formatted string of the budget status."""
        status = "LOCKED" if self._locked else "UNLOCKED"

        return f"""{self._category.value}:
            status: {status}
            amount spent: ${self._amount_spent:.2f}
            amount left: ${self.amount_remaining:.2f}
            total amount allocated: ${self._total_amount:.2f}"""

    def record_spending(self, amount):
        """Add to the amount spent in this budget.

        :param amount: the dollar amount spent
        """
        self._amount_spent += amount

    def percentage_used(self):
        """Return the percentage of the budget used."""
        if self._total_amount == 0:
            return 0.0
        return (self._amount_spent / self._total_amount) * 100
