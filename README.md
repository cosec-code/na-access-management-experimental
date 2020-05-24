## log2-access-management
# Lead by u/Zam
log2-access-management - On Mars we will have to treat the entire colony as one giant building. Most systems will be interconnected, so first of all we need to distinguish between: colonist personal health and safety, key system protection, workplace health and safety, police services, disaster and accident response, privacy and finally data and information IT system protection. For key systems User Access Management based on typical industrial solutions may be sufficient. RFID based access cards working as keys would be best, as they also allow to identify the user (by ID, so we can make it work while maintaining privacy) and not only identify if they had permission to access, but in case of later issues, system could check what threats each ID may have been exposed to (industrial fumes, sections not shielded from radiation, waste etc.).

concept.py: Written by u/aRandomCheapPerson(pkdecv#5640). It contains the base sorting code for the CSV files in order to quickly authenticate without connection to a server in case of lost connection or an emergency.

generator.py: Written by THEWILDOFFICIAL. Contains code for generating a CSV file containing randomized RFID codes and several other factors of 1,000,000 rows into a file: data.csv.

integrated_read.py: Written by a user on the website Medium. Boilerplate code for the reading of the RFID key.

integrated.py: Written by u/aRandomCheapPerson(pkdecv#5640). Combines integrated_read.py and concept.py.

databaseConnectionTest.py: Written by u/Crof2003.  Proof-of-concept of connecting to a hosted MySQL service.  This would be similar to the proposed final setup of the readers to database servers.  This MySQL database is currently hosted at heliohost.org.