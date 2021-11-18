# import urllib2

#Incase if the site needs to authenticate
username = ''
password = ''

# #This should be the base url you wanted to access.
baseurl = ''


import requests
downloadFile = open("download_links.txt","r")
links = downloadFile.readlines()
for i in links:
    url = i[:-1]
    print("Downloading: "+url)
    resp = requests.get(url, auth=(username, password))
    while(not resp.ok):
        continue
    if resp.ok:
        fileName = url.split("/")[-1]
        print("Saving: "+fileName)
        file = open(fileName, "wb+") # write, binary, allow creation
        file.write(resp.content)
        file.close()
    else:
        print("Failed to get the file")
