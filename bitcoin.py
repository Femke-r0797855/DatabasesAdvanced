import time
from bs4 import BeautifulSoup
import requests
import pymongo as mongo

#Database aanmaken
client = mongo.MongoClient("mongodb://127.0.0.1:27017") #Connect to mongo db

db_BitCoin = client["BitCoinTransactie"]
col_BitCoin = db_BitCoin["BitCoin"]

#File maken als deze niet bestaat
#f = open("LogBitCoinMost.txt", "w")
#Scaper
def scrape():
  url = 'https://www.blockchain.com/btc/unconfirmed-transactions'
  r = requests.get(url)
  soup = BeautifulSoup(r.content, features="html.parser")

  naam = soup.find_all('a', attrs={'class': 'sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK'})
  amount = soup.find_all('span', attrs={'class': 'sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC'})
  for tag in range(len(naam)):
    #print(tag.text.strip())
    datam.append(naam[tag].text[1:])
    #print(amount[x].text.strip())

  for tag in range(len(amount)):
    if amount[tag].text.find('$') ==0:
      dataa.append(amount[tag].text[1:])
      #print(amount)
    
  highest(datam, dataa)
  

def highest(naam, amount):
  if len(naam) == 0: #Dit is omdat ik soms een index out of range kreeg ik weet ook nie hoe maar nu gaat die da opnieuw proberen zodat die shit wel doet
    scrape()
  #print(len(naam))
  #print(len(amount))
  h = 0
  p = -1
  a = 'koeloekoeloe'
  for x in range(len(amount)):
    q = amount[x].replace(',', '')
    if float(h) <= float(q):
      a = amount[x]
      h = amount[x].replace(',', '')
      p = x
  output = a + ' ' + naam[p]
  print(a, naam[p])
  #Maakt file
  #f = open("LogBitcoinMost.txt", "a")
  #f.write(output)
  #f.write("\n")
  #f.close()
  
  output = {"hash": naam[p] , "amount": a}
  x = col_BitCoin.insert_one(output)



while True:
  datam =  []
  dataa = []
  scrape()
  time.sleep(60)
