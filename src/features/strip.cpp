#include "strip.h"

Adafruit_NeoPixel setupLedStrip(int pin, int length) {
    Serial.println("setupLedStrip");

    Adafruit_NeoPixel strip(length, pin, NEO_GRB + NEO_KHZ800);

    strip.begin();
    strip.setBrightness(255);
    strip.show(); // Initialize all pixels to 'off'

    strip.setPixelColor(0, 255, 0, 0);
    strip.setPixelColor(1, 0, 255, 0);
    strip.setPixelColor(2, 0, 0, 255);
    strip.setPixelColor(3, 255, 255, 255);
    strip.setPixelColor(4, 255, 255, 0);
    strip.setPixelColor(5, 0, 255, 255);
    strip.show();

    return strip;
}
