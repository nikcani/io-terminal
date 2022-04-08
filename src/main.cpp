#include <Arduino.h>

#define PIN_NO_LED 14
#define PIN_NO_BUTTON 26

volatile bool buttonState = false;

void buttonClicked()
{
  buttonState = digitalRead(PIN_NO_BUTTON);
}

void setup()
{
  pinMode(PIN_NO_LED, OUTPUT);
  digitalWrite(PIN_NO_LED, LOW);

  pinMode(PIN_NO_BUTTON, INPUT);
  attachInterrupt(PIN_NO_BUTTON, buttonClicked, CHANGE);
}

void loop()
{
  digitalWrite(PIN_NO_LED, buttonState);
}
