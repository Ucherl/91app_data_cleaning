import csv
import pickle

file=open('Member.csv',newline='', encoding='utf-8')

Member={}
for row in csv.reader(file):
    if row[0] not in Member:
        people=row[0]
        Member[people]={}
        Member[people]['MemberId']=row[0]
        Member[people]['RegisterDateTime']=row[4]
        Member[people]['MinOrderDate']=row[5]
        Member[people]['OpenCardPresent']=row[6]
        Member[people]['LastBirthdayPresentYear']=row[7]
        
filename ='Member.p'
fread = open(filename, 'wb')
pickle.dump(Member, fread)
fread.close()
