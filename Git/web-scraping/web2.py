#Used to make requests
import urllib.request

def finder(value):
    un = data.find(value)
    deux = data.find('>',un)
    trois = data.find('<',deux)
    final = data[deux+1:trois]
    return " ".join(final.split())

#url = "https://www.amazon.fr/Asus-Q87M-Carte-Intel-Socket/dp/B00ECDC2WA/ref=sr_1_3?keywords=carte+m%C3%A8re+socket+1150&qid=1566238842&s=gateway&sr=8-3"
url = "https://www.amazon.fr/dp/B002CQU14A/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B002CQU14A&pd_rd_w=6hmfh&pf_rd_p=76623467-ab4f-4e3d-b621-316747e68298&pd_rd_wg=FtVwj&pf_rd_r=VQE369NGQD0Q3JXXPZZF&pd_rd_r=de190a12-7deb-411e-9829-3a82e4da682b&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRU1UT1ZHQ0JPT09YJmVuY3J5cHRlZElkPUEwODE2NjM5VUdWQUk4NEJKTjRMJmVuY3J5cHRlZEFkSWQ9QTA3NTYxNTUxRFRWWkxDSThVTzVCJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
x = urllib.request.urlopen(url)
x = x.read()
data = x.decode("UTF-8")

print(finder("productTitle"))
print(finder("PriceString"))
