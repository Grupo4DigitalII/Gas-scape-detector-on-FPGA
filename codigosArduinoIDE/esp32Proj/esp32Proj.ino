#define BLYNK_TEMPLATE_ID "************"                      //Datos de autenticación de la plataforma Blynk.
#define BLYNK_DEVICE_NAME "*****"                             //DEBEN estar al incio del código.
#define BLYNK_AUTH_TOKEN "********************************"
#define BLYNK_PRINT Serial                                    //Imprime en el monitor serial el estado de la conexión.

#include <WiFi.h>
#include <WiFiClient.h>
#include <BlynkSimpleEsp32.h>
#include <Blynk.h>
#include <SoftwareSerial.h>

#define WIFI_SSID "********"
#define WIFI_PASSWORD "********"

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

  if(fpga.read() == 1){                                       //Espera el aviso de la FPGA
    Serial.println("Wait...");
    while(i<3){                                               //Se deben recibir las dos secciones del dato
      while(DATO == -1){
        DATO = fpga.read();
        //Serial.print(".");
      }
      if(i == 1){
        DATOF += (DATO*100);                                  //Digitos más singificativos 
      }
      else if (i == 2){
        DATOF += DATO;                                        //Digitos menos significativos
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
