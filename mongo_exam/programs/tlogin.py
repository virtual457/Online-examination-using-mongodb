import pymongo
client = pymongo.MongoClient("127.0.0.1",27017)
db=client.miniproject
b=list(db.teachers.find())
print(b) 
db.teachers.remove({})
def insert(tid,tname,tsub):
    db.questions.insert_one({"Tid":tid,"Tname":tname,"Tsub":tsub})
insert("1","chadnan","OS")
insert("2","vinay","DBMS")
insert("3","dheemanth","FLAT")
insert("4","vishwanath","CN")
a=list(db.questions.find())
print("inserion sucessfull")
for i in a:
	for key,val in i.items():
		if(key != "_id"):
			print(key,"=>",val) 