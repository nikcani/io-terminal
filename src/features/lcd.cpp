#include "lcd.h"

rgb_lcd setupLcdDisplay() {
    Serial.println("setupLcdDisplay");

    rgb_lcd lcd;
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
