import json
import os
data = []

with open('./programs/links.json') as f:
    data = json.load(f)

links = []
for entry in data:
    for link in entry["files"]:
        if link not in links:
            links.append(link)

for link in links:
    #os.system('wget ' + link) #uncomment to toggle download, 