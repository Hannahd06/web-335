# Import mongoDBClient
from pymongo import MongoClient
# Create a connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.ozktyyu.mongodb.net/web335DBretryWrites=true&w=majority")

print(client)

# Assign web335 database to variable db
db = client['web335DB']

print("Listing of all users in the web335 collection")
# Call the find function to display all users in the collection, displaying only firstName and LastName
for user in db.users.find({}, {"firstName": 1, "lastName": 1}):
    print(user)

print("Displaying information for employeeId: 1011")
# Call the find_one function to display a document with employeeId: 1011
print(db.users.find_one({"employeeId": "1011"}))

print("Displaying information for lastName: Mozart")
# Call the find_one function to display a document with the lastName Mozart
print(db.users.find_one({"lastName": "Mozart"}))