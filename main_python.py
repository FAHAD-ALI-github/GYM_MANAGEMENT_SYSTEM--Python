from datetime import *
from tabulate import tabulate

data_file = "Gym_database.txt"
gym_splits_1 = """1 - Three day split
Day 1: push day — chest, shoulders, triceps.
Day 2: pull day — back, biceps, forearms.
Day 3: legs day — quads, glutes, hamstrings, calves.
Day 4: push day — chest, shoulders, triceps.
Day 5: pull day — back, biceps, forearms.
Day 6: legs day — quads, glutes, hamstrings, calves.
Day 7: rest day\n\n"""

gym_splits_2 = """2 - Five-Day Split (recommended for beginners)
Day 1: Chest—4-5 exercises, 3-4 sets, 6-15 reps.
Day 2: Back— 5 exercises, 3-4 sets, 6-15 reps.
Day 3: Shoulders, upper traps— 4-5 exercises, 3-4 sets, 6-15 reps.
Day 4: Biceps, triceps— 3-4 exercises each, 3-4 sets, 6-15 reps.
Day 5: Legs— 5-6 exercises, 3-4 sets, 6-15 reps.
Day 6-7: Rest.\n\n"""

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]


def new_registration():
    date_ = datetime.now()
    day_name = date_.strftime("%A")
    print(day_name, date_)
    file_list = []
    file = open(data_file, "r")
    for line in file:
        a = line.split("\t")
        file_list.append(a)
    file.close()
    id = 1 + int(file_list[-1][0])
    bmic = "--"
    name = input("ENTER YOUR FULL NAME   :  ").strip().title()
    dob = input("Enter your date of birth  --> dd-mm-yyyy :  ")
    weight = input("Enter your weight (in kg)  :  ")
    height = input("Enter your height (in cm) :  ")
    x = int(weight) / ((int(height)/100) ** 2)
    if x < 18.5:
        bmic = 'Underweight'
    if (x >= 18.5) and (x < 25):
        bmic = "Normal"
    if (x >= 25) and (x < 30):
        bmic = 'Overweight'
    if x >= 30:
        bmic = 'Obesity'
    username = input("Create a USERNAME : ").strip().upper()
    password = input("Create a password : ").strip().upper()
    no_of_days = 0
    print("Which gym split do you want to take? \n", gym_splits_1, gym_splits_2)
    split_num = input("Enter 1 or 2  :  ")
    fee_status = "NOT PAID\n"

    data_line = (str(id) + "\t" + name + "\t" + username + "\t" + password + "\t" + dob + "\t" + weight +
                 "\t" + height + "\t" + bmic + "\t" + day_name + "\t" + str(date_) + "\t" + str(no_of_days) + "\t" +
                 split_num + "\t" + fee_status)
    file = open(data_file, 'a')
    file.write(data_line)
    file.close()

def read_all():
    with open(data_file, "r") as file:
        file_list = []
        for line in file:
            fields = line.strip().split("\t")
            dob = fields[4]
            age_ = calculate_age(dob)
            file_list.append([
                fields[0],                  # ID
                fields[1],                  # Name
                age_,                       # Age
                fields[5] + " kg",          # Weight
                fields[6] + " cm",          # Height
                fields[7],                  # BMI
                fields[9][:19],             # Join Date
                fields[10],                 # Days
                "Split " + fields[11],      # Split
                fields[12].strip()          # Fee status
            ])

    headers = ["ID", "Name", "Age", "Weight", "Height", "BMI", "Join Date", "Days", "Split", "Fee Status"]
    print(tabulate(file_list, headers=headers, tablefmt="fancy_grid"))


def today_game(x, y):
    today = datetime.now().weekday()
    if today == 6:
        print("TODAY IS REST DAY ")
        exit()
    split_ = x
    joining_day = y
    splits_1 = ["push day — chest, shoulders, triceps.", "pull day — back, biceps, forearms."
            , "legs day — quads, glutes, hamstrings, calves.", "push day — chest, shoulders, triceps."
            , "pull day — back, biceps, forearms.", "legs day — quads, glutes, hamstrings, calves."
            , "push day — chest, shoulders, triceps.", "pull day — back, biceps, forearms."
            , "legs day — quads, glutes, hamstrings, calves.", "push day — chest, shoulders, triceps."
            , "pull day — back, biceps, forearms.", "legs day — quads, glutes, hamstrings, calves."]
    splits_2 = ["Chest—4-5 exercises, 3-4 sets, 6-15 reps."
               , "Back— 5 exercises, 3-4 sets, 6-15 reps."
               , "Shoulders, upper traps— 4-5 exercises, 3-4 sets, 6-15 reps."
               , "Biceps, triceps— 3-4 exercises each, 3-4 sets, 6-15 reps."
               , "Legs— 5-6 exercises, 3-4 sets, 6-15 reps.", "Rest day"
               , "Chest—4-5 exercises, 3-4 sets, 6-15 reps."
               , "Back— 5 exercises, 3-4 sets, 6-15 reps."
               , "Shoulders, upper traps— 4-5 exercises, 3-4 sets, 6-15 reps."
               , "Biceps, triceps— 3-4 exercises each, 3-4 sets, 6-15 reps."
               , "Legs— 5-6 exercises, 3-4 sets, 6-15 reps.", "Rest day"]
    if split_ == '1':
        if joining_day == 'Monday':
            print(splits_1[6 + today])
        if joining_day == 'Tuesday':
            print(splits_1[6 + today-1])
        if joining_day == 'Wednesday':
            print(splits_1[6 + today-2])
        if joining_day == 'Thursday':
            print(splits_1[6 + today-3])
        if joining_day == 'Friday':
            print(splits_1[6 + today-4])
        if joining_day == 'Saturday':
            print(splits_1[6 + today-5])
    if split_ == '2':
        if joining_day == 'Monday':
            print(splits_2[6 + today])
        if joining_day == 'Tuesday':
            print(splits_2[6 + today-1])
        if joining_day == 'Wednesday':
            print(splits_2[6 + today-2])
        if joining_day == 'Thursday':
            print(splits_2[6 + today-3])
        if joining_day == 'Friday':
            print(splits_2[6 + today-4])
        if joining_day == 'Saturday':
            print(splits_2[6 + today-5])


def change_password(id, new_password):
    file = open(data_file, "r")
    n = 1  # var 'n' is made to count no. of lines
    no_of_lines = 0
    file_list = []
    for line in file:
        a = line.split("\t")
        file_list.append(a)
        no_of_lines = n
        n += 1
    file.close()

    for i in range(no_of_lines):
        if file_list[i][0] == id:
            file_list[i][3] = new_password
            break

    # remove all text from the text file
    file = open(data_file, "r+")
    file.truncate(0)
    file.close()
    # updating text file
    file = open(data_file, 'a')
    for i in range(no_of_lines):
        file.write(file_list[i][0] + "\t" + file_list[i][1] + "\t" + file_list[i][2] + "\t" +
                   file_list[i][3] + "\t" + file_list[i][4] + "\t" + file_list[i][5] + "\t" +
                   file_list[i][6] + "\t" + file_list[i][7] + "\t" + file_list[i][8] + "\t" +
                   file_list[i][9] + "\t" + file_list[i][10] + "\t" + file_list[i][11] +
                   "\t" + file_list[i][12])
    file.close()


def attendance():
    while True:
        file = open(data_file, "r")
        n = 1  # var 'n' is made to count no. of lines
        no_of_lines = 0
        file_list = []
        for line in file:
            a = line.split("\t")
            file_list.append(a)
            no_of_lines = n
            n += 1
        file.close()

        id = input("Enter ID#  (if many then separated by commas) : ").split(",")
        for i in range(len(id)):
            x = int(id[i])
            y = int(file_list[x - 1][10])
            y += 1
            file_list[x - 1][10] = y

        # remove all text from the text file
        file = open(data_file, "r+")
        file.truncate(0)
        file.close()
        # updating text file
        file = open(data_file, 'a')
        for i in range(no_of_lines):
            file.write(file_list[i][0] + "\t" + file_list[i][1] + "\t" + file_list[i][2] + "\t" +
                       file_list[i][3] + "\t" + file_list[i][4] + "\t" + file_list[i][5] + "\t" +
                       file_list[i][6] + "\t" + file_list[i][7] + "\t" + file_list[i][8] + "\t" +
                       file_list[i][9] + "\t" + str(file_list[i][10]) + "\t" + file_list[i][11] +
                       "\t" + file_list[i][12])
        file.close()
        print("Successfully done !\n")
        h = input("""    Enter 0 to close attendance app
    or ENTER ANY number to again take attendance\n\t>>> """)
        if int(h) == 0:
            break


def fees_updated():
    file = open(data_file, "r")
    file_list = []
    n = 1  # var 'n' is made to count no. of lines
    no_of_lines = 0
    for line in file:
        a = line.split("\t")
        file_list.append(a)
        no_of_lines = n
        n += 1
    file.close()
    # updated list
    id_ = input("Enter ID#  (if many then separated by commas) : ").split(",")
    for i in range(len(id_)):
        file_list[int(id_[i])-1][-1] = "'PAID'\n"
    # remove all text from the text file
    file = open(data_file, "r+")
    file.truncate(0)
    file.close()
    # updating text file
    file = open(data_file, 'a')
    for i in range(no_of_lines):
        file.write(file_list[i][0] + "\t" + file_list[i][1] + "\t" + file_list[i][2] + "\t" +
                   file_list[i][3] + "\t" + file_list[i][4] + "\t" + file_list[i][5] + "\t" +
                   file_list[i][6] + "\t" + file_list[i][7] + "\t" + file_list[i][8] + "\t" +
                   file_list[i][9] + "\t" + file_list[i][10] + "\t" + file_list[i][11] + "\t" + file_list[i][12])
    file.close()
    print("Successfully updated the fee status of the user !\n")


def fees_not_paid():
    file = open(data_file, 'r')
    for line in file:
        full_line = line.split("\t")
        id = full_line[0]
        name = full_line[1]
        fee_status = full_line[-1].strip()
        if fee_status == "NOT PAID":
            print("id # ", id, "   NAME _ ", name)
    file.close()

def age(dob):
    day, month, year = dob.split("-")
    day = int(day)
    month = int(month)
    year = int(year)
    # CURRENT DATE
    date_ = datetime.now().today()
    current_day = date_.day
    current_month = date_.month
    current_year = date_.year
    # CALCULATE AGE
    if current_day < day:
        current_day += 30
        current_month -= 1
    age_day = current_day - day
    if current_month < month:
        current_month += 12
        current_year -= 1
    age_month = current_month - month
    age_year = current_year - year
    age_ = ("YOUR AGE IS : " + str(age_year) + " years, " + str(age_month) + " months, " + str(age_day) + " days")
    return age_


def calculate_age(dob):
    day, month, year = map(int, dob.split("-"))
    today = datetime.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    return f"{age} yrs"
