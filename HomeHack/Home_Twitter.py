# -*- coding: utf-8 -*-
import json
import config
import datetime
import time 
import serial
import subprocess
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)
read_url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
send_url = "https://api.twitter.com/1.1/statuses/update.json"
upload_url = "https://upload.twitter.com/1.1/media/upload.json"

ser = serial.Serial('/dev/ttyACM0',115200)

Twitter_status=False
before_time=datetime.datetime.now()
now=datetime.datetime.now()
pre_time='first'
first=True
while first is True:
    params ={'count' : 1} 
    res = twitter.get(read_url, params = params)
    if res.status_code == 200: 
        timelines = json.loads(res.text) 
        for line in timelines: 
            print(line['user']['name']+'::'+line['text'])
            print(line['created_at'])
            print('*******************************************')
            pre_time=line['created_at']
            first = False
    else: 
        print("Failed: %d" % res.status_code)
    

while True:
    now= datetime.datetime.now()
    waittime=(now-before_time).total_seconds()
    if waittime>=70:
        before_time=datetime.datetime.now()
        params ={'count' : 1} 
        res = twitter.get(read_url, params = params)
        if res.status_code == 200: 
            timelines = json.loads(res.text) 
            for line in timelines: 
                print(line['user']['name']+'::'+line['text'])
                print(line['created_at'])
                print('*******************************************')
                if line['created_at'] == pre_time:
                    print('through')
                elif line['user']['name'] == 'syatch' in line['text'] and '@Akari_syatchIT' in line['text']:
                    print('get command:')
                    print( line['text'])
                    if '電源タップ' in  line['text']:
                        if '１' in  line['text'] or '1' in  line['text']:
                            if 'つけて' in  line['text']:
                                ser.write(b"AAB")
                            elif '消して' in  line['text']:
                                ser.write(b"AAA")
                        elif '２' in  line['text'] or '2' in  line['text']:
                            if 'つけて' in  line['text']:
                                ser.write(b"ABB")
                            elif '消して' in  line['text']:
                                ser.write(b"ABA")
                        elif '３' in  line['text'] or '3' in  line['text']:
                            if 'つけて' in  line['text']:
                                ser.write(b"ACB")
                            elif '消して' in  line['text']:
                                ser.write(b"ACA")
                        params = {"status": "{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\n電源タップを操作したよ"}
                        req = twitter.post(send_url,params = params)
            
                    
                    elif 'テレビ' in  line['text']:
                        if 'つけて' in  line['text'] or '消して' in  line['text']:
                            ser.write(b"BAA")
                        elif '１' in  line['text'] or '1' in  line['text']:
                            ser.write(b"BAB")
                        elif '２' in  line['text'] or '2' in  line['text']:
                            ser.write(b"BAC")
                        elif '３' in  line['text'] or '3' in  line['text']:
                            ser.write(b"BAD")
                        elif '４' in  line['text'] or '4' in  line['text']:
                            ser.write(b"BAE")
                        elif '５' in  line['text'] or '5' in  line['text']:
                            ser.write(b"BAF")
                        elif '６' in  line['text'] or '6' in  line['text']:
                            ser.write(b"BAG")
                        elif '７' in  line['text'] or '7' in  line['text']:
                            ser.write(b"BAH")
                        elif '８' in  line['text'] or '8' in  line['text']:
                            ser.write(b"BAI")
                        elif '９' in  line['text'] or '9' in  line['text']:
                            ser.write(b"BAJ")
                        elif '１０' in  line['text'] or '10' in  line['text']:
                            ser.write(b"BAK")
                        elif '１１' in  line['text'] or '11' in  line['text']:
                            ser.write(b"BAL")
                        elif '１２' in  line['text'] or '12' in  line['text']:
                            ser.write(b"BAM")
                        elif '音量' in  line['text']:
                            if '上げて' in  line['text']:
                                ser.write(b"BAN")
                            elif '下げて' in  line['text']:
                                ser.write(b"BAO")
                        elif '入力切替' in  line['text']:
                            ser.write(b"BAP")
                    
                        params = {"status": "{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\nテレビを操作したよ"}
                        req = twitter.post(send_url,params = params)
                        
                    elif 'チャンネル' in  line['text'] or 'チャン' in  line['text']:
                        if '１' in  line['text'] or '1' in  line['text']:
                            ser.write(b"BAB")
                        elif '２' in  line['text'] or '2' in  line['text']:
                            ser.write(b"BAC")
                        elif '３' in  line['text'] or '3' in  line['text']:
                            ser.write(b"BAD")
                        elif '４' in  line['text'] or '4' in  line['text']:
                            ser.write(b"BAE")
                        elif '５' in  line['text'] or '5' in  line['text']:
                            ser.write(b"BAF")
                        elif '６' in  line['text'] or '6' in  line['text']:
                            ser.write(b"BAG")
                        elif '７' in  line['text'] or '7' in  line['text']:
                            ser.write(b"BAH")
                        elif '８' in  line['text'] or '8' in  line['text']:
                            ser.write(b"BAI")
                        elif '９' in  line['text'] or '9' in  line['text']:
                            ser.write(b"BAJ")
                        elif '１０' in  line['text'] or '10' in  line['text']:
                            ser.write(b"BAK")
                        elif '１１' in  line['text'] or '11' in  line['text']:
                            ser.write(b"BAL")
                        elif '１２' in  line['text'] or '12' in  line['text']:
                            ser.write(b"BAM")
                        params = {"status": "{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\nテレビを操作したよ"}
                        req = twitter.post(send_url,params = params)
                    
                           
                    elif '扇風機' in  line['text']:
                        if 'タイマー' not in  line['text'] and ( 'つけて' in  line['text'] or '消して' in  line['text'] ):
                            ser.write(b"BBA")
                        elif 'リズム' in  line['text']:
                            ser.write(b"BBB")
                        elif '風量' in  line['text']:
                            if '上げて' in  line['text']:
                                ser.write(b"BBC")
                            elif '下げて' in  line['text']:
                                ser.write(b"BBD")
                        elif '上下' in  line['text']:
                            ser.write(b"BBE")
                        elif '左右' in  line['text']:
                            ser.write(b"BBF")
                        elif 'タイマ−' in  line['text']:
                            if 'つけて' in  line['text']:
                                ser.write(b"BBG")
                            elif '消して' in  line['text']:
                                ser.write(b"BBH")
                        params = {"status": "{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\n扇風機を操作したよ"}
                        req = twitter.post(send_url,params = params)
                    
                    elif '風量' in  line['text']:
                        if '上げて' in  line['text']:
                            ser.write(b"BBC")
                        elif '下げて' in  line['text']:
                            ser.write(b"BBD")
                        params = {"status": "{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\n扇風機を操作したよ"}
                        req = twitter.post(send_url,params = params)
                        
                 
                    elif '電気' in  line['text']:
                        if 'つけて' in  line['text']:
                            ser.write(b"BCA")
                            params = {"status": "{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\n電気をつけたよ"}
                            req = twitter.post(send_url,params = params)
                        elif '消して' in  line['text']:
                            ser.write(b"BCB")
                            params = {"status": "{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\n電気を消したよ"}
                            req = twitter.post(send_url,params = params)
                        elif '明るく' in  line['text']:
                            ser.write(b"BCC")
                            params = {"status": "{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\n電気を明るくしたよ"}
                            req = twitter.post(send_url,params = params)
                        elif '暗く' in  line['text']:
                            ser.write(b"BCD")
                            params = {"status": "{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\n電気を暗くしたよ"}
                            req = twitter.post(send_url,params = params)
                        elif '白く' in  line['text']:
                            ser.write(b"BCE")
                            params = {"status": "{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\n電気を白くしたよ"}
                            req = twitter.post(send_url,params = params)
                        elif '暖かく' in  line['text']:
                            ser.write(b"BCF")
                            params = {"status": "{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\n電気を暖かくしたよ"}
                            req = twitter.post(send_url,params = params)
                        elif '常夜灯' in  line['text']:
                            ser.write(b"BCG")
                            params = {"status": "{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\n電気を常夜灯にしたよ"}
                            req = twitter.post(send_url,params = params)
                        elif '全灯' in  line['text']:
                            ser.write(b"BCH")
                            params = {"status": "{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\n電気を全灯にしたよ"}
                            req = twitter.post(send_url,params = params)
                    
                   
                    elif 'エアコン' in  line['text']:
                        if '暖房' in  line['text']:
                            ser.write(b"BDA")
                            params = {"status": "{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\nエアコン、暖房をつけたよ"}
                            req = twitter.post(send_url,params = params)
                        elif '冷房' in  line['text']:
                            ser.write(b"BDB")
                            params = {"status": "{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\nエアコン、冷房をつけたよ"}
                            req = twitter.post(send_url,params = params)
                        elif '自動' in  line['text']:
                            ser.write(b"BDC")
                            params = {"status": "{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\nエアコン、自動でつけたよ"}
                            req = twitter.post(send_url,params = params)
                        elif '消して' in  line['text']:
                            ser.write(b"BDD")
                            params = {"status": "{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\nエアコン消したよ"}
                            req = twitter.post(send_url,params = params)
                    
                    elif 'ポルター' in  line['text']:
                        if '終わり' in  line['text']:
                            wf = open('./home_data/polter.txt', 'w')
                            wf.write('0')
                            wf.clos
                            params = {"status": "{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\nいたずらしゅーりょー"}
                            req = twitter.post(send_url,params = params)
                        else:
                            wf = open('./home_data/polter.txt', 'w')
                            wf.write('1')
                            wf.close
                            params = {"status": "{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\nいたずらするぞー！"}
                            req = twitter.post(send_url,params = params)
                    elif '写真' in  line['text']:
                        
                        subprocess.run(["python","GR_camera.py","0"])
                        
                        
                        rf = open('./home_data/picture.txt', 'r')
                        path=rf.readline()
                        path = path.replace('\n','')
                        path = path.replace('\r','')
                        rf.close
                        params={"media":open(path,'rb')}
                        pic = twitter.post(upload_url,files=params)
                        if pic.status_code != 200:
                            print(pic.status_code)
                        else:
                            media_id = json.loads(pic.text)['media_id']
                            params = {"status": "{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\n写真を撮りました！", "media_ids" : [media_id]}
                            req = twitter.post(send_url,params = params)
                        
                    elif '動画' in  line['text']:
                        
                        subprocess.run(["python","GR_camera.py","1"])
                        
                        rf = open('./home_data/picture.txt', 'r')
                        path=rf.readline()
                        rf.close
                        params = {"status": "{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\n動画を撮りました！"}
                        req = twitter.post(send_url,params = params)
                
        	    
                    elif '情報' in  line['text']:
                        rf = open('./home_data/data.txt', 'r')
                        data=rf.readline()
                        print(data)
                        rf.close
                        params = {"status": "@syatchIT\n現在("+"{0:%Y年%m月%d日%H:%M:%S}".format(now)+")、\n室温"+data[0:6]+"\n気圧"+data[6:16]+"\n照度"+data[16:]+"\nです！"}
                        req = twitter.post(send_url,params = params)
                        
                else:
                    print('through')
                pre_time=line['created_at']
        else:
            print("Failed: %d" % res.status_code)
    else:
        pass    
        

    rf = open('./home_data/warn.txt', 'r')
    warn=rf.readline()
    rf.close
        	
    if warn[0:1] is '1':
        
        rf = open('./home_data/warn_pic.txt', 'r')
        warn=rf.readline()
        warn = warn.replace('\n','')
        warn = warn.replace('\r','')
        rf.close
        params={"media":open(warn,'rb')}
        pic = twitter.post(upload_url,files=params)
        if pic.status_code != 200:
            print(pic.status_code)
        else:
            media_id = json.loads(pic.text)['media_id']
            params = {"status": "@syatchIT\n"+"{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\n"+"侵入者です！(((( ;ﾟдﾟ)))ｱﾜﾜﾜﾜ", "media_ids" : [media_id]}
            req = twitter.post(send_url,params = params)
        
        print("warning")
        """
        params = {"status": "@syatchIT\n"+"{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\n"+"侵入者です！(((( ;ﾟдﾟ)))ｱﾜﾜﾜﾜ"}
        req = twitter.post(send_url,params = params)

        時間がかかるので無効化中
        #動画のパスを取得
        rf = open('./home_data/warn_vid.txt', 'r')
        warn=rf.readline()
        warn = warn.replace('\n','')
        warn = warn.replace('\r','')
        rf.close
        params={"media":open(warn,'rb')}
        pic = twitter.post(upload_url,files=params)
        time.sleep(5)
        if pic.status_code != 200:
            print(pic.status_code)
        else:
            media_id = json.loads(pic.text)['media_id']
            #ツイート（動画付き）
            params = {"status": "@syatchIT\n"+"{0:%Y年%m月%d日%H:%M:%S}".format(now)+"\n"+"動画です！(((( ;ﾟдﾟ)))ｱﾜﾜﾜﾜ", "media_ids" : [media_id]}
            req = twitter.post(send_url,params = params)
        """        	
        wf = open('./home_data/warn.txt', 'w')
        wf.write('')
        wf.close
    else:
        pass
    
    time.sleep(0.5)
ser.close()
