import requests
from bs4 import BeautifulSoup
from scrapy import Selector
import re
import sys

url = input()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
r = requests.session()
response = r.get(url=url,headers = headers)
#print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
sel = Selector(text=soup.prettify())

name = sel.xpath('//*[@id="productTitle"]/text()').extract_first()
name = name.lstrip()

prix = sel.xpath('//*[@id="priceblock_ourprice"]').extract_first()
if prix == None : prix = sel.xpath('//*[@id="newBuyBoxPrice"]').extract_first()
if prix == None : prix = sel.xpath('//*[@id="price_inside_buybox"]').extract_first()


prix = re.sub("<.*?>|</.*?>"," ",prix)
prix = prix.lstrip()

commentaire = sel.xpath('//*[@id="feature-bullets"]/ul').extract_first()
commentaire = re.sub("<.*?>|</.*?>"," ",commentaire)
commentaire = commentaire.split('\n')
commentaire = [i for i in commentaire if not i.isspace()]
del commentaire[0:5]
commentaire = [i.lstrip() for i in commentaire]

descriptif = sel.xpath('//*[@id="prodDetails"]/div/div[1]/div[1]/div[2]/div/div/table/tbody').extract_first()
if descriptif == None : descriptif = sel.xpath('//*[@id="productDescription"]').extract_first()
descriptif = re.sub("<.*?>|</.*?>"," ",descriptif)
descriptif = descriptif.split('\n')
descriptif = [i for i in descriptif if not i.isspace()]
descriptif = [i.lstrip() for i in descriptif]

print("NAME  :" + name)
print("PRICE :" + prix)
print("COMMENT :")
for item in commentaire : print(item)
print("\nDESCRIPTION :")
if type(descriptif) == type([]) :
    for i in range(0,len(descriptif),2) : print(str(descriptif[i]) + " " + str(descriptif[i+1])) 
else : print(descriptif)
