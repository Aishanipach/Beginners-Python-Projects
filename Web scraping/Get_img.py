import requests
import bs4

resultt= requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
sou=bs4.BeautifulSoup(resultt.text, "lxml")
img_src=""
y=0
for x in (sou.select('.thumbimage')): 
    y=y+1
    if y==2:  #selects the third listed image on the page
        img_src=x['src']
        print(img_src)
        break
        
image_l=requests.get('https:'+img_src)
#print(image_l.content)  #to display contents of image's binary file

f=open("Mynewimage.jpg", 'wb')
f.write(image_l.content)
f.close()

#This program saves the image from a single webpage in the folder where your python file exists 
