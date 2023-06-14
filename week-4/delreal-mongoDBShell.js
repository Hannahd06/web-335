/**
	Title: delreal-mongoDBShell.js
    Author: Professor Krasso
    Date: 13 June 2023
    Description: MongoDB Shell Scripts for the users collection.
 */

// Query to display all documents in users collection
db.users.find();

// Query to find user with email address jbach@me.com 
db.users.find({email: "jbach@me.com"});

// Query to find user with lastName Mozart
db.users.find({lastName: "Mozart"});

// Query to find user with firstName Richard
db.users.find({firstName: "Richard"});

// Query to find user with employeeId 1010 
db.users.find({employeeId: "1010"}); 
