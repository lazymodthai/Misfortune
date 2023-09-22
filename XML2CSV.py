from bs4 import BeautifulSoup
import csv
import time

start = time.time()
count = 0
allitems = []
outputfile = "out"

# Read XML
filename = "old.xml"
with open(filename, encoding='utf-8') as raw_resuls:
    results = BeautifulSoup(raw_resuls, 'xml')
checkItem = []
fl = ""
for txt in results.find_all("translationText"):
    print(txt.data.data_6['value'])
    if fl == txt.data.data_6['value']:
        continue
    else:
        item_en = txt.data.data_6['value']
        item_rus = txt.data.data_0['value']
        allitems.append([item_en,item_rus, ""])
        fl = item_en


with open(outputfile+'.csv', 'w', encoding='utf8', newline='') as f:
    write = csv.writer(f)
    write.writerow(["EN", "RUS", "TH"])
    write.writerows(allitems)
