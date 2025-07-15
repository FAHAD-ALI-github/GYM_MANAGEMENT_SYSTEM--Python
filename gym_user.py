# gym_user.py
from main_python import *
from colorama import Fore, Style, init
from tabulate import tabulate
init(autoreset=True)

def display_bmi(weight, height, bmi):
    x = int(weight) / ((int(height) / 100) ** 2)
    print(Fore.YELLOW + f"Your BMI is: {x:.2f}  ({bmi})")

def user_menu():
    print(Fore.CYAN + """
===================================================
                🏋️ GYM USER MENU 🏋️
===================================================
1. Change your password
2. See your age
3. See your BMI
0. Exit
""")

def login():
    print(Fore.GREEN + "Welcome to the Gym CLI")
    username_input = input("Enter your username or '1' for new registration: ").strip().upper()
    if username_input == '1':
        new_registration()
        return

    with open(data_file, "r") as file:
        for line in file:
            fields = line.strip().split("\t")
            if username_input == fields[2]:
                password_input = input("Enter password: ").strip().upper()
                if password_input == fields[3]:
                    id_, _, username_, password_, dob_, weight, height, bmi, joining_day, *_ = fields
                    print(Fore.CYAN + f"\nToday is {datetime.now().strftime('%A')}:\n")
                    today_game(fields[11], joining_day)

                    while True:
                        user_menu()
                        choice = input(Fore.GREEN + "Choose an option: ").strip()
                        if choice == '1':
                            old_pw = input("Enter current password: ").strip().upper()
                            if old_pw == password_:
                                new_pw = input("Enter new password: ").strip().upper()
                                confirm_pw = input("Confirm new password: ").strip().upper()
                                if new_pw == confirm_pw:
                                    change_password(id_, new_pw)
                                    print(Fore.GREEN + "Password updated successfully.")
                                else:
                                    print(Fore.RED + "Passwords do not match.")
                        elif choice == '2':
                            print(age(dob_))
                        elif choice == '3':
                            display_bmi(weight, height, bmi)
                        elif choice == '0':
                            print(Fore.BLUE + "Goodbye!")
                            exit()
                        else:
                            print(Fore.RED + "Invalid option.")
                    return
    print(Fore.RED + "User not found or incorrect password.")

if __name__ == "__main__":
    login()
