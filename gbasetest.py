# -*- coding: utf-8 -*-
import MySQLdb,time,datetime,uuid
i=10
ch=('1','2')
chn=('ff','fff')
t3=datetime.timedelta(minutes=3)
t=datetime.datetime.now()

conn=MySQLdb.connect(host='192.168.10.81',user='admin',passwd='luxiaobin',db='hansci_mam',port=5258,charset='utf8')
cur=conn.cursor()
while  i<=100:
    for j,k in zip(ch,chn):        
        t2=datetime.timedelta(minutes=i)
        startt=(t+t2).strftime('%Y-%m-%d %H:%M:%S')
        endt=(t+t2+t3).strftime('%Y-%m-%d %H:%M:%S')
        for l in range(4):
            id=uuid.uuid4()
            cur.execute("insert into T_CLIP_TASK values(%s,%s,%s,%s,%s,%s,%s,'',0,0,0,'','IP',1)",(id,k,j,3,startt,endt,t))
            #INSERT INTO `T_CLIP_CLIPINFO` VALUES ('34aa0645-17a0-4e43-9949-b66566feda3b', '34aa0645-17a0-4e43-9949-b66566feda3b', 'fffff', '', '收录', '2013-12-18 16:13:00', '2013-12-18 16:14:17', '', '00:00:00:00', '00:00:48:09', '00:00:48:10', '00:00:00:00', '00:00:00:00', '00:00:00:00', '', '2', '1', '', '2', '2013-12-18 16:14:17', null, '2013-12-18 16:14:17', '0', '0', '0', '');
    i+=10
conn.commit()
cur.close()
conn.close()
print 'over'