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

filter = {"student_id": "1007"}
update = {"$set": {"last_name": "Builder II"}}

students.update_one(filter, update)

doc = students.find_one({"student_id": "1007"})
print(" -- DISPLAYING STUDENT DOCUMENT {} -- ".format(doc["student_id"]))
print("Student ID: {}\nFirst Name: {}\nLast Name: {}".format(doc["student_id"], doc["first_name"], doc["last_name"]))
print("\n\n")

pause_exit(0, 'End of program, press any key to exit... ')