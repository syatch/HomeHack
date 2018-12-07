//Copyright (c) Takashi Ito 2018
//Twitter: @syatchIT
//github: https://github.com/syatch
#include "Serial_with_GR_ide.h"		// Additional Header
#define LED 26						// pin number of Blue LED
#define SUBGHZ_CH	36
#define SUBGHZ_PANID	0xffff		// panid
#define HOST_ADDRESS	0xffff	// distination address
uint8_t rx_data[256];
uint32_t last_recv_time = 0;
SUBGHZ_STATUS rx;							// structure for getting rx status
#define BLUE_LED	26

static const unsigned char *aes_key = NULL;		// disable AES key

unsigned char send_data[128];
int i,j;
bool serial_state;
unsigned char rxbuf[128];
//char(n+65);




void setup(void)
{
	uint8_t myAddr[8];		// setting of LED
	SUBGHZ_MSG msg;				// initializing Sub-GHz
	Serial.begin(9600);
	pinMode(LED,OUTPUT);			// setting of LED
	digitalWrite(LED,HIGH);
	
	
	msg = SubGHz.init();
	if(msg != SUBGHZ_OK)
	{
		SubGHz.msgOut(msg);
		while(1){ }
	}
	
	SubGHz.getMyAddr64(myAddr);


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

	
	return;
}

void loop(void)
{
	SUBGHZ_MAC_PARAM mac;
	short rx_len;
	short index=0;
	uint16_t data16;
	SUBGHZ_MSG msg;
	// Initializing
	
	
	rx_len = SubGHz.readData(rx_data,sizeof(rx_data));
	rx_data[rx_len]=0;// start Sub-GHz
	if(rx_len>0)
	{
		digitalWrite(BLUE_LED, LOW);
		SubGHz.getStatus(NULL,&rx);										// get status of rx
		SubGHz.decMac(&mac,rx_data,rx_len);
		Serial.print(mac.payload);
		// print ln
		Serial.println("");
		digitalWrite(BLUE_LED, HIGH);
	}
	//SubGHz.begin(SUBGHZ_CH, SUBGHZ_PANID,  SUBGHZ_100KBPS, SUBGHZ_PWR_20MW);
	i=0;
	serial_state=false;
	while(Serial.available()){
		rxbuf[i]=Serial.read();
		i++;
		serial_state=true;
		delay(10);
	}
	
	if(serial_state==true){
		// preparing data
		digitalWrite(LED,LOW);														// LED ON
		msg=SubGHz.send(SUBGHZ_PANID, HOST_ADDRESS, &rxbuf, sizeof(rxbuf),NULL);// send data
		digitalWrite(LED,HIGH);														// LED off
		SubGHz.msgOut(msg);
		// close
		for(i=0;i<128;i++){
			rxbuf[i]=0;
	    }
	}
	
	return;
}

