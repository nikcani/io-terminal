#include <Arduino.h>

#define PIN_NO_LED_INTERNAL D0

void blinkForX(int pin, int milliseconds, byte firstState, byte lastState);
void blinkForOneSecond(int pin);
void blinkInternalForX(int milliseconds);
void blinkInternalForOneSecond();
void setupLed(int pin, byte lowState);
void setupInternalLed();
