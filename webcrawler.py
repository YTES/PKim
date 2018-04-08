import urllib
import urllib.request
from bs4 import BeautifulSoup

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"
def substring_after(s, delim):
    return s.partition(delim)[2]
opener = AppURLopener()
f= open("wcrawler_r.txt","w+")
 
data={}
data['q']=input('Please input the keywords for searching via google:')
url_values=urllib.parse.urlencode(data)
url="https://www.google.com/search?"
full_url=url+url_values
print ("getting results from...."+full_url)
 
data=opener.open(full_url).read()  
soup = BeautifulSoup(data, 'html.parser')
items = soup.select('h3.r > a')

for i in items:
    b_text=bytes(i.text,'cp950','ignore') 
    f.write("Title: "+str(b_text,'cp950','ignore')+"\n")
    f.write("URL: "+substring_after(i.get('href'),'/url?q=')+"\n\n")

f.close()
exit()

