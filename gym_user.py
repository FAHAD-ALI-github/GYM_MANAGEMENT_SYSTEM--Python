from main_python import *

id_ = ""
username_ = ""
password_ = ""
dob_ = ""
weight = ""
height = ""
bmi = ""
split_number = ""
joining_day = ""


x = input("Enter your username OR press 1 for new registration : ").upper()
if x == '1':
    new_registration()
else:
    file = open(data_file, "r")
    for line in file:
        full_line = line.split("\t")
        id_ = full_line[0]
        username_ = full_line[2]
        password_ = full_line[3]
        dob_ = full_line[4]
        weight = full_line[5]
        height = full_line[6]
        bmi = full_line[7]
        split_number = full_line[11]
        joining_day = full_line[8]

        if x == username_:
            password = input("ENTER PASSWORD  :  ").strip().upper()
            if password == password_:
                day = datetime.now().strftime("%A")
                print(f"TODAY IS {day} :")
                today_game(split_number, joining_day)
                a = input("""\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    Enter 1 to change your password
    Enter 2 to see your age
    Enter 3 to see your Body Mass Index ( BMI )
    Or Enter 0 to end the PRoGRAM\n\t>>> """)
                if a == '1':
                    password = input("ENTER previous PASSWORD  :  ").strip().upper()
                    if password == password_:
                        password_ = input("ENTER new PASSWORD  :  ").strip().upper()
                        password__ = input("REWRITE PASSWORD  :  ").strip().upper()
                        if password__ == password_:
                            change_password(id_, password__)

                if a == '2':
                    print(age(dob_))

                if a == '3':
                    x = int(weight) / ((int(height) / 100) ** 2)
                    print(f"YOUR BODY MASS INDEX IS {x:.5}  (<<{bmi}>>)")

                if a == '0':
                    exit()
    file.close()
