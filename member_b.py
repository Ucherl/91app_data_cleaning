import pickle
import string
from datetime import datetime

def str_to_date(input):
    temp=input.split()[0]
    return datetime.strptime(temp,'%Y-%m-%d')

def cal_seniority(input):
    temp=str_to_date(input)
    senior=datetime(2018,5,16)-temp
    return senior.days

filename1='./MemberNew.p'
f1=open(filename1,'rb')
member=pickle.load(f1)

filename2='./AddToWishNew.p'
f2=open(filename2,'rb')
addtowish=pickle.load(f2)

Member_B={}

for row in member:
    ID=member[row]['MemberId']
    Member_B[ID]={}
    Member_B[ID]['MemberId']=member[row]['MemberId']
    Member_B[ID]['RegisterDate']=str_to_date(member[row]['RegisterDateTime'])
    Member_B[ID]['Seniority']=cal_seniority(member[row]['RegisterDateTime'])

for row in member:
    if row in addtowish:
        ID=member[row]['MemberId']
        Member_B[ID]['WishCount']=addtowish[row]['count']
        Member_B[ID]['WishInterval']=addtowish[row]['interval']
    else:
        ID=member[row]['MemberId']
        Member_B[ID]['WishCount']=0
        Member_B[ID]['WishInterval']=0

filename ='Member_B.p'
fread = open(filename, 'wb')
pickle.dump(Member_B, fread)
fread.close()    


#result:{'MemberId': '1587633', 'RegisterDate': datetime.datetime(2016, 8, 5, 0, 0), 'Seniority': 649, 'WishCount': 0, 'WishInterval': 0}
