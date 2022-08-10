#include <Arduino.h>

class SerialApi {
public:
    SerialApi();

    void write(String string);

    void actionListenerCycle(void (*callback)(String));

private:
    String buffer;

    void resetBuffer();
};
