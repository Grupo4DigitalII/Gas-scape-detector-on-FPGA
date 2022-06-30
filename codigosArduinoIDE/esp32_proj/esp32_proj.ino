#define BLYNK_TEMPLATE_ID "TMPL-uBWhYEV"
#define BLYNK_DEVICE_NAME "ESP32"
#define BLYNK_AUTH_TOKEN "Zkcns-OCFZheCG5vnHrQPTrl498yX6ay"
#define BLYNK_PRINT Serial

#include <WiFi.h>
#include <WiFiClient.h>
#include <BlynkSimpleEsp32.h>
#include <Blynk.h>
#include <SoftwareSerial.h>

#define WIFI_SSID "Redmi Note 10Sc"
#define WIFI_PASSWORD "Sierra117"

SoftwareSerial fpga(16,17);

int DATO = -1;
int DATOF = 0;
int i = 1;

void setup() {
  Serial.begin(9600);
  delay(1000);
  Blynk.begin(BLYNK_AUTH_TOKEN, WIFI_SSID, WIFI_PASSWORD);
  fpga.begin(9600);
  Serial.println("Ready...");

}

void loop() {

  if(fpga.read() == 1){
    Serial.println("Wait...");
    while(i<3){
      while(DATO == -1){
        DATO = fpga.read();
        //Serial.print(".");
      }
      if(i == 1){
        DATOF += (DATO*100);
      }
      else if (i == 2){
        DATOF += DATO;
      }
      i++;
      DATO = -1;
    }
    Blynk.run();
    Blynk.virtualWrite(V0, DATOF);
    Serial.print("Dato FPGA: ");
    Serial.println(DATOF);
    }
  DATO = -1;
  i = 1;
  DATOF = 0;
}
