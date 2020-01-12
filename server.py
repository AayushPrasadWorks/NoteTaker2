import pymongo

class server:

    def
    def getPersonMessage(name):
        myclient = pymongo.MongoClient('localhost', 27017)
        db = myclient["test"]
        cl = db["test"]
        myquery = { "name": name }
        doc = cl.find(myquery)

        for x in doc:
            print(x)

        

    def add(name, message, date):
        myclient = pymongo.MongoClient('localhost', 27017)
        db = myclient["test"]
        cl = db["test"]
        di = { "name": name, "message": message, "date": date}
        cl.insert_one(di)


    def printAll():
        myclient = pymongo.MongoClient('localhost', 27017)
        db = myclient["test"]
        cl = db["test"]
        y = cl.find().sort("name", 1)
        for x in y:
            print(x)





    


server.getPersonMessage("Eddie")





    







