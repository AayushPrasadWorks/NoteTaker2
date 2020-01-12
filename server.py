import pymongo

myclient = pymongo.MongoClient('localhost', 27017)
db = myclient["test"]
cl = mydb["test"]


dicts = { "name": "John", "message": "hello", "date": "00/00/00"}

x = cl.insert_one(dicts)
y =  cl.find({},{ "name": 1, "message": 1 })
print(x)
print(y)
