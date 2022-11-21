import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ms=requests.session()
auth_link="https://doc.sd-praktika.ru/auth.php"

ua = UserAgent()

header = {
    'User-Agent': ua.chrome
}


data = {
    'group_id': '34118',
    'login' : 'msorokin',
    'user_id': '40845392',
    'password': 'zPe3HARa*ard'
}

response = ms.post(auth_link, data=data, headers=header).text

doclink='https://doc.sd-praktika.ru/document.card.php?id=444356848'

doc_response=ms.get(doclink, headers=header)

print(doc_response.text)
