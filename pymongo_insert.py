# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database
dbname = get_database()
collection_name = dbname["links"]

item_1 = {
  "_id" : "U1IT00001",
  "topic_name" : "description here",
  "link": "www.facebook.com"
}

item_2 = {
  "_id" : "U1IT00002",
  "topic_name" : "description here",
  "link": "www.google.com"
}
collection_name.insert_many([item_1,item_2])