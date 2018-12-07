# -*- coding: utf-8 -*-
#python3.6
import socket
import xml.etree.ElementTree as ET
import os
import subprocess
import time
import sys
#sys.path.append("/usr/local/lib/python3.6/dist-packages/serial")
import serial
#import _pyautogui_x11 as pgui
import pyautogui as pgui
import datetime
from signal import signal,SIGRTMIN
from enum import IntEnum


#soket通信の設定
host = "localhost"
port = 10500 #juliusのポート
#max_size = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

#マイコンに送るシリアルの設定
ser = serial.Serial('/dev/ttyACM0',115200)

try:
    data =""
    beforeword =""
    getword=""
    quickMode=False
    voice_status=False
    watch=False
    before_time = datetime.datetime.now()
    now_time = datetime.datetime.now()
    pre_watch = datetime.datetime.now()
    now_watch = datetime.datetime.now()
    #clock_p=subprocess.Popen("./clock")
    #home_p=subprocess.Popen(["python","./GetHomeData.py"])
    #displaydata_p=subprocess.Popen("./DataFromHome")
    while 1:
        #juliusからのデータを受信し終わったら
        if "</RECOGOUT>\n." in data: 
            #音声認識の結果をマスキング
            #print(data)
            data = data.split('</RECOGOUT>')[0]+"</RECOGOUT>"
            #print(data)
            root = ET.fromstring(data[data.find("<RECOGOUT>"):].replace("\n", ""))
            for whypo in root.findall("./SHYPO/WHYPO"):
                word = whypo.get("WORD")
                if word != "[s]" and word != "[/s]":
                    getword += word
            data = ""
            print(getword)
            
            #以下操作の条件分岐
            #”あかり”（キャラクター名）が認識結果に含まれているか、前回に”あかり”のみ（呼びかけ）認識しているか、クイックモードでないと反応しないようにする（誤爆を防ぐため）
            
            if u'あかり' in getword or beforeword == "あかり" or quickMode==True:
                print("Command has come")
                if beforeword=="あかり":
                    beforeword=""
                else:
                    pass
                #######電源タップ
                if u'でんげんたっぷ' in getword:
                    if u'いち' in getword:
                        if u'つけて' in getword:
                            ser.write(b"AAB")
                        elif u'けして' in getword:
                            ser.write(b"AAA")
                        else:
                            print("Tap 1:Unexpected command")
                            print(getword)
                    elif u'に' in getword:
                        if u'つけて' in getword:
                            ser.write(b"ABB")
                        elif u'けして' in getword:
                            ser.write(b"ABA")
                        else:
                            print("Tap 2:Unexpected command")
                            print(getword)
                    elif u'さん' in getword:
                        if u'つけて' in getword:
                            ser.write(b"ACB")
                        elif u'けして' in getword:
                            ser.write(b"ACA")
                        else:
                            print("Tap 3:Unexpected command")
                            print(getword)
                    else:
                        print("Tap:Unexpected command")
                        print(getword)
            
                #######テレビ
                elif u'てれび' in getword:
                    if u'つけて' in getword or u'けして' in getword:
                        ser.write(b"BAA")
                    elif u'いち' in getword:
                        ser.write(b"BAB")
                    elif u'に' in getword:
                        ser.write(b"BAC")
                    elif u'さん' in getword:
                        ser.write(b"BAD")
                    elif u'し' in getword:
                        ser.write(b"BAE")
                    elif u'ご' in getword:
                        ser.write(b"BAF")
                    elif u'ろく' in getword:
                        ser.write(b"BAG")
                    elif u'なな' in getword:
                        ser.write(b"BAH")
                    elif u'はち' in getword:
                        ser.write(b"BAI")
                    elif u'きゅう' in getword:
                        ser.write(b"BAJ")
                    elif u'じゅう' in getword:
                        ser.write(b"BAK")
                    elif u'じゅういち' in getword:
                        ser.write(b"BAL")
                    elif u'じゅうに' in getword:
                        ser.write(b"BAM")
                    elif u'おんりょう' in getword:
                        if u'あげて' in getword:
                            ser.write(b"BAN")
                        elif u'さげて' in getword:
                            ser.write(b"BAO")
                        else:
                            print("TV volume:Unexpected command")
                            print(getword)
                    elif u'にゅうりょくきりかえ' in getword:
                        ser.write(b"BAP")
                    else:
                        print("TV:Unexpected command")
                        print(getword)
                elif u'ちゃんねる' in getword or u'ちゃん' in getword:
                    if u'いち' in getword:
                        ser.write(b"BAB")
                    elif u'に' in getword:
                        ser.write(b"BAC")
                    elif u'さん' in getword:
                        ser.write(b"BAD")
                    elif u'し' in getword:
                        ser.write(b"BAE")
                    elif u'ご' in getword:
                        ser.write(b"BAF")
                    elif u'ろく' in getword:
                        ser.write(b"BAG")
                    elif u'なな' in getword:
                        ser.write(b"BAH")
                    elif u'はち' in getword:
                        ser.write(b"BAI")
                    elif u'きゅう' in getword:
                        ser.write(b"BAJ")
                    elif u'じゅう' in getword:
                        ser.write(b"BAK")
                    elif u'じゅういち' in getword:
                        ser.write(b"BAL")
                    elif u'じゅうに' in getword:
                        ser.write(b"BAM")
                    else:
                        print("TV channel:Unexpected command")
                        print(getword)
                    
                #######扇風機        
                elif u'せんぷうき' in getword:
                    if u'たいまー' not in getword and ( u'つけて' in getword or u'けして' in getword ):
                        ser.write(b"BBA")
                    elif u'りずむ' in getword:
                        ser.write(b"BBB")
                    elif u'ふうりょう' in getword:
                        if u'あげて' in getword:
                            ser.write(b"BBC")
                        elif u'さげて' in getword:
                            ser.write(b"BBD")
                        else:
                            print("Fan Fan strength:Unexpected command")
                            print(getword)
                    elif u'じょうげ' in getword:
                        ser.write(b"BBE")
                    elif u'さゆう' in getword:
                        ser.write(b"BBF")
                    elif u'たいまー' in getword:
                        if u'つけて' in getword:
                            ser.write(b"BBG")
                        elif u'けして' in getword:
                            ser.write(b"BBH")
                        else:  
                            print("FanTimer:Unexpected command")
                            print(getword)
                    else:
                        print("Fan:Unexpected command")
                        print(getword)
                    
                elif u'ふうりょう' in getword:
                    if u'あげて' in getword:
                        ser.write(b"BBC")
                    elif u'さげて' in getword:
                        ser.write(b"BBD")
                    else:
                        print("Fan strength:Unexpected command")
                        print(getword)
                        
                ########照明  
                elif u'でんき' in getword:
                    if u'つけて' in getword:
                        ser.write(b"BCA")
                    elif u'けして' in getword:
                        ser.write(b"BCB")
                    elif u'あかるく' in getword:
                        ser.write(b"BCC")
                    elif u'くらく' in getword:
                        ser.write(b"BCD")
                    elif u'しろく' in getword:
                        ser.write(b"BCE")
                    elif u'あたたかく' in getword:
                        ser.write(b"BCF")
                    elif u'じょうやとう' in getword:
                        ser.write(b"BCG")
                    elif u'ぜんとう' in getword:
                        ser.write(b"BCH")
                    else:
                        print("Light:Unexpected command")
                        print(getword)
                    
                #######エアコン    
                elif u'えあこん' in getword:
                    if u'だんぼう' in getword:
                        ser.write(b"BDA")
                    elif u'れいぼう' in getword:
                        ser.write(b"BDB")
                    elif u'じどう' in getword:
                        ser.write(b"BDC")
                    elif u'けして' in getword:
                        ser.write(b"BDD")
                    else:
                        print("Air Conditioner:Unexpected command")
                        print(getword)
                #生活
                elif u'ただいま' in getword:
                    ser.write(b"BCA")
                    watch=False
                    subprocess.Popen(["aplay","-q","./voice/back.wav"])
                elif u'いってきます' in getword or u'いってくる' in getword:
                    ser.write(b"BCB")
                    watch=True
                    watch_count=0
                    subprocess.Popen(["aplay","-q","./voice/niceday.wav"])
                elif u'おはよう' in getword or u'おっは' in getword:
                    ser.write(b"BCA")
                    subprocess.Popen(["aplay","-q","./voice/morning.wav"])
                elif u'おやす' in getword:
                    ser.write(b"BCB")
                    subprocess.Popen(["aplay","-q","./voice/night.wav"])
                        
                #######天気・ニュースの表示
                elif u'てんき' in getword:
                    subprocess.Popen(["./get_data/get_data","6"])
                elif u'にゅーす' in getword:
                    if u'しゃかい' in getword:
                        subprocess.Popen(["./get_data/get_data","1"])
                    elif u'かがく' in getword or u'いりょう' in getword:
                        subprocess.Popen(["./get_data/get_data","2"])
                    elif u'せいじ' in getword:
                        subprocess.Popen(["./get_data/get_data","3"])
                    elif u'けいざい' in getword:
                        subprocess.Popen(["./get_data/get_data","4"])
                    elif u'こくさい' in getword:
                        subprocess.Popen(["./get_data/get_data","5"])
                    else:
                        subprocess.Popen(["./get_data/get_data","0"])
                        
               
                #######Ubuntu操作（PC）
                elif u'おんりょう' in getword:
                    if u'あげて'in getword:
                        pgui.press('volumeup')
                    elif u'さげて'in getword:
                        pgui.keyDown('VolumeUp')
                        pgui.keyUp('VolumeUp')
                elif u'とじて' in getword:
                    pgui.hotkey('alt','f4')


                #GR-LYCHEEのカメラ関係
                elif u'しゃしん' in getword:
                    if u'さいれんと' in getword:
                        wf = open('./home_data/camera.txt', 'w')
                        wf.write('0')
                        wf.close
                    else:
                        wf = open('./home_data/camera.txt', 'w')
                        wf.write('0')
                        wf.close
                        
                elif u'どうが' in getword:
                    if u'さいれんと' in getword:
                        wf = open('./home_data/camera.txt', 'w')
                        wf.write('1')
                        wf.close
                    else: 
                        wf = open('./home_data/camera.txt', 'w')
                        wf.write('1')
                        wf.close

                #クイックモードの鍵ワード
                elif u'くいっく' in getword:
                    if u'つけて' in getword:
                        quickMode=True
                        subprocess.Popen(["aplay","-q","./voice/quick_start.wav"])
                    elif u'けして' in getword:
                        quickMode=False
                        subprocess.Popen(["aplay","-q","./voice/quick_end.wav"])
                    else:
                        print("quickMode:Unexpected command")
                        print(getword)
                elif u'あかり' in getword:
                    before_time = datetime.datetime.now()
                    print("なんですか？")
                    if quickMode==True:
                        subprocess.Popen(["aplay","-q","./voice/what.wav"])
                    elif beforeword != "あかり" : 
                        subprocess.Popen(["aplay","-q","./voice/what.wav"])
                    beforeword="あかり"
                else:
                    print("Not registrated this command: ")
                    print(getword)
            else:
                pass   
            before_time = datetime.datetime.now()
        
        #juliusからのデータがあるとき
        else:
            response = client.recv(4096)
            data += response.decode() 

        #監視の条件分岐
        if watch==True:
            rf = open('./home_data/human.txt', 'r')
            human=rf.readline()
            rf.close
            now_watch = datetime.datetime.now()
            if human[0:1] is '1' and (now_watch-pre_watch).total_seconds()>=120:
                print("in")
                wf = open('./home_data/camera.txt', 'w')
                wf.write('2')
                wf.close
                #写真を撮り、
                #subprocess.Popen(["python","GR_camera.py","2"])
                pre_watch=now_watch
            else:
                pass
        else:
            pass

        now_time = datetime.datetime.now()

        if beforeword=="あかり" and (now_time-before_time).total_seconds()>10:
            beforeword = ""
            print("Return to wait")
        else:
            pass

        getword=""
    ser.close()
    client.close()
    
except KeyboardInterrupt:
    ser.close()
    client.close()
    ser.close()
    client.close()
