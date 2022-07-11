#include "LightIndicator.h"

Adafruit_NeoPixel strip(LENGTH_LED_STRIP, PIN_NO_LED_STRIP, NEO_GRB + NEO_KHZ800);

LightIndicator::LightIndicator() {
    Serial.println("setupLightIndicator");

    strip.begin();

    // activate maximum brightness
    strip.setBrightness(255);

    // init to 'off'
    strip.show();

    testing();
}

void LightIndicator::clear() {
    strip.clear();
    strip.show();
}

void LightIndicator::testing() {
    strip.setPixelColor(0, 255, 0, 0);
    strip.setPixelColor(1, 0, 255, 0);
    strip.setPixelColor(2, 0, 0, 255);
    strip.setPixelColor(3, 255, 255, 255);
    strip.setPixelColor(4, 255, 255, 0);
    strip.setPixelColor(5, 0, 255, 255);
    strip.show();
}
