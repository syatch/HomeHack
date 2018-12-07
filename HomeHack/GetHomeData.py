#Copyright (c) Takashi Ito 2018
#Twitter: @syatchIT
#github: https://github.com/syatch
# coding: UTF-8
# arduinoからシリアル通信受信して温度をモニター
import sys
import os
import serial
# importはカレントディレクトリもまわるので，このスクリプト名をserial.pyにすると動かない！


def main(args):
    ser = serial.Serial('/dev/ttyACM0',115200)
    ArduinoState = False
    GRstate = False
    while True:
        line = ser.readline()
        line = line.replace(b'\n',b'')
        line = line.replace(b'\r',b'')
        line=line.decode(errors='ignore')
        #print(line)
        #line2 = line2.replace('|','\n')
        #ps(line2)
        #data is from Arduino and is data of temp and lux
        if line[0:1] is '$':
            wf = open('./home_data/data.txt', 'w')
            wf.write(line[1:13])
            print(line[1:13])
            wf.close
        #data is from Arduino and is data of human
        elif line[0:1] is '#':
            if line[1:2] is '0':
                ArduinoState = False
                print(line)
            if line[1:2] is '1':
                ArduinoState = True
                print(line)
        elif line[0:1] is '&':
            if line[1:2] is '0':
                GRstate = False
                print(line)
            if line[1:2] is '1':
                GRstate = True
                print(line)
        if ArduinoState == True and GRstate == True:
            wf = open('./home_data/human.txt', 'w')
            wf.write('1')
            print('1')
            wf.close
        else:
            wf = open('./home_data/human.txt', 'w')
            wf.write('0')
            print('0')
            wf.close
    ser.close()

#def ps(output):
#    sys.stdout.write(str(output))
#    sys.stdout.flush()

if __name__ == '__main__':
    main(sys.argv)
