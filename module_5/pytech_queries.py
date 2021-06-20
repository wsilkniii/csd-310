# William Silknitter
# June 20th, 2021
# Prof. Sampson
# PyTech: Collection Queries

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

doc = students.find_one({"student_id": "1007"})
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM findOne() QUERY -- ")
print("Student ID: {}\nFirst Name: {}\nLast Name: {}".format(doc["student_id"], doc["first_name"], doc["last_name"]))
print("\n\n")

pause_exit(0, 'Press any key to exit... ')