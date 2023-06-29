/**
	Title: delreal-aggregate-queries.js
    Author: Professor Krasso
    Date: 27 June 2023
    Description: MongoDB Shell Scripts for the houses and students collection.
 */

// Query to return all documents in house collection
db.houses.find();

// Query to return all documents in students collection
db.students.find();

// Query to add a document to the student’s collection
db.students.insertOne({"firstName": "Remus", "lastName": "Lupin", "studentId": "s1019", "houseId": "h1007"});

// Query to validate new student document has been added to students collection
db.students.find({"studentId": "s1019"});

// Query to delete newly created document
db.students.deleteOne({"firstName": "Remus"});

// Query to verify document has been deleted
db.students.find({"firstName": "Remus"});

// Query to show a list of students by house
db.houses.aggregate([{$lookup: {from: "students", localField: "houseId", foreignField: "houseId", as: "students"}}]);

// Query to show a list of students for house Gryffindor
db.houses.aggregate([{$lookup: {from: "students", localField: "houseId", foreignField: "houseId", as: "students"}}, {$match: {"founder": "Godric Gryffindor"}}]);

// Query to show a list of students for Eagle Mascot
db.houses.aggregate([{$match: {"mascot": "Eagle"}}, {$lookup: {from: "students", localField: "houseId", foreignField: "houseId", as: "students"}}]);
