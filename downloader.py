import argparse

parser = argparse.ArgumentParser('Find links')


parser.add_argument('--username', dest=r'username', help='input username to login', type=str, default=0)
parser.add_argument('--password', dest=r'password', help='input password', type=str, default=0)

args = parser.parse_args()

#Incase if the site needs to authenticate
username = args.username
password = args.password




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
