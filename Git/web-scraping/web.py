import requests
from bs4 import BeautifulSoup
from scrapy import Selector
import re
import sys


#url = "https://www.amazon.fr/Asus-Q87M-Carte-Intel-Socket/dp/B00ECDC2WA/ref=sr_1_3?keywords=carte+m%C3%A8re+socket+1150&qid=1566238842&s=gateway&sr=8-3#customerReviews"
#url = "https://www.amazon.fr/Crosstour-T%C3%A9l%C3%A9commande-%C2%B0Grand-Angle-Rechargeables-Accessoires/dp/B073WX4VLJ?ref_=Oct_DLandingS_PC_8a9a3baa_0&smid=A35I3GL156ACTW "
#url = "https://www.amazon.fr/Dim-Ecodim-X5-Chaussettes-Homme/dp/B07G9KY9LJ/ref=zg_bs_apparel_10?_encoding=UTF8&refRID=ES2R61JKX7XXGBPZXCG4"
#url = "https://www.amazon.fr/%C3%89lectrique-Automatique-Rechargeable-Ajustables-Sensibilit%C3%A9/dp/B07GWQCN53?ref_=Oct_BSellerC_2036699031_1&pf_rd_p=dc5196b1-87ae-5780-bcfa-85ec8eb024fc&pf_rd_s=merchandised-search-6&pf_rd_t=101&pf_rd_i=2036699031&pf_rd_m=A1X6FK5RDHNB96&pf_rd_r=2WZCS5PFNE6GZGJD49NT&pf_rd_r=2WZCS5PFNE6GZGJD49NT&pf_rd_p=dc5196b1-87ae-5780-bcfa-85ec8eb024fc"
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
