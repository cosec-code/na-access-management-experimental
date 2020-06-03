# log2-access-management
## Lead by u/Zam
log2-access-management - On Mars we will have to treat the entire colony as one giant building. Most systems will be interconnected, so first of all we need to distinguish between: colonist personal health and safety, key system protection, workplace health and safety, police services, disaster and accident response, privacy and finally data and information IT system protection. For key systems User Access Management based on typical industrial solutions may be sufficient. RFID based access cards working as keys would be best, as they also allow to identify the user (by ID, so we can make it work while maintaining privacy) and not only identify if they had permission to access, but in case of later issues, system could check what threats each ID may have been exposed to (industrial fumes, sections not shielded from radiation, waste etc.).

### concept.py: 
Written by u/aRandomCheapPerson(pkdecv#5640). It contains the base sorting code for the CSV files in order to quickly authenticate without connection to a server in case of lost connection or an emergency.



generator.py: Written by THEWILDOFFICIAL. Contains code for generating a CSV file containing randomized RFID codes and several other factors of 1,000,000 rows into a file: data.csv.

integrated_read.py: Written by a user on the website Medium. Boilerplate code for the reading of the RFID key.

### integrated.py: 
Written by u/aRandomCheapPerson(pkdecv#5640). Combines integrated_read.py and concept.py.

#### Mode of operation:
Defines the end reader function, then hooks the "SIGINT", then initializes the object MFRC522, required to read the RFID data off the fob being used for testing. Then, using an infinite while loop, it attempts to catch a signal from a nearby RFID transmitter, and if a signal is received, it is parsed into a string, then compared to a CSV based credential database, using the Pandas library. It first initializes a dataframe(EDITED BY u/aRandomCheapPerson to now initialize it at the beginning, at the suggestion of Crof in order to improve perfromance in each iteration of the loop), then it uses .values and loc methods to get the row matching the RFID key, then converts the row into a list. Then, using array reference, the permission of the entry is taken, and is compared to the required permission. If permission is present, and actuator will turn on and if not, it will deny entry.
Then, it will log the denied or accepted entry as a INFO level log into a .log file, which will then be commited to a higher hierarchial server.

##### To be done for integrated.py
Network code for commiting log files.
Decision on how to implement the framework in itself, since parsing on a RPI3B+ is slow, so separation of reading and sorting(Reading on RPI, Sorting on x86) may be in order.
Implementation of encryption and decryption.
