#include <Arduino.h>
#include <Camera.h>
#include <opencv.hpp>
//#include <DisplayApp.h>
#include <RPR-0521RS.h>
#include <Wire.h>
#include "AE_SHT31.h"

using namespace cv;
#define IMAGE_HW 320
#define IMAGE_VW 240
static Camera camera(320, 240);
//static DisplayApp display_app;
char rxbuf[128];
int img_count=0; 
int human=0;

const int VDDA =2;
bool cam_state=false;
unsigned long time_val=0;
unsigned long beforetime=0;
static int before_human=0;
int IRhuman=0;
const int Sence=6;
RPR0521RS rpr0521rs;
AE_SHT31 SHT31 = AE_SHT31(0x45);

void setup() {
  Serial4.begin(9600);
  Serial.begin(115200);
  pinMode(VDDA,OUTPUT);
  pinMode(Sence,INPUT);
  camera.begin();
  byte rc;
  rc = rpr0521rs.init();
  Wire.begin();
  Serial.println("SHT31 Test!!");
  SHT31.SoftReset();
  SHT31.Heater(0);
}

void serial(){
  int i=0;

  digitalWrite(VDDA,LOW);
  bool PCserial_state=false;
  bool Lazserial_state=false;
  
  while(Serial.available()){
    rxbuf[i]=Serial.read();
    i++;
    PCserial_state=true;
    digitalWrite(VDDA,HIGH);
    delay(10);
  }
  
  while(Serial4.available()){
    rxbuf[i]=Serial4.read();
    i++;
    Lazserial_state=true;
    digitalWrite(VDDA,HIGH);
    delay(10);
    if(rxbuf[0]=='S'||rxbuf[0]==' '){
        Lazserial_state=false;
    }
    else{
    }
  }
  
  if(PCserial_state){
    //rxbuf[0]がZの時のGR-LYCHEE処理の命令分岐
    if(rxbuf[0]=='Z'){
      if(rxbuf[1]=='A'){
        cam_state=true;
      }
      else{
        cam_state=false;
      }
    } 
    //それ以外はパイプ
    else{
      for(int j=0;j<i;j++){
        //Serial.print(rxbuf[j]);
        Serial4.print(rxbuf[j]);
      }
      //Serial.println("");
    }
  }
  
  if(Lazserial_state){
    for(int j=0;j<i;j++){
      Serial.print(rxbuf[j]); 
    }
    Serial.println("");
  }
  
  
  //get_homedata
  time_val=millis()-beforetime;
  if(time_val>10000){
    if(cam_state==true){
      if(img_count>100){
        human=1; 
      }
      else{
        human=0;
      }
      Serial.print("#");
      Serial.println(human);
    }
    byte rc;
    unsigned short ps_val;
    float als_val;
    SHT31.GetTempHum();
    Serial.print("$");
    Serial.print(SHT31.Temperature());
    Serial.print("℃");
    Serial.print(SHT31.Humidity());
    Serial.print("%");
    rc = rpr0521rs.get_psalsval(&ps_val, &als_val);
    if (rc == 0) {
      if (als_val != RPR0521RS_ERROR) {
        Serial.print(als_val);
      Serial.println("lx");
      }
    }  
    IRhuman=digitalRead(Sence);
    if(before_human==1&&IRhuman==1){
      Serial.println("&1");
    }
    else{
      Serial.println("&0");
    }
    before_human=IRhuman;
    beforetime=millis();
  }
  for(i=0;i<128;i++){
    rxbuf[i]=0;
  }
}

void loop() {
    Mat img_raw(IMAGE_VW, IMAGE_HW, CV_8UC2, camera.getImageAdr());
    Mat src, diff, srcFloat, dstFloat, diffFloat,thresFloat;
    dstFloat.create(IMAGE_VW, IMAGE_HW, CV_32FC1);
    dstFloat.setTo(0.0);
    while(true){
      cvtColor(img_raw, src, COLOR_YUV2GRAY_YUYV); //covert from YUV to GRAY
 
      src.convertTo(srcFloat, CV_32FC1, 1 / 255.0);
      addWeighted(srcFloat, 0.01, dstFloat, 0.99, 0, dstFloat, -1);
      absdiff(srcFloat, dstFloat, diffFloat);
      diffFloat.convertTo(diff, CV_8UC1, 255.0);
      threshold(diff,diff, 25, 255, THRESH_BINARY);
      img_count=countNonZero(diff);
      //display_app.SendJpeg(camera.getJpegAdr(), (int)camera.createJpeg());
      //delay(25);
      serial();
    }
}
