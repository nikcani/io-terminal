#include <Arduino.h>
#include <Adafruit_NeoPixel.h>

#define PIN_NO_LED_STRIP D6
#define LENGTH_LED_STRIP 6

class LightIndicator {
public:
    LightIndicator();

    void clear();

private:
    void testing();
};
