#include <Arduino.h>
#include <Adafruit_NeoPixel.h>
#include <rgb_lcd.h>

#include <secrets.h>
#include <functions.h>

#define PIN_NO_BUTTON_LEFT 33
#define PIN_NO_BUTTON_RIGHT 26
#define PIN_NO_LED_STRIP 14
#define LED_STRIP_LENGTH 6

volatile bool button_left;
volatile bool button_right;

rgb_lcd lcd;
Adafruit_NeoPixel strip(LED_STRIP_LENGTH, PIN_NO_LED_STRIP, NEO_GRB + NEO_KHZ800);

void buttonEventLeft() {
    button_left = digitalRead(PIN_NO_BUTTON_LEFT);
}

void buttonEventRight() {
    button_right = digitalRead(PIN_NO_BUTTON_RIGHT);
}

void setupButtons() {
    pinMode(PIN_NO_BUTTON_LEFT, INPUT);
    attachInterrupt(PIN_NO_BUTTON_LEFT, buttonEventLeft, CHANGE);

    pinMode(PIN_NO_BUTTON_RIGHT, INPUT);
    attachInterrupt(PIN_NO_BUTTON_RIGHT, buttonEventRight, CHANGE);
}

void setupLedStrip() {
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
}

void setupLcdDisplay() {
    lcd.begin(16, 2);

    lcd.setRGB(255, 255, 255);

    // first col
    lcd.setCursor(0, 0);
    lcd.print("HELLO WORLD");

    // second col
    lcd.setCursor(0, 1);
    lcd.print("LEFT");
    lcd.setCursor(10, 1);
    lcd.print("RIGHT");
}

void setup() {
    Serial.begin(115200);

    setupButtons();
    setupLedStrip();
    setupLcdDisplay();

    Serial.println("setup done");
}

void buttonAction(int pin, String message) {
    digitalWrite(PIN_NO_BUTTON_LEFT, HIGH);
    delayMicroseconds(50);
    digitalWrite(PIN_NO_BUTTON_LEFT, LOW);
    delay(100);
    if (pin == PIN_NO_BUTTON_LEFT) button_left = false;
    if (pin == PIN_NO_BUTTON_RIGHT) button_right = false;

    Serial.println(message);
}

void loop() {

}

/*void loop() {
    if (button_left) buttonAction(PIN_NO_BUTTON_LEFT, "button_left_pressed");
    if (button_right) buttonAction(PIN_NO_BUTTON_RIGHT, "button_right_pressed");

    if (Serial.available()) // Check to see if at least one character is available
    {
        char ch = Serial.read();
        Serial.println(ch);
        //if (ch >= '0' && ch <= '9') // is this an ascii digit between 0 and 9?
        //{
        //    blinkRate = (ch - '0'); // ASCII value converted to numeric value
        //}
    }
}
*/