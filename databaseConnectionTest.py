import mysql.connector

cnx = mysql.connector.connect(user='crof2003_AccessManagementReadDev', password='hoL9dBuIKVq8uKL479DTEpCPET99', host='johnny.heliohost.org', database='crof2003_NA_Access_Management_Dev01')
cursor = cnx.cursor()

query = ("SELECT access_Code, Authorisation_Level, Name, RFID FROM AccessKeysTest WHERE RFID = \"")

inRFID = "51,37,7,973,53"

#cursor.execute(query, inRFID)
cursor.execute(query + inRFID + "\"")

for (access_Code, Authorisation_Level, Name, RFID) in cursor:
  print("{} has auth level: {}.  RFID:{}".format( Name, Authorisation_Level, RFID))

cursor.close()
cnx.close()