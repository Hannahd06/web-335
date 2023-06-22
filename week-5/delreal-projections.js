/**
	Title: delreal-projections.js
    Author: Professor Krasso
    Date: 20 June 2023
    Description: MongoDB Shell Scripts for the users collection.
 */

// Add a new user to the users collection
db.users.insertOne({
	"firstName": "George",
	"lastName": "Handel",
	"employeeId": "1013",
	"email": "ghandel@me.com",
	"dateCreated": new Date()
});

// Query to update Mozart email to mozart@me.com
db.users.updateOne({"email": "wmozart@me.com"}, { $set: {"email": "mozart@me.com"}})

// Query to verify email has been updated to mozart@me.com
db.users.find( {"email": "mozart@me.com"} );

// Alternative query to verify email has been updated to mozart@me.com
db.users.aggregate([{$match: {"email": "mozart@me.com"}}]);

// Query to list all documents in the users collection for only firstName, lastName, and email
db.users.find({}, {"firstName": 1, "lastName": 1, "email": 1, "_id": 0});

// Alternative query to list all documents in the users collection for only firstName, lastName, and email
db.users.aggregate({$project: {"_id": 0, "firstName": 1, "lastName": 1, "email": 1}});