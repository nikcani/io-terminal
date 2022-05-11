#include "functions.h"

void blinkForX(int pin, int milliseconds) {
    digitalWrite(pin, HIGH);
    delay(milliseconds);
    digitalWrite(pin, LOW);
    delay(milliseconds);
}

void blinkForOneSecond(int pin) {
    blinkForX(pin, 1000);
}
