import urllib.request
from bs4 import BeautifulSoup
from scrapy import Selector
import re

url = "https://www.amazon.fr/Asus-Q87M-Carte-Intel-Socket/dp/B00ECDC2WA/ref=sr_1_3?keywords=carte+m%C3%A8re+socket+1150&qid=1566238842&s=gateway&sr=8-3#customerReviews"
x = urllib.request.urlopen(url)
x = x.read()
data = x.decode("UTF-8")

soup = BeautifulSoup(data, 'html.parser')

sel = Selector(text=soup.prettify())
name = sel.xpath('//*[@id="feature-bullets"]/ul/li[2]/span').extract_first()
name = re.sub("<.*?>|</.*?>"," ",name)
name = name.lstrip()

prix = sel.xpath('//*[@id="priceblock_ourprice"]').extract_first()
prix = re.sub("<.*?>|</.*?>"," ",prix)
prix = prix.lstrip()

commentaire = sel.xpath('//*[@id="feature-bullets"]/ul').extract_first()
commentaire = re.sub("<.*?>|</.*?>"," ",commentaire)
commentaire = commentaire.split('\n')
commentaire = [i for i in commentaire if not i.isspace()]
del commentaire[0:5]
commentaire = [i.lstrip() for i in commentaire]


print(name)
print(prix)
print(commentaire)
