#Basic program
import requests
#result= requests.get("http://example.com/")
#print(type(result))
#print(result.text)
import bs4
#soup= bs4.BeautifulSoup(result.text,"lxml")
#print(soup)
#print(soup.select('title'))
#print(soup.select('title')[0].getText())
res= requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soupp=bs4.BeautifulSoup(res.text, "lxml")
for x in soupp.select('.toctext'):
    print(x.text)
