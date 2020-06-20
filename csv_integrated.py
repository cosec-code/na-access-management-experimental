import pandas as pd
import RPi.GPIO as GPIO
import MFRC522
import signal
import logging as log
import datetime
import time

start_time = time.time()

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted


def end_read(signal, frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()


# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()


while continue_reading:
    # Scan for cards
    (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        print("Card detected")

        # Get the UID of the card
        (status, uid) = MIFAREReader.MFRC522_Anticoll()

        # Print UID
        my_uid_string = "{},{},{},{},{}".format(str(uid[0]), str(uid[1]), str(uid[2]), str(uid[3]), str(uid[4]))

        # Gets assigned the main input given by the reader.
        term = my_uid_string

        # Uses Pandas to read the data from a .csv file containing the auth levels for all users and assigns them to a
        # data frame for easy manipulation.
        reader = pd.read_csv('file.csv')
        df1 = pd.DataFrame(reader)
        print(df1)

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
            GPIO.output(LED, GPIO.HIGH)  # Turn on LED
            time.sleep(5)  # Wait 5 Seconds
            GPIO.output(LED, GPIO.LOW)
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

    else:
           print("That is an invalid input. Retry again.")
           log.basicConfig(filename="save.log", level=log.INFO)
           log.info("Successful log: It is an incorrect input. Nothing logged.")
    end_time = time.time()
    total_time = end_time - start_time
    print(total_time)
