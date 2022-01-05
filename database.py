from pymongo import MongoClient

#create the connection url
connecturl = "mongodb://127.0.0.1:27017/"

# connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)


# select the 'training' database 

db = connection.training

# select the 'python' collection 

collection = db.mongodb_glossary

# method for inserting data
def insertdata(name,num,gen,room,add):
    d={"Name":name,"Number":num,"Gender":gen,"Room no.":room,"Address":add}
    db.collection.insert_one(d)

def deletedata(name,num,gen,room,add):
    d={"Name":name,"Number":num,"Gender":gen,"Room no.":room,"Address":add}
    db.collection.delete_one(d)
