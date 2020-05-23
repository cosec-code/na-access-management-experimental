import names
import random
import pandas


i = 0
namelist = []
authorisation = []
access_codes = []

alr_codes = []

RFID = []
while i< 1000000:
    access_level = ''
    person_name = names.get_first_name()
    namelist.append(person_name)

    access_code = random.randint(1000000,9999999)
    access_codes.append(access_code)

    authid = random.randint(0,2)

    if authid == 0:
        access_level = "Full"

    elif authid == 1:
        access_level = "None"

    elif authid == 2:
        access_level = "Basic"

    #authorisation.append(access_level)
    authorisation.append(authid)

    first = random.randint(10, 99)
    second = random.randint(10, 99)
    third = random.randint(0, 9)
    fourth = random.randint(100, 999)
    fifth = random.randint(10, 99)

    RFIDnum = "{},{},{},{},{}".format(first, second, third, fourth, fifth)

    RFID.append(RFIDnum)
    i +=1
    if i%1000 == 0:
        print('{:,}'.format(i) )

print("GENERATION DONE!")
df = pandas.DataFrame(data={"RFID":RFID, "Name":namelist, "Authorisation_Level": authorisation, "Access code": access_codes})
df.to_csv("./file.csv", sep=',', index=False)
