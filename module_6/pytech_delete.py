# William Silknitter
# June 27th, 2021
# Prof. Sampson
# PyTech: Updating Documents

from pymongo import MongoClient
from getch import pause_exit

url  = "mongodb+srv://admin:admin@cluster0.lvixm.mongodb.net/pytech?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
db = client.pytech
students = db.students

docs = students.find({})

print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")
for doc in docs:
    print("Student ID: {}\nFirst Name: {}\nLast Name: {}".format(doc["student_id"], doc["first_name"], doc["last_name"]))
    print()

# This is the argument for the data being inserted into to the database
newStudent = {"student_id": "1010", "first_name": "Johnny", "last_name" : "Test"}

students.insert_one(newStudent)

studs = [newStudent]

print(" -- INSERT STATEMENTS -- ")
for student in studs:
    print("Inserted student record {} {} into the students collection with document_id {} ".format(student["first_name"], student["last_name"], student["_id"]))
    print()


testDoc = students.find_one({"student_id": "1010"})
print(" -- DISPLAYING STUDENT TEST DOC -- ")
print("Student ID: {}\nFirst Name: {}\nLast Name: {}".format(testDoc["student_id"], testDoc["first_name"], testDoc["last_name"]))
print()

# This is the argument for the filter within the delete_one method.
delFilter = {"student_id" : "1010"}

students.delete_one(delFilter)

newDocs = students.find({})
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")
for doc in newDocs:
    print("Student ID: {}\nFirst Name: {}\nLast Name: {}".format(doc["student_id"], doc["first_name"], doc["last_name"]))
    print()

print("\n\n")
pause_exit(0, 'End of program, press any key to exit... ')