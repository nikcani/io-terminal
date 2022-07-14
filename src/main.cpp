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

void testing() {
    lightIndicator.showPixelColor(0, 255, 0, 0);
    lightIndicator.showPixelColor(1, 0, 255, 0);
    lightIndicator.showPixelColor(2, 0, 0, 255);
    lightIndicator.showPixelColor(3, 255, 255, 255);
    lightIndicator.showPixelColor(4, 255, 255, 0);
    lightIndicator.showPixelColor(5, 0, 255, 255);

    lock.open();
    blinkInternalForOneSecond();
    lock.close();

    lightIndicator.clear();
}

void interpretPacket(String packet) {
    lcd.bgBlue();
    delay(200);
    lcd.bgRed();
    lcd.clear();
    lcd.printFirstRow("interpretPacket");
    lcd.printSecondRow(String(packet.length()));
    delay(1000);
    /*String first = packet.substring(0, 16);
    String second = packet.substring(16, 32);
    String third = packet.substring(32, 48);
    lcd.clear();
    lcd.printFirstRow(String(first.length()) + "x" + String(second.length()) + "x" + String(third.length()));
    lcd.printSecondRow(first);
    delay(1000);*/
}

void setup() {
    serialApi = SerialApi();
    lightIndicator = LightIndicator();
    lcd = LCD();
    lock = Lock();
    setupInternalLed();
    setupButtons();

    //testing();
}

void loop() {
    if (button_left) buttonAction(PIN_NO_BUTTON_LEFT);
    if (button_right) buttonAction(PIN_NO_BUTTON_RIGHT);

    // Check to see if at least one character is available
    if (Serial.available()) serialApi.actionListenerCycle(&interpretPacket);
}
