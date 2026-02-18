from datetime import datetime
from budget import Budget, BudgetCategory
from bank_account import BankAccount
from transaction import TransactionRecorder
from user import Angel, Troublemaker, Rebel


def _get_valid_input(prompt, cast_type, min_value=None, max_value=None):
    """Prompt the user until a valid input of the given type is entered.

    :param prompt: the input prompt string
    :param cast_type: the type to cast to
    :param min_value: optional minimum value for range validation
    :param max_value: optional maximum value for range validation
    :return: the validated input value
    """
    while True:
        try:
            value = cast_type(input(prompt))

            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Value must be at most {max_value}.")
                continue

            return value

        except ValueError:
            print(f"Invalid input. Please enter a valid {cast_type.__name__}.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            raise
        except Exception as e:
            print(f"Unexpected error: {e}. Please try again.")


class FAM:
    """Main application controller for the F.A.M. system."""

    def __init__(self):
        """Initialize the FAM system."""
        self._users = []

    def load_test_users(self):
        """Load hardcoded test users for testing purposes."""
        garfield = Troublemaker(
            name="Garfield",
            date_of_birth=datetime(2010, 6, 19),
            bank_account=BankAccount("1234-5678", "RBC", 1000.00),
            budgets={
                BudgetCategory.GAMES_ENTERTAINMENT: Budget(
                    BudgetCategory.GAMES_ENTERTAINMENT, 200.00
                ),
                BudgetCategory.CLOTHING_ACCESSORIES: Budget(
                    BudgetCategory.CLOTHING_ACCESSORIES, 150.00
                ),
                BudgetCategory.EATING_OUT: Budget(BudgetCategory.EATING_OUT, 100.00),
                BudgetCategory.MISCELLANEOUS: Budget(
                    BudgetCategory.MISCELLANEOUS, 50.00
                ),
            },
        )

        snoopy = Rebel(
            name="Snoopy",
            date_of_birth=datetime(2008, 10, 4),
            bank_account=BankAccount("8765-4321", "TD", 800.00),
            budgets={
                BudgetCategory.GAMES_ENTERTAINMENT: Budget(
                    BudgetCategory.GAMES_ENTERTAINMENT, 100.00
                ),
                BudgetCategory.CLOTHING_ACCESSORIES: Budget(
                    BudgetCategory.CLOTHING_ACCESSORIES, 100.00
                ),
                BudgetCategory.EATING_OUT: Budget(BudgetCategory.EATING_OUT, 100.00),
                BudgetCategory.MISCELLANEOUS: Budget(
                    BudgetCategory.MISCELLANEOUS, 100.00
                ),
            },
        )

        mickey = Angel(
            name="Mickey",
            date_of_birth=datetime(2009, 11, 18),
            bank_account=BankAccount("1111-2222", "BMO", 1200.00),
            budgets={
                BudgetCategory.GAMES_ENTERTAINMENT: Budget(
                    BudgetCategory.GAMES_ENTERTAINMENT, 250.00
                ),
                BudgetCategory.CLOTHING_ACCESSORIES: Budget(
                    BudgetCategory.CLOTHING_ACCESSORIES, 200.00
                ),
                BudgetCategory.EATING_OUT: Budget(BudgetCategory.EATING_OUT, 150.00),
                BudgetCategory.MISCELLANEOUS: Budget(
                    BudgetCategory.MISCELLANEOUS, 100.00
                ),
            },
        )

        self._users.extend([garfield, snoopy, mickey])

    def register_user(self):
        """Prompt the user to register a new child user."""
        name = input("Enter the user's name: ")

        year = _get_valid_input(
            "Enter the user's year of birth (all digits; eg. 2001): ",
            int,
            min_value=1900,
            max_value=datetime.now().year,
        )
        month = _get_valid_input(
            "Enter the user's month of birth (two digits; eg 09 for September): ",
            int,
            min_value=1,
            max_value=12,
        )
        day = _get_valid_input(
            "Enter the user's day of birth (two digits; eg. 01 for the 1st): ",
            int,
            min_value=1,
            max_value=31,
        )

        # Validate the complete date
        while True:
            try:
                date_of_birth = datetime(year, month, day)
                break
            except ValueError as e:
                print(f"Invalid date: {e}")
                day = _get_valid_input(
                    "Enter the user's day of birth (two digits; eg. 01 for the 1st): ",
                    int,
                    min_value=1,
                    max_value=31,
                )

        bank_name = input("Enter the user's Bank account name: ")
        bank_account_number = input("Enter the bank account number: ")
        bank_balance = _get_valid_input("Enter the bank balance in dollars: ", float)
        bank_account = BankAccount(bank_account_number, bank_name, bank_balance)

        budget_games_entertainment = _get_valid_input(
            "Enter the budget (in dollars) for games and entertainment: ", float
        )
        budget_cloths_accessories = _get_valid_input(
            "Enter the budget (in dollars) for clothing accessories: ", float
        )
        budget_eating_out = _get_valid_input(
            "Enter the budget (in dollars) for eating out: ", float
        )
        budget_miscellaneous = _get_valid_input(
            "Enter the budget (in dollars) for miscellaneous: ", float
        )

        budgets = {
            BudgetCategory.GAMES_ENTERTAINMENT: Budget(
                BudgetCategory.GAMES_ENTERTAINMENT, budget_games_entertainment
            ),
            BudgetCategory.CLOTHING_ACCESSORIES: Budget(
                BudgetCategory.CLOTHING_ACCESSORIES, budget_cloths_accessories
            ),
            BudgetCategory.EATING_OUT: Budget(
                BudgetCategory.EATING_OUT, budget_eating_out
            ),
            BudgetCategory.MISCELLANEOUS: Budget(
                BudgetCategory.MISCELLANEOUS, budget_miscellaneous
            ),
        }

        user_type_map = {"1": Angel, "2": Troublemaker, "3": Rebel}
        while True:
            print("Select user type:")
            print("1. Angel")
            print("2. Troublemaker")
            print("3. Rebel")
            user_type_choice = input("Enter choice (1-3): ")

            if user_type_choice in user_type_map:
                user_class = user_type_map[user_type_choice]
                new_user = user_class(name, date_of_birth, bank_account, budgets)
                self._users.append(new_user)
                break
            else:
                print("Invalid user type. Please try again.")

    def login_menu(self):
        """Display the list of users and allow login selection."""
        while True:
            number_of_users = len(self._users)
            print("\nSelect user to log in as:")
            for i in range(number_of_users):
                lock_status = " - LOCKED" if self._users[i].account_locked else ""
                print(
                    f"{i + 1}. {self._users[i].name} ({self._users[i].user_type}){lock_status}"
                )

            print("0. Return to main menu")

            try:
                selection = int(input("Enter selection: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if selection == 0:
                break

            user_index = selection - 1
            if user_index in range(number_of_users):
                if self._users[user_index].account_locked:
                    print("Unable to log in: account locked")
                else:
                    user = self._users[user_index]
                    self.user_menu(user)
            else:
                print("Invalid user number.")

    def user_menu(self, user):
        """Display the user menu after login.

        :param user: the logged-in User object
        """
        while True:
            print(f"\nLogged in as {user.name} ({user.user_type}).")
            print("Select from one of the options below:")
            print("1. View Budgets")
            print("2. Record a Transaction")
            print("3. View Transactions by Budget")
            print("4. View Bank Account Details")
            print("5. Logout")

            choice = input("\nEnter choice: ")

            if choice == "1":
                self._view_budgets(user)
            elif choice == "2":
                self._input_transaction(user)
                if user.account_locked:
                    break
            elif choice == "3":
                self._view_transactions_by_budget(user)
            elif choice == "4":
                self._view_bank_account_details(user)
            elif choice == "5":
                print("Logging out...")
                break
            else:
                print("Invalid choice.")

    @staticmethod
    def _view_budgets(user):
        """Display all budgets associated with the user.

        :param user: the logged-in User object"""
        print(f"\n{user.name}'s Budgets: ")
        for category, budget in user.budgets.items():
            print(budget)

    @staticmethod
    def _select_budget_category(prompt="Select category:"):
        """Prompt the user to select a budget category.

        :param prompt: the header prompt to display
        :return: the selected BudgetCategory, or None if invalid
        """
        category_map = {
            "1": BudgetCategory.GAMES_ENTERTAINMENT,
            "2": BudgetCategory.CLOTHING_ACCESSORIES,
            "3": BudgetCategory.EATING_OUT,
            "4": BudgetCategory.MISCELLANEOUS,
        }

        print(f"\n{prompt}")
        print("1. Games and Entertainment")
        print("2. Clothing and Accessories")
        print("3. Eating Out")
        print("4. Miscellaneous")
        choice = input("Enter choice (1-4): ")

        if choice not in category_map:
            print("Invalid category.")
            return None

        return category_map[choice]

    @staticmethod
    def _input_transaction(user):
        """Prompt user to enter transaction details.

        :param user: the logged-in User object"""
        amount = _get_valid_input("Enter transaction amount: $", float)
        if amount <= 0:
            print("Transaction amount must be a positive, non-zero number.")
            return

        category = FAM._select_budget_category()
        if category is None:
            return

        shop_name = input("Enter shop/website name: ")

        TransactionRecorder.record_transaction(user, amount, category, shop_name)

    def _view_transactions_by_budget(self, user):
        """Display all transactions group by budget type

        :param user: the logged-in User object"""
        category = self._select_budget_category("Select category to view:")
        if category is None:
            return
        transactions = user.get_transactions_by_category(category)

        print(f"\n{category.value} Transactions:")
        if transactions:
            for t in transactions:
                print(t)
        else:
            print("No transactions in this category.")

    @staticmethod
    def _view_bank_account_details(user):
        """Display all bank account details associated with the user,
        alongside the closing balance

        :param user: the logged-in User object"""
        account_summary = user.get_bank_account_summary()

        print(f"Bank Account Details:")
        print(f"Name: {user.name} (Age: {user.age})")
        print(f"Account Number: {account_summary['account_number']}")
        print(f"Bank Name: {account_summary['bank_name']}")
        print(f"Balance: ${account_summary['balance']:.2f}\n")

        transactions = user.get_transactions_all()
        for t in transactions:
            print(t)

    def main_menu(self):
        """Display the main menu and handle user input."""
        while True:
            print("\nWelcome to the Family Appointed Moderator (F.A.M.) system.")
            print("\nSelect option:")
            print("1. Register a new user")
            print("2. Login to existing user")
            print("3. Exit")
            selection = input("Enter choice (1-3): ")

            if selection == "1":
                self.register_user()
            elif selection == "2":
                self.login_menu()
            elif selection == "3":
                print("Thank you for using F.A.M. Goodbye!\n")
                break
            else:
                print("Invalid choice.\n")
