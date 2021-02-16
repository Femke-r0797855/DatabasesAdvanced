import time
from bs4 import BeautifulSoup
import requests


datam =  []
dataa = []
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
  #print(naam)
  h = 0
  p = -1
  a = 'koeloekoeloe'
  for x in range(len(amount)):
    q = amount[x].replace(',', '')
    if float(h) <= float(q):
      a = amount[x]
      h = amount[x].replace(',', '')
      p = x
  print(a, naam[p])



while True:
  scrape()
  time.sleep(60)