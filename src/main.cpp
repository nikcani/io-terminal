#include <Arduino.h>
#include <Adafruit_NeoPixel.h>
#include <rgb_lcd.h>
#include <Servo.h>

#include <functions.h>

#include "main_pins.h"

volatile bool button_left;
volatile bool button_right;

void IRAM_ATTR buttonEventLeft();
void IRAM_ATTR buttonEventRight();

Adafruit_NeoPixel strip;
rgb_lcd lcd;
Servo servo;

void buttonEventLeft() {
    button_left = digitalRead(PIN_NO_BUTTON_LEFT);;
}

void buttonEventRight() {
    button_right = digitalRead(PIN_NO_BUTTON_RIGHT);;
}

void setupButtons() {
    Serial.println("setupButtons");

    pinMode(PIN_NO_BUTTON_LEFT, INPUT);
    attachInterrupt(digitalPinToInterrupt(PIN_NO_BUTTON_LEFT), buttonEventLeft, CHANGE);

    pinMode(PIN_NO_BUTTON_RIGHT, INPUT);
    attachInterrupt(digitalPinToInterrupt(PIN_NO_BUTTON_RIGHT), buttonEventRight, CHANGE);
}

rgb_lcd setupLcdDisplay() {
    Serial.println("setupLcdDisplay");
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

    return lcd;
}

void testing() {
    Serial.println("testing started");

    openLock(servo);
    blinkInternalForOneSecond();
    closeLock(servo);

    Serial.println("testing done");
}

void setup() {
    Serial.begin(9600);

    Serial.println("setup started");

    strip = setupLedStrip(PIN_NO_LED_STRIP, LED_STRIP_LENGTH);
    lcd = setupLcdDisplay();
    servo = setupServo(PIN_NO_SERVO);
    setupInternalLed();
    setupButtons();

    Serial.println("setup done");

    testing();
}

void buttonAction(int pin) {
    String message;
    if (pin == PIN_NO_BUTTON_LEFT) {
        button_left = false;
        message = "button_left_pressed";
    }
    if (pin == PIN_NO_BUTTON_RIGHT) {
        button_right = false;
        message = "button_right_pressed";
    }
    Serial.println(message);
    lcd.setRGB(0, 255, 0);
    delay(200);
    lcd.setRGB(255, 255, 255);
}

void loop() {
    if (button_left) buttonAction(PIN_NO_BUTTON_LEFT);
    if (button_right) buttonAction(PIN_NO_BUTTON_RIGHT);

    /*if (Serial.available()) // Check to see if at least one character is available
    {
        char ch = Serial.read();
        Serial.println(ch);
        //if (ch >= '0' && ch <= '9') // is this an ascii digit between 0 and 9?
        //{
        //    blinkRate = (ch - '0'); // ASCII value converted to numeric value
        //}
    }*/
}
