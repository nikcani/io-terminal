#include <Arduino.h>
#include <Wifi.h>

#define PIN_NO_LED 14
#define PIN_NO_BUTTON 26

volatile bool buttonState = false;

const char *ssid = "SSID";
const char *password = "PASSWORD";

void buttonClicked() {
    buttonState = digitalRead(PIN_NO_BUTTON);
}

void setup() {
    pinMode(PIN_NO_LED, OUTPUT);
    digitalWrite(PIN_NO_LED, LOW);

    pinMode(PIN_NO_BUTTON, INPUT);
    attachInterrupt(PIN_NO_BUTTON, buttonClicked, CHANGE);

    Serial.begin(115200);
    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.println("Connecting to WiFi..");
    }
    Serial.println("Connected to the WiFi network");
    Serial.println(WiFi.gatewayIP());
    Serial.println(WiFi.localIP());
}

void loop() {
    digitalWrite(PIN_NO_LED, buttonState);
}
