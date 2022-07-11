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

#define PIN_NO_SERVO D3

#define PIN_NO_LED_STRIP D6
#define LED_STRIP_LENGTH 6
