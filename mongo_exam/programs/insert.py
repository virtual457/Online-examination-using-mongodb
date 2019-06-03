
import pymongo
client = pymongo.MongoClient("127.0.0.1",27017)
db=client.miniproject
b=list(db.questions.find())
print(b) 
db.questions.remove({})
def insert(q_id,question,options,answer,explanation):
    db.questions.insert_one({"Q_id":q_id,"Q":question,"O":options,"A":answer,"E":explanation})
insert("1","who is the great person",["chandan","vinay","dheemanth","all of the above"],"0000","because he is a legend")
insert("2","who is the great person",["chandan","vinay","dheemanth","all of the above"],"0001","because he is a legend")
insert("3","who is the great person",["chandan","vinay","dheemanth","all of the above"],"0010","because he is a legend")
insert("4","who is the great person",["chandan","vinay","dheemanth","all of the above"],"0100","because he is a legend")
insert("5","who is the great person",["chandan","vinay","dheemanth","all of the above"],"1000","because he is a legend")
a=list(db.questions.find())
print("inserion sucessfull")
for i in a:
	for key,val in i.items():
		if(key != "_id"):
			print(key,"=>",val) 