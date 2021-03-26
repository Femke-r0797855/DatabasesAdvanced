import time
from bs4 import BeautifulSoup
import requests
import pymongo as mongo
import redis


#MongoDB aanmaken
client = mongo.MongoClient("mongodb://127.0.0.1:27017") #Connect to mongo db
db_BitCoin = client["BitCoinTransactie"]
col_BitCoin = db_BitCoin["BitCoin"]







  h = 0
  p = -1
  a = 'IetsAnders'
  for x in range(len(amount)):
    q = amount[x].replace(',', '')
    if float(h) <= float(q):
      a = amount[x]
      h = amount[x].replace(',', '')
      p = x
  output = a + ' ' + naam[p]
  print(a, naam[p])
  
  output = {"hash": naam[p] , "amount": a}
  x = col_BitCoin.insert_one(output)
