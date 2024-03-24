from main_python import *


while True:
    choice_selector = """\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    Enter 1 to a add new member.
    Enter 2 to view all gym-users data.
    Enter 3 to open attendance app.
    Enter 4 to view all the members those have not paid fees.
    Enter 5 to UPDATE fee status.
    Enter 0 to close app.
      >>> """
    choice = input(choice_selector)
    if int(choice) == 1:
        new_registration()
    elif int(choice) == 2:
        read_all()
    elif int(choice) == 3:
        attendance()
    elif int(choice) == 4:
        fees_not_paid()
    elif int(choice) == 5:
        fees_updated()
    elif int(choice) == 0:
        break
