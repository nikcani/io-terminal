#include <Arduino.h>
#include <Servo.h>

#define PIN_NO_SERVO D3

void servoWriteDelayed(Servo servo, int angle);
void openLock(Servo servo);
void closeLock(Servo servo);
Servo setupServo();
