from bs4 import BeautifulSoup
import csv
import time

start = time.time()
count = 0
edited = 0
filename = "old.xml"  # ไฟล์เดิมเป็น XML
translatedfile = "out.csv"  # ไฟล์แปลแล้วเป็น CSV
outputfile = "NAT_SpeechManager.SpeechManager.xml"  # ไฟล์ที่จะทำเป็น Output

with open(filename, encoding='utf-8') as raw_resuls:
    results = BeautifulSoup(raw_resuls, 'xml')

for txt in results.find_all("translationText"):
    fl = False
    g = open(translatedfile, encoding='utf-8')
    csv_reader2 = csv.reader(g)
    for i in csv_reader2:
        if i[0] == txt.data.data_6['value'] and i[2] != "":
            txt.data.data_0['value'] = i[2]
            print(str(count)+'_'+txt.data.data_6['value']+": แก้ไขแล้ว")
            fl = True
            edited += 1
            count += 1
            break
    if fl != True:
        print(str(count)+'_'+txt.data.data_6['value']+": ข้าม")
        fl = False
        count += 1
with open(outputfile, "w", encoding='utf-8') as outfile:
    outfile.write(results.prettify())

end = time.time()
percentage = "{:.2f}".format(edited*100/count)
print('ทั้งหมด: '+str(edited)+'/'+str(count)+'('+percentage+'%)')
restime = end - start
if restime >= 60:
    restime = restime/60
    unit = ' นาที'
else:
    unit = ' วินาที'
totaltime = "{:.2f}".format(restime)
print('ใช้เวลาไป: ' + str(totaltime) + unit)
