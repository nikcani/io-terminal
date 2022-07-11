#include "led.h"

void blinkForX(int pin, int milliseconds, byte firstState = HIGH, byte lastState = LOW) {
    digitalWrite(pin, firstState);
    delay(milliseconds);
    digitalWrite(pin, lastState);
}

void blinkForOneSecond(int pin) {
    blinkForX(pin, 1000);
}

void blinkInternalForX(int milliseconds) {
    blinkForX(PIN_NO_LED_INTERNAL, milliseconds, LOW, HIGH);
}

void blinkInternalForOneSecond() {
    blinkInternalForX(1000);
}

void setupLed(int pin, byte lowState = LOW) {
    pinMode(pin, OUTPUT);
    digitalWrite(pin, lowState);
}

void setupInternalLed() {
    setupLed(PIN_NO_LED_INTERNAL, HIGH);
}
