import pandas as pd
import logging as log
import datetime

# Temp fill in for the human readability while testing
print("Welcome to the reading concept tester!")

#loop through taking multiple codes
Input_code = "-1"
csvLoaded = False

while not Input_code == "":
    Input_code = input(str("Enter your code in the format (XX,XX,X,XXX,XX) or blank to quit: "))
    
    # Check if the program should be ended by blank user input
    if Input_code == "":
        break

    which_auth_file = input(str("Do you want to verify by the log file or by the CSV file: "))


    if which_auth_file.upper() == "CSV":
        # Gets assigned the main input given by the reader.
        term = Input_code

        # Uses Pandas to read the data from a .csv file containing the auth levels for all users and assigns them to a
        # data frame for easy manipulation.
        # Only load the file the frist time
        if not csvLoaded:
            reader = pd.read_csv('file.csv')
            df1 = pd.DataFrame(reader)
            print(df1)
            csvLoaded = True

        # Sorts through the CSV file for the matching row and then imports the auth level of the user as a list
        # for comparision.
        human_data = df1.loc[df1['RFID'] == term].values
        verification = "Full"

        # Verification printing.
        print(verification)
        print(human_data)

        # Takes the required data from the lists.
        access_level_data = human_data[0, 2]
        print(access_level_data)
        name = human_data[0, 1]
        RFID_used = human_data[0, 0]
        welcome = "\nWelcome"
        not_welcome = "\nYou are not welcome"

        # Sample if statement for testing.
        if access_level_data == verification:
            ver = 1
            print(welcome)
        else:
            ver = 2
            print(not_welcome)

        if ver == 1:
            did_it_work = "Approved entry."
        else:
            did_it_work = "Denied entry"

        log.basicConfig(filename="save.log", level=log.INFO)

        now = datetime.datetime.now()
        print("Current date and time : ")
        time_logger = now.strftime("%Y-%m-%d %H:%M:%S")
        print(time_logger)
        log.info("{} ({}) ({}), {}, (Time = {}), {}".format(name, RFID_used, access_level_data, did_it_work,
                                                                            time_logger, "Done by CSV"))
    elif which_auth_file == "Log":
        with open('save.log') as f:
            content = f.read().splitlines()

        print(content)

        # log.basicConfig(filename="save.log", level=log.INFO)

        # now = datetime.datetime.now()
        # print("Current date and time : ")
        # time_logger = now.strftime("%Y-%m-%d %H:%M:%S")
        # print(time_logger)
        # log.info("{} ({}) ({}), {}, (Time = {}), {}".format(name, RFID_used, access_level_data,
        # did_it_work, time_logger, "Done by CSV"))
    else:
        print("That is an invalid input. Retry again.")
        log.basicConfig(filename="save.log", level=log.INFO)
        log.info("Successful log: It is an incorrect input. Nothing logged.")