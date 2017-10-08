import pymongo

conn = pymongo.MongoClient()
db = conn.scrapy_mongo_demo #create a db , named scrapy_mongo_demo
table_test = db.test #create a table , named test

record_1 = {"name":"robin", "age":24, "gender":"male", "height":1.78}
record_2 = {"name":"Alice", "age":18, "hobby":"studying", "country":"china"}


#table_test.insert(record_1)
#table_test.insert(record_2)

#table_test.remove({"name":"Alice"})

print "DB operation done"
