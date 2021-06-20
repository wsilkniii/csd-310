# William Silknitter
# June 20th, 2021
# Prof. Sampson
# PyTech: Collection Insert

from pymongo import MongoClient
from getch import pause_exit

url  = "mongodb+srv://admin:admin@cluster0.lvixm.mongodb.net/pytech?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
db = client.pytech
students = db.students

student1 =  { "student_id" : "1007", "first_name" : "Bob", "last_name" : "Builder"}
student2 =  { "student_id" : "1008", "first_name" : "Ben", "last_name" : "Awad"}
student3 =  { "student_id" : "1009", "first_name" : "Nick", "last_name" : "White"}

bob = students.insert_one(student1).inserted_id
ben = students.insert_one(student2).inserted_id
nick = students.insert_one(student3).inserted_id

studs = [student1, student2, student3]

print(" -- INSERT STATEMENTS -- ")
for student in studs:
    print("Inserted student record {} {} into the students collection with document_id {} ".format(student["first_name"], student["last_name"], student["_id"]))

pause_exit(0, 'Press any key to exit... ')