#include <Arduino.h>
#include <Servo.h>

#define PIN_NO_SERVO D3

class Lock {
public:
    Lock();

    void open();

    void close();

private:
    Servo servo;

    void writeDelayed(int angle);
};
