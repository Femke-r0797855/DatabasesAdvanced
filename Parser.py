import time
from bs4 import BeautifulSoup
import requests
import pymongo as mongo
import redis

#MongoDB aanmaken
client = mongo.MongoClient("mongodb://127.0.0.1:27017") #Connect to mongo db
db_BitCoin = client["BitCoinTransactie"]
col_BitCoin = db_BitCoin["BitCoin"]


#Gegevens uit Redis halen
def parse():
  highest = 0
  plaats = -1
  name = 'IetsAnders'
  
  #print("Ik ben niet lui")
  r = redis.Redis()
  for key in r.keys():
    naam = key
    data = r.get(key)
    x = data.split("-")
    print()
    
    if float(highest)< x[0]:
      name = naam
      highest = x[0]
    
  print(str(name) + str(highest))
  
  
#Timer
while True:
  x = []
  parse()
  time.sleep(60)
