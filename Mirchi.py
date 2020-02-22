  
import requests
import json
from bs4 import BeautifulSoup

data= []
val=[]
h={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'}
url='http://www.radiomirchi.com/more/tamil-top-20'
r=requests.get(headers=h,url=url)
s=BeautifulSoup(r.content,'html.parser')
b=s.find_all('div',class_='header')

for i in range(1,21): 
    Movie=b[i-1].find_all('h3')
    SongTitle=b[i-1].find_all('h2')
    a = str(Movie[0])
    val=a.split("<br/>")   
    data.append({'Movie':val[0].replace("<h3>"," ").strip() ,'SongTitle': str(SongTitle[0]).replace("<h2>"," ").replace("</h2>"," ").strip(),'Artist':val[1].replace("\n", " ").replace("</h3>"," ").replace(","," ").strip(),'Rank':i})
    a=range(1,21)
z=dict(zip(a,data))    
    with open('Inputjson.json','w') as f:
     json.dump(str(z),f)