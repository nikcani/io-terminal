#include "Lock.h"

Lock::Lock() {
    servo.attach(PIN_NO_SERVO);
    close();
}

void Lock::open() {
    writeDelayed(0);
}

void Lock::close() {
    writeDelayed(140);
}

void Lock::writeDelayed(int angle) {
    servo.write(angle);
    delay(1000);
}
