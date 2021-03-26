import time
from bs4 import BeautifulSoup
import requests
import pymongo as mongo
import redis

#MongoDB aanmaken
client = mongo.MongoClient("mongodb://127.0.0.1:27017") #Connect to mongo db
db_BitCoin = client["BitCoinTransactie"]
col_BitCoin = db_BitCoin["BitCoin"]


#Scaper
def scrape():
  url = 'https://www.blockchain.com/btc/unconfirmed-transactions'
  r = requests.get(url)
  soup = BeautifulSoup(r.content, features="html.parser")

  naam = soup.find_all('a', attrs={'class': 'sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK'})
  amount = soup.find_all('span', attrs={'class': 'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})

  #Data name
  for tag in range(len(naam)):
    #print(tag.text.strip())
    datan.append(naam[tag].text[1:])
    #print(amount[x].text.strip())

 #Data Amount
  for tag in range(len(amount)):
    if amount[tag].text.find('$') ==0:
      dataa.append(amount[tag].text[1:])
  
  #Data Bitcoin
  for tag in range(len(amount)):
    if amount[tag].text.find('BTC') > 0:
      datab.append(amount[tag].text[1:])

  cach(datan, dataa, datab)
  
#Caching in Redis
def cach(naam, amount):
  if len(naam) == 0: #Dit is omdat ik soms een index out of range kreeg ik weet ook nie hoe maar nu gaat die da opnieuw proberen zodat die shit wel doet
    scrape()


while True:
  datan =  [] #Data naam
  dataa = [] #Data Amount
  datab= [] #Data BitCoin
  datat=[] #Data Time
  scrape()
  time.sleep(60)
