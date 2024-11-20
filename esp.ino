#include <ESP8266WiFi.h>
#include <ArduinoJson.h>

#include "DHT.h"
#define DHTTYPE DHT11



// вписываем здесь SSID и пароль для вашей WiFi-сети: 
const char* ssid = "Kiski_muriski";
const char* password = "eY7m76S_rP";


const uint8_t DHTPin = D7;
DHT dht(DHTPin, DHTTYPE);


float Temperature;
float Humidity;

void setup() {
  Serial.begin(115200);
  dht.begin(); 

  WiFi.begin(ssid, password);
 
  Serial.println("Подключение к WiFi");
 
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
 
  Serial.println("");
  Serial.print("Подключение успешно, ip=");
  Serial.println(WiFi.localIP());
 
  // Отправляем сообщение в WhatsApp
  Serial.print("Привет от ESP!\n");
}

void loop() {
  // put your main code here, to run repeatedly:
  float temp = dht.readTemperature();
  float hum = dht.readHumidity();
  Serial.print(temp);
  Serial.print(' ');
  Serial.print(hum);
  Serial.print('\n');
  delay(5000);
}

