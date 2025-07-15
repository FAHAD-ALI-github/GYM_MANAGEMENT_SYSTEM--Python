# admin.py
from main_python import *
from colorama import Fore, Style, init
from tabulate import tabulate
init(autoreset=True)

def admin_menu():
    print(Fore.CYAN + """
===================================================
               🛠️ ADMIN CONTROL PANEL 🛠️
===================================================
1. Add new member
2. View all members
3. Open attendance app
4. View unpaid members
5. Update fee status
0. Exit
""")

def run_admin():
    while True:
        admin_menu()
        choice = input(Fore.GREEN + "Choose an option: ").strip()

        if choice == '1':
            new_registration()
        elif choice == '2':
            read_all()
        elif choice == '3':
            attendance()
        elif choice == '4':
            fees_not_paid()
        elif choice == '5':
            fees_updated()
        elif choice == '0':
            print(Fore.BLUE + "Exiting Admin Panel...")
            break
        else:
            print(Fore.RED + "Invalid option. Try again.")

if __name__ == "__main__":
    run_admin()
