""" 
    Title: delreal_usersp2.py
    Author: Professor Krasso
    Modified by: Hannah Del Real
    Date: 4 July 2023
    Description: Connecting Python with MongoDB
"""
# Import mongoDBClient
from pymongo import MongoClient
import datetime
# Create a connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.ozktyyu.mongodb.net/web335DBretryWrites=true&w=majority")

print(client)

# Assign web335 database to variable db
db = client['web335DB']

# Create space between outputs
print()

# Create a new user document to be added to the users collection
monteverdi = {
    "firstName": "Claudio",
    "lastName": "Monteverdi",
    "employeeId": "1014",
    "email": "cmonteverdi@me.com",
    "dateCreated": datetime.datetime.utcnow()
}

# Add newly created document to users collection
monteverdi_user_id = db.users.insert_one(monteverdi).inserted_id

#print result of insertion
print(monteverdi_user_id)


# Create a query to verify that document has been inserted to users collection
print(db.users.find_one({ "employeeId": "1014"}))

# Create a query to update the value of email field for newly created document
db.users.update_one(
    {"employeeId": "1014"},
    {
        "$set": {
            "email": "claudio.montver@me.com"
        }
    }
)

# Create a query to verify that email has been updated
print(db.users.find_one({"employeeId": "1014"}))


# Create a query to delete newly updated document and display results
result = db.users.delete_one({"employeeId": "1014"})
print(result)


# Create a query to verify that document has been deleted
print(db.users.find_one({"employeeId": "1014"}))
