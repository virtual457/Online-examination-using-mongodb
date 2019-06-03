import pymongo
client = pymongo.MongoClient("127.0.0.1",27017)
db=client.miniproject
def check(q_id,answer):
	b=list(db.questions.find())
	
	for i in b:
		print("inside i loop")
		print(i)
		b=int((q_id))
		a=int((i['Q_id']))
		if(a == b):
			c=i["A"]
			x=int(answer)
			y=int(c)
			break
	if(x==y):
		print("the answered option is correct")
		d =1
		return d
	else:
		print("entered option is wrong") 
		d = 0
		return d			
check(3,"0010")		
