import pandas as pd
import logging as log
import datetime

print("Welcome to the new class based program for the Nexus Aurora access management project.")


class RFID_setup:
    def __init__(self, rfid_code):
        self.rfid_code = rfid_code

    def main_processing(self):
        reader = pd.read_csv('file.csv')
        df1 = pd.DataFrame(reader)
        print(df1)

        human_data = df1.loc[df1['RFID'] == self.rfid_code].values
        verification = "Full"

        access_level_data = human_data[0, 2]
        print(access_level_data)
        name = human_data[0, 1]
        rfid_used = human_data[0, 0]
        welcome = "\nWelcome"
        not_welcome = "\nYou are not welcome"

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
        log.info("{} ({}) ({}), {}, (Time = {}), {}".format(name, rfid_used, access_level_data, did_it_work,
                                                            time_logger, "Done by CSV"))


p = RFID_setup("21,70,3,214,38")
p.main_processing()





