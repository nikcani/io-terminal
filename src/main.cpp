#include <Arduino.h>
#include <functions.h>

/*
 * Pinout
 * https://joy-it.net/files/files/Produkte/SBC-NodeMCU/SBC-NodeMCU_pinout.png
 * https://www.google.com/search?q=esp8266+gpio+pinout
 *
 * https://github.com/esp8266/Arduino/issues/584#issuecomment-123715951
 * static const uint8_t D0   = 16;
 * static const uint8_t D1   = 5;
 * static const uint8_t D2   = 4;
 * static const uint8_t D3   = 0;
 * static const uint8_t D4   = 2;
 * static const uint8_t D5   = 14;
 * static const uint8_t D6   = 12;
 * static const uint8_t D7   = 13;
 * static const uint8_t D8   = 15;
 * static const uint8_t D9   = 3;
 * static const uint8_t D10  = 1;
*/

#define PIN_NO_BUTTON_LEFT D8
#define PIN_NO_BUTTON_RIGHT D7

LCD lcd;
Lock lock;
LightIndicator lightIndicator;

volatile bool button_left;
volatile bool button_right;

// @formatter:off
void IRAM_ATTR buttonEventLeft();
void IRAM_ATTR buttonEventRight();
// @formatter:on

void buttonEventLeft() {
    button_left = digitalRead(PIN_NO_BUTTON_LEFT);;
}

void buttonEventRight() {
    button_right = digitalRead(PIN_NO_BUTTON_RIGHT);;
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

void setupButtons() {
    Serial.println("setupButtons");

    pinMode(PIN_NO_BUTTON_LEFT, INPUT);
    attachInterrupt(digitalPinToInterrupt(PIN_NO_BUTTON_LEFT), buttonEventLeft, CHANGE);

    pinMode(PIN_NO_BUTTON_RIGHT, INPUT);
    attachInterrupt(digitalPinToInterrupt(PIN_NO_BUTTON_RIGHT), buttonEventRight, CHANGE);
}

void testing() {
    Serial.println("testing started");

    lock.open();
    blinkInternalForOneSecond();
    lock.close();

    Serial.println("testing done");
}

void setup() {
    Serial.begin(9600);

    Serial.println("setup started");

    lightIndicator = LightIndicator();
    lcd = LCD();
    lock = Lock();
    setupInternalLed();
    setupButtons();

    Serial.println("setup done");

    testing();

    lightIndicator.clear();
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
