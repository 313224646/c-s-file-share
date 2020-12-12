import os
import json
from file2md5 import get_md5_small
import client

newMd5 = {}
oldMd5 = {}

client.connect(('192.168.89.129', 22000))

def getNewMd5(filePath, md5 = {}):
    fullpath = os.getcwd() + '\\' + filePath
    files = os.listdir(fullpath)
    for item in files:
        if item.find('.') == 1:
            md5[filePath + '\\' + item] = get_md5_small(fullpath + '\\' + item)
        else: 
            md5 = getNewMd5(filePath + '\\' + item, md5)
    return md5

with open('md5.json', 'r') as f:
    oldMd5 = json.load(f)

newMd5 = getNewMd5('share')

for key in newMd5:
    if key in oldMd5 and newMd5[key] == oldMd5[key]:
        continue
    else:
        client.sendFile(key)

with open('md5.json', 'w') as f:
    json.dump(newMd5, f)
