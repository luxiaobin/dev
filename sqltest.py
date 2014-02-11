# -*- coding: utf-8 -*-
import MySQLdb,time,datetime,uuid
i=2
ch=('ch1','ch2')
chn=('湖南','江苏')
t3=datetime.timedelta(minutes=2)
t=datetime.datetime.now()

conn=MySQLdb.connect(host='192.168.1.85',user='root',passwd='123456',db='hansci_mam',port=3306,charset='utf8')
cur=conn.cursor()
while  i<=2:
    for j,k in zip(ch,chn):
        id=uuid.uuid4()
        t2=datetime.timedelta(minutes=i)
        startt=(t+t2).strftime('%Y-%m-%d %H:%M:%S')
        endt=(t+t2+t3).strftime('%Y-%m-%d %H:%M:%S')
        cur.execute("insert into T_CLIP_TASK values(%s,%s,%s,%s,%s,%s,%s,'',0,0,0,'','IP',1)",(id,k,j,'CLIPTYPE_2',startt,endt,t))
        cur.execute("insert into T_TASK_RECDOUTTMPL_R values('TMPL_ID2',%s)",id)
    i+=2
conn.commit()
cur.close()
conn.close()
print 'over'