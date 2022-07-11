#include <Arduino.h>

class SerialApi {
public:
    SerialApi();

    void write(String string);

    void actionListenerCycle(void (*callback)(String));

private:
    String buffer;
    String packet;

    void nextPackage(void (*callback)(String));

    void resetBuffer();
};
