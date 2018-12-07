#read Web camera and find start and end JPEG and copy JPEG
import sys
import cv2
import datetime
import subprocess
import time

args = sys.argv


#写真
if args[1] is '0':
    now = datetime.datetime.now()
    path1='./picture/'
    path2="{0:%Y-%m-%d_%H:%M:%S}".format(now)
    path3='.jpg'
    path=path1+path2+path3

    cap=cv2.VideoCapture(0)
    ret,frame=cap.read()
    cv2.imwrite(path,frame)
    cap.release()
    
    wf=open("./home_data/picture.txt","w")
    wf.write(path)
    wf.close

#動画
elif args[1] is '1':
    #rec_data_from_GR
    time1=time.time()
    time2=0
    time_long=20
    count=0
    cap=cv2.VideoCapture(0)
    while True:
        path1='./rawImage/read'
        path2= str(count)
        path3='.jpg'
        path=path1+path2+path3
        ret,frame=cap.read()
        cv2.imwrite(path,frame)
        time2=time.time()
        if time2-time1>time_long:
            break
        count += 1
    cap.release()
    #動画にする
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    now = datetime.datetime.now()
    savepath1='./video/'
    savepath2="{0:%Y-%m-%d_%H:%M:%S}".format(now)
    savepath3='.mp4'
    savepath=savepath1+savepath2+savepath3
    video = cv2.VideoWriter(savepath, fourcc, count/time_long, (640, 480))
    print(str(count))
    for i in range(count):
        path1='./rawImage/read'
        path2= str(i)
        path3='.jpg'
        path=path1+path2+path3
        img = cv2.imread(path.format(i))
        video.write(img)
    video.release()
    subprocess.run(['rm -r -f ./rawImage/*'],shell=True)
#侵入者検知時
elif args[1] is '2':
    now = datetime.datetime.now()
    path1='./picture/'
    path2="{0:%Y-%m-%d_%H:%M:%S}".format(now)
    path3='.jpg'
    path=path1+path2+path3

    cap=cv2.VideoCapture(0)
    ret,frame=cap.read()
    cv2.imwrite(path,frame)
    cap.release()
    
    wf=open("./home_data/warn_pic.txt","w")
    wf.write(path)
    wf.close
    wf = open('./home_data/warn.txt', 'w')
    wf.write('1')
    wf.close
    
    #rec_data_from_GR
    time1=time.time()
    time2=0
    time_long=20
    count=0
    cap=cv2.VideoCapture(0)
    while True:
        path1='./rawImage/read'
        path2= str(count)
        path3='.jpg'
        path=path1+path2+path3
        ret,frame=cap.read()
        cv2.imwrite(path,frame)
        time2=time.time()
        if time2-time1>time_long:
            break
        count += 1
    cap.release()
    #動画にする
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    now = datetime.datetime.now()
    savepath1='./video/'
    savepath2="{0:%Y-%m-%d_%H:%M:%S}".format(now)
    savepath3='.mp4'
    savepath=savepath1+savepath2+savepath3
    video = cv2.VideoWriter(savepath, fourcc, count/time_long, (640, 480))
    print(str(count))
    for i in range(count):
        path1='./rawImage/read'
        path2= str(i)
        path3='.jpg'
        path=path1+path2+path3
        img = cv2.imread(path.format(i))
        video.write(img)
    video.release()
    subprocess.run(['rm -r -f ./rawImage/*'],shell=True)
    wf=open("./home_data/warn_vid.txt","w")
    wf.write(savepath)
    wf.close
else:
    pass
