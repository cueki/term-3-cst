# Assignment 1 - F.A.M. (Family Appointed Moderator)

## Team Members
- **Madison Lovett** - Student Number: A01292253
- **Tony Chen** - Student Number: A01415041

## Description
The F.A.M. is a parental control lock on a child's bank account. It registers users, tracks all their spending across budget categories, and locks them out if they go overboard.

## How to Run
```
python driver.py
```
Three test users (Garfield, Snoopy, Mickey) are loaded automatically on startup.

## How It Works
The main menu gives you three options:

1. **Register a new user** - Walk through entering the child's name, date of birth, bank details, budget amounts, and user type.
2. **Login as an existing user** - Pick from the list of users. Locked accounts show up as "LOCKED" and can't be logged into.
3. **Exit** - Quit the program.

After logging in, you get the user menu:

1. **View Budgets** - Shows each budget's status (locked/unlocked), amount spent, amount left, and total allocated.
2. **Record a Transaction** - Enter an amount, pick a category from a list, and type in the shop name. The system checks for sufficient funds and whether the category is locked before recording.
3. **View Transactions by Budget** - Pick a category and see all transactions in it.
4. **View Bank Account Details** - Shows the user's name, age, account info, current balance, and a list of all transactions.
5. **Logout** - Back to the main menu.

## Features Implemented
- User registration with full input validation (dates, numbers, ranges)
- `load_test_users()` with the three hardcoded users
- Support for multiple users with the ability to switch between them
- All four budget categories: Games and Entertainment, Clothing and Accessories, Eating Out, Miscellaneous
- Transaction recording with timestamp, amount, category selection from a list, and shop name
- Transactions blocked if they would bring the balance below zero
- Bank balance updates after each transaction
- Budget notifications at different thresholds depending on user type
- Budget category lockout for Troublemaker and Rebel
- Full account lockout for Rebel when 2+ categories are locked
- Locked accounts displayed in the login menu and blocked from logging in

## Known Limitations
- Data doesn't persist between sessions, everything resets when you restart the program
- No username/password login so users just pick their account from a list
- No GUI!

## Design

### OOP Stuff
- **Inheritance**: `User` is an ABC. `Angel`, `Troublemaker`, and `Rebel` extend it with their own thresholds and notification behavior.
- **Polymorphism**: `check_budget_notifications()` is called on a `User` reference and the correct subclass version runs automatically.
- **Composition**: `User` has-a `BankAccount`, a collection of `Budget` objects, and a collection of `Transaction` objects.
- **Encapsulation**: All classes use private attributes (`_name`, `_balance`, etc.) with property accessors to control access.
- **Law of Demeter**: `FAM` never reaches through `User` into `BankAccount` directly.

### SOLID Principles
1. **Single Responsibility**: Each class has one job. `BankAccount` manages the balance, `Budget` tracks spending per category, `Transaction` represents a purchase, `TransactionRecorder` handles validation and recording, and `FAM` runs the menus.
2. **Open/Closed**: New user types can be added by subclassing `User` and implementing the abstract methods -- no need to touch existing code.
3. **Liskov Substitution**: Angel, Troublemaker, and Rebel are all interchangeable wherever a `User` is expected.
4. **Interface Segregation**: The `User` ABC defines abstract methods (`check_budget_notifications`, `get_warning_threshold`, `get_lockout_threshold`) that each subclass implements differently.
