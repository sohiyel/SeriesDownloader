from bs4 import BeautifulSoup, SoupStrainer
import requests

#Paste the url of the page containing the urls of the series that you want to download between quotaions
url = ""

page = requests.get(url)    
data = page.text
soup = BeautifulSoup(data)


links = []


for link in soup.find_all('a'):
    #If the file format of the videoes were somthing else, change the mkv to your desired type
    if "mkv" in link.get('href'):
        links.append(url+str(link.get('href')))

links = set(links)

# You can change the name of the output file
a = open("download_links.txt","w")
for i in links:
    print(i)
    a.writelines(i+"\n")