import urllib
import urllib.request
from bs4 import BeautifulSoup
import time

class AppURLopener(urllib.request.FancyURLopener):
	version = "Mozilla/5.0"

def substring_after(s, delim):
    return s.partition(delim)[2]
opener = AppURLopener()
f= open("results.txt","w+")
qstr=input('Please input the keywords for searching via google scholar:') 
count=1
sta=0
while (sta<=500):
	data={}
	data['hl']='en'
	data['q']=qstr
	data['start']=sta
	url_values=urllib.parse.urlencode(data)
	url="https://scholar.google.com.tw/scholar?"
	full_url=url+url_values
	print ("getting results from...."+full_url) 
	data=opener.open(full_url).read()  
	soup = BeautifulSoup(data, 'html.parser')
	items = soup.select('h3.gs_rt > a')
	for i in items:
		f.write(str(count)+"\n")
		b_text=bytes(i.text,'cp950','ignore') 
		f.write("Title: "+str(b_text,'cp950','ignore')+"\n")
		f.write("URL: "+i.get('href')+"\n\n")
		count=count+1
	sta=sta+10
	num=1
	for num in range(1,10):
		time.sleep(2)
		print(".")
		num=num+1
	ynprompt=input('Do youu want to get the results from the Next page?[y/n]')
	if (ynprompt=='y'):
		continue
	else:
		break
f.close()
exit()

