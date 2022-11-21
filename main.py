from urllib.request import urlopen
from bs4 import BeautifulSoup


doc_link="https://doc.sd-praktika.ru/document.card.php?id=444356848&DNSID=wQ_Ypl3xCGsLsOPdq-eHdcg"

html = urlopen(doc_link)
bs = BeautifulSoup(html.read(), 'html.parser')
print (bs)

tableList = bs.find_all('table', {'class': 's-agree-comment__table'})

print ('tables=')
print (tableList)

for table in tableList:
    print(table.get_text())

