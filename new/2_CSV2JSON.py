from fileinput import filename
import json
import csv
filename = 'NAT_SpeechManager-resources.assets-4009'  # ต้นฉบับ
translated = 'translated'  # CSV ที่แปลแล้ว
outputfile = 'NEW_'+filename  # JSON ขาออก
with open(translated+'.csv', encoding='utf-8') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    csv_dict = {}
    for row in csv_data:
        if row[0] not in csv_dict:
            csv_dict[row[0]] = {}
        csv_dict[row[0]][row[1]] = row[3]
# with open("Dict.json", "w", encoding='utf8') as outfile:
#     json_object = json.dumps(csv_dict, indent=2)
#     outfile.write(json_object)
      
with open(filename+'.json', encoding='utf8') as f:
    data = json.load(f)
    for i in data['lines']:
        i_id = str(i['lineID'])
        i_en = i['text']
        # print(i_id,i_en)
        try:
            if i_id in csv_dict and csv_dict[i_id][i_en] != '':
                i['translationText'][0] = csv_dict[i_id][i_en]
            else:
                i['translationText'][0] = csv_dict[i_id][i_en]  
        except:
            continue
    with open(outputfile+'.json', "w", encoding='utf-8') as k:
        k.write(json.dumps(data, indent=2, ensure_ascii=False))
        k.close()
