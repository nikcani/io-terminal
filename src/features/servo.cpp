#include "servo.h"

void servoWriteDelayed(Servo servo, int angle) {
    servo.write(angle);
    delay(1000);
}

void openLock(Servo servo) {
    servoWriteDelayed(servo, 0);
}

void closeLock(Servo servo) {
    servoWriteDelayed(servo, 140);
}

Servo setupServo() {
    Serial.println("setupServo");

    Servo servo;
    servo.attach(PIN_NO_SERVO);
    closeLock(servo);

    return servo;
}
