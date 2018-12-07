import subprocess
import time

wf = open('./home_data/camera.txt', 'w')
wf.write('')
wf.close
camera_state = 0
while True:
    rf = open('./home_data/camera.txt', 'r')
    camera_state=rf.readline()
    rf.close
    #if command has come
    if camera_state[0:1] is not '':
        if camera_state[0:1] is '0':
            subprocess.run(["python","camera.py","0"])
            wf = open('./home_data/camera.txt', 'w')
            wf.write('')
            wf.close
        elif camera_state[0:1] is '1':
            subprocess.run(["python","camera.py","1"])
            wf = open('./home_data/camera.txt', 'w')
            wf.write('')
            wf.close
        elif camera_state[0:1] is '2':
            subprocess.run(["python","camera.py","2"])
            wf = open('./home_data/camera.txt', 'w')
            wf.write('')
            wf.close
    time.sleep(0.1)
