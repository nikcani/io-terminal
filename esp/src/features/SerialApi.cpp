#include "SerialApi.h"

SerialApi::SerialApi() {
    Serial.begin(9600);
    resetBuffer();
}

void SerialApi::write(String string) {
    Serial.println(string);
}

void SerialApi::actionListenerCycle(void (*callback)(String)) {
    char readChar = Serial.read();
    if (readChar == '#') {
        callback(buffer);
        resetBuffer();
    } else {
        buffer += readChar;
    }
}

void SerialApi::resetBuffer() {
    buffer = "";
}
