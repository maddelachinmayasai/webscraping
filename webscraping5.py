import requests
import pandas as pd
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_="KzDlHZ")
name=[]
for i in names:
    d=i.get_text()
    name.append(d)
print(name)
prices=soup.find_all('div',class_="Nx9bqj _4b5DiR")
price=[]
for i in prices:
    d=i.get_text()
    price.append(d)
print(price)
rates=soup.find_all('div',class_="Nx9bqj _4b5DiR")
rate=[]
for i in rates:
    d=i.get_text()
    price.append(d)
print(rate)
images=soup.find_all('img',class_="DByuf4")
image=[]
for i in images:
    d=i['src']
    image.append(d)
print(image)
links=soup.find_all('link',class_="KzDlHZ")
link=[]
for i in links:
    d="https://www.flipkart.com" + i['href']
    link.append(d)
print(link)