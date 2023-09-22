from fileinput import filename
import json
import csv
allitems = []
filename = 'NAT_SpeechManager-resources.assets-4009'  # ชื่อไฟล์
with open(filename+'.json', encoding='utf8') as f:
    data = json.load(f)
    for i in data['lines']:
        i_id = i['lineID']
        i_key = i['scene']
        i_eng = i['text']
        i_rus = i['translationText'][0]
        print(i_key,i_eng)
#         print(k,i)    
        allitems.append([i_id,i_key,i_eng,i_rus])
with open(filename+'.csv', 'w', encoding='utf8', newline='') as f:
    write = csv.writer(f,delimiter=';')
    write.writerow(["ID","scene", "EN", "RUS","TH"])
    write.writerows(allitems)
