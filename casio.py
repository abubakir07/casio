import requests 
from bs4 import BeautifulSoup as bs 
import json 
 
data = [] 
 
header = { 
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36' 
} 
 
for i in range(1, 10): 
    url = 'https://shop.casio.ru/catalog/?PAGEN_1={i}' 
    req = requests.get(url, headers=header) 
    response = req.content 
 
    soup = bs(response,'lxml') 
    articls = soup.find_all(class_='product-item__articul') 
    prize = soup.find_all(class_='product-item__price')
    link = soup.find_all(class_='product-item__link')
    # lst = [] 
    # for i in articls: 
    #     lst.append(i.text.strip())
    
    # lst_prize =[]
    # for i in prize: 
    #         lst_prize.append(i.text.strip())    
    
     
    c = 0 
    for i in link: 
        # href = 'https://shop.casio.ru/'+str(i.get('href')) 
        href ='https://shop.casio.ru/'+str(i.get('href'))
        dct = { 
            'model': articls[c].text.strip(),
            'price': prize[c].text.strip(), 
            'links': href 
            } 
        data.append(dct) 
        with open('lesson_5/dz/w_casio.json','w',encoding='utf-8') as file: 
            json.dump(data, file, indent=4, ensure_ascii=False)