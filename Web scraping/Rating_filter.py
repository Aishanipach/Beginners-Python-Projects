#Program to find three starred items on an e-commerce website

import requests
import bs4
ex_url="http://books.toscrape.com/catalogue/page-{}.html"
cur_page=ex_url.format(1)
res= requests.get(cur_page)
soup=bs4.BeautifulSoup(res.text,"lxml")
prod=soup.select('.product_pod')
ctr=0
for user in (prod):
    
    if(user.select('.star-rating.Three')==[]):
        pass
    else:
        print(user.select('a')[1]['title'])
    
