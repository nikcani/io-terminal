#include "SerialApi.h"

SerialApi::SerialApi() {
    Serial.begin(9600);
    resetBuffer();
}

void SerialApi::write(String string) {}

void SerialApi::actionListenerCycle(void (*callback)(String)) {
    char readChar = Serial.read();
    if (readChar == '#') {
        nextPackage(callback);
    } else {
        buffer += readChar;
    }
}

void SerialApi::nextPackage(void (*callback)(String)) {
    packet = buffer;
    resetBuffer();
    callback(packet);
}

void SerialApi::resetBuffer() {
    buffer = "";
}
