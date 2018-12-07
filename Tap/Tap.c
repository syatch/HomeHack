//Copyright (c) Takashi Ito 2018
//Twitter: @syatchIT
//github: https://github.com/syatch
#include "Tap_ide.h"		// Additional Header
#define SUBGHZ_CH	36
#define SUBGHZ_PANID	0xABCD
uint8_t rx_data[256];
uint32_t last_recv_time = 0;
SUBGHZ_STATUS rx;							// structure for getting rx status
#define BLUE_LED	26

static const unsigned char *aes_key = NULL;		// disable AES key

int LED[3]={12,10,7};
int Button[3]={13,11,9};
int LQ[3]={4,5,6};
bool state[3]={false,false,false};
int i;


//Read Button
bool Read(int pin,bool now){
  int btn;
  btn=digitalRead(pin);
  if(btn==1){
    while(btn==1){
      btn=digitalRead(pin);
      delay(10);
    }
    return !now;
  }
  else{
    return now;
  }
}
//LQ
void Switch(int pin,bool state){
  if(state==true){
    analogWrite(pin,255);
  }
  else{
    analogWrite(pin,0);
  }
}
//LED
void Light(int pin,bool state){
  if(state==true){ 
    digitalWrite(pin,HIGH);
  }
  else{
    digitalWrite(pin,LOW);
  }
}


void print_hex_func(uint8_t data)
{
	if(data == 0) Serial.print("00");
	else if(data < 16) {
		Serial.print("0");
		Serial.print_long(data,HEX);
	} else {
		Serial.print_long(data,HEX);
	}
}

void setup(void)
{
	SUBGHZ_MSG msg;
	uint8_t myAddr[8];

	Serial.begin(115200);
	
	msg = SubGHz.init();
	if(msg != SUBGHZ_OK)
	{
		SubGHz.msgOut(msg);
		while(1){ }
	}
	
	SubGHz.getMyAddr64(myAddr);
	Serial.print("myAddress = ");
	print_hex_func(myAddr[0]);
	print_hex_func(myAddr[1]);
	Serial.print(" ");
	print_hex_func(myAddr[2]);
	print_hex_func(myAddr[3]);
	Serial.print(" ");
	Serial.print(" ");
	print_hex_func(myAddr[4]);
	print_hex_func(myAddr[5]);
	Serial.print(" ");
	print_hex_func(myAddr[6]);
	print_hex_func(myAddr[7]);
	Serial.println("");


	SubGHz.setKey(aes_key);
	
	msg = SubGHz.begin(SUBGHZ_CH, SUBGHZ_PANID,  SUBGHZ_100KBPS, SUBGHZ_PWR_20MW);
	if(msg != SUBGHZ_OK)
	{
		SubGHz.msgOut(msg);
		while(1){ }
	}
	msg = SubGHz.rxEnable(NULL);
	if(msg != SUBGHZ_OK)
	{
		SubGHz.msgOut(msg);
		while(1){ }
	}
	
	pinMode(BLUE_LED,OUTPUT);
	digitalWrite(BLUE_LED,HIGH);
	
	Serial.println("TIME	HEADER	SEQ	PANID	RX_ADDR	TX_ADDR	RSSI	PAYLOAD");
	Serial.println("-----------------------------------------------------------------------------------------------------------------");

	
	//set pins
	for(i=0;i<3;i++){
    pinMode(LED[i],OUTPUT);
    pinMode(LQ[i],OUTPUT);
   }
   for(i=0;i<3;i++){
    pinMode(Button[i],INPUT);
   }

   
	return;
}

void loop(void)
{
	SUBGHZ_MAC_PARAM mac;
	short rx_len;
	short index=0;
	uint16_t data16;
	int recieved_data[3];
	
	rx_len = SubGHz.readData(rx_data,sizeof(rx_data));
	rx_data[rx_len]=0;
	if(rx_len>0)
	{
		digitalWrite(BLUE_LED, LOW);
		SubGHz.getStatus(NULL,&rx);										// get status of rx
		SubGHz.decMac(&mac,rx_data,rx_len);
		Serial.print(mac.payload);
		// print ln
		Serial.println("");
		digitalWrite(BLUE_LED, HIGH);

		
		for(i=0;i<3;i++){
			recieved_data[i]=(int)(mac.payload[i]-65);
		}
		
		if(recieved_data[0]==0){
			if(recieved_data[1]==0){
				if(recieved_data[2]==0){
					state[0]=false;
				}
				else if(recieved_data[2]==1){
					state[0]=true;
				}
			}
			else if(recieved_data[1]==1){
				if(recieved_data[2]==0){
					state[1]=false;
				}
				else if(recieved_data[2]==1){
					state[1]=true;
				}
			}
			else if(recieved_data[1]==2){
				if(recieved_data[2]==0){
					state[2]=false;
				}
				else if(recieved_data[2]==1){
					state[2]=true;
				}
			}
		}
	}
	
	for(i=0;i<3;i++){
	    state[i]=Read(Button[i],state[i]);
	    Switch(LQ[i],state[i]);
	    Light(LED[i],state[i]);
    }
	return;
}

