# William Silknitter
# June 20th, 2021
# Prof. Sampson
# PyTech: Collection Creation

from pymongo import MongoClient
from getch import pause_exit

url  = "mongodb+srv://admin:admin@cluster0.lvixm.mongodb.net/pytech?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(url)
db = client.pytech


print(" -- Pytech COllection List -- ")
print(db.list_collection_names())
print("\n")

pause_exit(0, 'Press any key to exit... ')