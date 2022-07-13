#include "LightIndicator.h"

Adafruit_NeoPixel strip(LENGTH_LED_STRIP, PIN_NO_LED_STRIP, NEO_GRB + NEO_KHZ800);

LightIndicator::LightIndicator() {
    strip.begin();

    // activate maximum brightness
    strip.setBrightness(255);

    // init to 'off'
    strip.show();
}

void LightIndicator::showPixelColor(uint16_t n, uint8_t r, uint8_t g, uint8_t b) {
    strip.setPixelColor(n, r, g, b);
    strip.show();
}

void LightIndicator::clear() {
    showPixelColor(0, 0, 0, 0);
    showPixelColor(1, 0, 0, 0);
    showPixelColor(2, 0, 0, 0);
    showPixelColor(3, 0, 0, 0);
    showPixelColor(4, 0, 0, 0);
    showPixelColor(5, 0, 0, 0);
    strip.clear();
    strip.show();
}
