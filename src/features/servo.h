#include <Arduino.h>
#include <Servo.h>

void servoWriteDelayed(Servo servo, int angle);
void openLock(Servo servo);
void closeLock(Servo servo);
Servo setupServo(int pin);
