import requests
from bs4 import BeautifulSoup
 
urls = 'https://vnexpress.net/phap-luat-p1'
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')

# opening a file in write mode
f = open("URL_phap-luat.txt", "a")

"""Tìm những URL dẫn đến những bài viết con: Trong trang chủ, đường dẫn được bao trong thẻ h3, class ="title-news".
Với trang web khác thì đường dẫn có thể trong thẻ khác"""

for link in soup.find_all("h3", {"class":"title-news"}):
    data = link.a.get('href')
    print(data)
    f.writelines(data)
    f.write("\n")
f.close()

   