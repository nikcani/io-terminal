#include <Arduino.h>
#include <Adafruit_NeoPixel.h>

#define PIN_NO_LED_STRIP D6
#define LENGTH_LED_STRIP 6

class LightIndicator {
public:
    LightIndicator();

    void showPixelColor(uint16_t n, uint8_t r, uint8_t g, uint8_t b);

    void clear();
};
