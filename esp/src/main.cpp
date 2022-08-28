#include <Arduino.h>
#include "functions.h"

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
SerialApi serialApi;

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
        lcd.bgGreen();
    }
    if (pin == PIN_NO_BUTTON_RIGHT) {
        button_right = false;
        message = "button_right_pressed";
        lcd.bgRed();
    }
    serialApi.write(message);
    delay(200);
    lcd.bgWhite();
}

void setupButtons() {
    pinMode(PIN_NO_BUTTON_LEFT, INPUT);
    attachInterrupt(digitalPinToInterrupt(PIN_NO_BUTTON_LEFT), buttonEventLeft, CHANGE);

    pinMode(PIN_NO_BUTTON_RIGHT, INPUT);
    attachInterrupt(digitalPinToInterrupt(PIN_NO_BUTTON_RIGHT), buttonEventRight, CHANGE);
}

void interpretPacket(String packet) {
    String action = packet.substring(0, 16);
    String data_1 = packet.substring(16, 32);
    String data_2 = packet.substring(32, 48);

    action.trim();

    if (action == "display_print") {
        lcd.printFirstRow(data_1);
        lcd.printSecondRow(data_2);
    } else if (action == "display_clear") {
        lcd.clear();
    } else if (action == "display_color") {
        lcd.setRGB(data_1.substring(0, 2).toInt(), data_1.substring(4, 6).toInt(), data_1.substring(8, 10).toInt());
    } else if (action == "li_activate") {
        lightIndicator.showPixelColor(
                data_1.toInt(),
                data_2.substring(0, 2).toInt(),
                data_2.substring(4, 6).toInt(),
                data_2.substring(8, 10).toInt()
        );
    } else if (action == "li_clear") {
        lightIndicator.clear();
    } else if (action == "lock_open") {
        lock.open();
    } else if (action == "lock_close") {
        lock.close();
    }
}

void setup() {
    serialApi = SerialApi();
    lightIndicator = LightIndicator();
    lcd = LCD();
    lock = Lock();
    setupInternalLed();
    setupButtons();
}

void loop() {
    // handle button press
    if (button_left) buttonAction(PIN_NO_BUTTON_LEFT);
    if (button_right) buttonAction(PIN_NO_BUTTON_RIGHT);

    // interpret serial characters
    if (Serial.available()) serialApi.actionListenerCycle(&interpretPacket);
}
