import mysql.connector

# TODO: do not store username/password in code files.  This user has read-only access to a database of fake information.
cnx = mysql.connector.connect(user='crof2003_AccessManagementReadDev', password='hoL9dBuIKVq8uKL479DTEpCPET99', host='johnny.heliohost.org', database='crof2003_NA_Access_Management_Dev01')
cursor = cnx.cursor()

#loop through taking multiple codes
inRFID = "-1"
csvLoaded = False

while not inRFID == "":

    #inRFID = "51,37,7,973,53"
    inRFID = input(str("Enter your code in the format (XX,XX,X,XXX,XX) or blank to quit: "))

    # Check if the program should be ended by blank user input
    if inRFID == "":
        break

    #cursor.execute(query, inRFID)
    query = ("SELECT access_Code, Authorisation_Level, Name, RFID FROM AccessKeysTest WHERE RFID = \"")
    cursor.execute(query + inRFID + "\"")

    for (access_Code, Authorisation_Level, Name, RFID) in cursor:
        print("{} has auth level: {}.  RFID:{}".format( Name, Authorisation_Level, RFID))

cursor.close()
cnx.close()