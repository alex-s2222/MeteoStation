#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <ArduinoJson.h>


#include "DHT.h"
#define DHTTYPE DHT11


// вписываем здесь SSID и пароль для вашей WiFi-сети:
// const char* ssid = "Kiski_muriski";
// const char* password = "eY7m76S_rP";
const char* ssid = "iPhone (Alexey)";
const char* password = "12346789";

const char* serverName = "http://172.20.10.9:8000/";
WiFiClient wifiClient;


const uint8_t DHTPin = D7;
DHT dht(DHTPin, DHTTYPE);


void setup() {
  Serial.begin(115200);
  dht.begin();

  // WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  Serial.println("Подключение к WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.print("Подключение успешно, ip=");
  Serial.println(WiFi.localIP());
}

void loop() {
  // put your main code here, to run repeatedly:
  float temp = dht.readTemperature();
  float hum = dht.readHumidity();
  Serial.printf("%.2f %.2f \n", temp, hum);

  HTTPClient http;
  http.begin(wifiClient, serverName);
  http.addHeader("Content-Type", "application/json");

  DynamicJsonDocument doc(512);
  JsonObject object = doc.to<JsonObject>();
  object["temperature"] = temp;
  object["humidity"] = hum;

  String data;
  serializeJsonPretty(object, data);
  Serial.println(data);

  int httpCode = http.POST(data);

  if (httpCode == 200) {
    Serial.println("POST succeeded with code:");
    Serial.println(httpCode);

  } else if (httpCode != 200) {
    Serial.println("POST failed with code:");
    Serial.println(httpCode);

  } else {
    Serial.println("Unknown error");
  }
  http.end();
  delay(5000);
}
