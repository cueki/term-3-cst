# Name: Madison Lovett
# Student number: A01292253

# Name: Tony Chen
# Student number: A01415041

from fam import FAM


def main():
    """Entry point for the F.A.M. application."""
    app = FAM()
    app.load_test_users()
    app.main_menu()


if __name__ == "__main__":
    main()
