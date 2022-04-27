from asyncio.windows_events import NULL
import requests
from bs4 import BeautifulSoup
 
urls = 'https://vnexpress.net/so-hoa/cong-nghe-p'
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')
i = 1
f = open("URL_cong-nghe.txt", "a")
while(1):
    grab = requests.get(urls + str(i) + '/')
    soup = BeautifulSoup(grab.text, 'html.parser')
    # print(soup.contents)
    for link in soup.find_all("h2", {"class":"title-news"}):
        data = link.a.get('href')
        f.writelines(data)
        f.write("\n")
    print(i)
    i += 1
    if i > 21 :
        break

   