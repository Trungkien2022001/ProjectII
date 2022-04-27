import requests
from bs4 import BeautifulSoup
import time

filename ="Data/thoi_su/Thoi_su_"

with open('./URL/URL_thoi_su.txt', 'r', encoding='utf-8') as f:
    data = [s.strip() for s in f.readlines()]
length = len(data)
for i in range(0, length):
    name = filename +str(i)+".txt"
    f1 = open(name, "w", encoding='utf-8')
    url = data[i]
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    
    # write header
    for link in soup.find_all("h1", {"class":"title-detail"}):
        text = str(link.text)
        f1.write(text)
        f1.write("\n")
    # Write description
    for link in soup.find_all("p", {"class":"description"}):
        text = str(link.text)
        f1.write(text)
        f1.write("\n")
    # Write content
    for link in soup.find_all("p", {"class":"Normal"}):
        text = str(link.text)
        f1.write(text)
        f1.write("\n")
    print(i)
    f1.close()
    time.sleep(1)
    


f.close()
        




