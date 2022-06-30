#include <SoftwareSerial.h>
#include <MQUnifiedsensor.h>

#define LED 13

#define Board ("Arduino UNO")
#define Pin (A2)
#define Type ("MQ-2") //MQ2
#define Voltage_Resolution (5)
#define ADC_Bit_Resolution (10) // For arduino UNO/MEGA/NANO
#define RatioMQ2CleanAir (9.83) //RS / R0 = 9.83 ppm

MQUnifiedsensor MQ2(Board, Voltage_Resolution, ADC_Bit_Resolution, Pin, Type);

SoftwareSerial nA7(8,9); //rx,tx

int MQ_PIN, MQ_PIN1, MQ_PIN2;


double ppm_log, ppm;

void setup()
{
  nA7.begin(9600);
  //Serial.begin(9600);
  //pinMode(LED, OUTPUT);

  MQ2.setRegressionMethod(1); //_PPM =  a*ratio^b
  MQ2.setA(3616.1); MQ2.setB(-2.675); // Configure the equation to to calculate LPG concentration
  MQ2.init();
  MQ2.setRL(2);

  /*Serial.print("Calibrating please wait.");
  float calcR0 = 0;
  for(int i = 1; i<=10; i ++)
  {
    MQ2.update(); // Update data, the arduino will read the voltage from the analog pin
    calcR0 += MQ2.calibrate(RatioMQ2CleanAir);
    Serial.print(".");
  }
  MQ2.setR0(calcR0/10);
  Serial.println("  done!.");*/
  MQ2.setR0(1.43);

  MQ2.serialDebug(true);
 
}


void loop()
{
  //digitalWrite(LED, LOW);
  MQ2.update();
  MQ_PIN = round(MQ2.readSensor());
  if(MQ_PIN > 10000){MQ_PIN = 10000;}
  else if(MQ_PIN < 0){MQ_PIN = 10000;}

  //Serial.print("MQ_PIN: ");
  //Serial.println(MQ_PIN);
   
  MQ_PIN1 = MQ_PIN / 100;
  MQ_PIN2 = MQ_PIN - (MQ_PIN1*100);

  //Serial.print("MQ_PIN1: ");
  //Serial.println(MQ_PIN1);
  //Serial.print("MQ_PIN2: ");
  //Serial.println(MQ_PIN2);
  //Serial.println("----------------");

  if (nA7.read()== 'A'){
 
    nA7.write(MQ_PIN1);
    nA7.write(MQ_PIN2);

  }

  //delay(200);
  //digitalWrite(LED, HIGH);
  //delay(200);
 
}
