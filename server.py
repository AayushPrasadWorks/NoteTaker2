import pymongo

myclient = pymongo.MongoClient('localhost', 27017)
mydb = myclient["test"]
mycol = mydb["test"]


mydict = { "name": "John", "message": "hello", "date": "00/00/00"}

x = mycol.insert_one(mydict)
y =  mycol.find({},{ "name": 1, "message": 1 })
print(x)
print(y)
