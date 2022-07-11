#include "LCD.h"

LCD::LCD() {
    lcd.begin(16, 2);
    bgWhite();
    printFirstRow("HELLO WORLD");
    printSecondRow("LEFT       RIGHT");
}

void LCD::printFirstRow(String string) {
    printRow(string, 0);
    first_row = string;
}

void LCD::printSecondRow(String string) {
    printRow(string, 1);
    second_row = string;
}

void LCD::setRGB(unsigned char r, unsigned char g, unsigned char b) {
    lcd.setRGB(r, g, b);
}

void LCD::bgRed() {
    setRGB(255, 0, 0);
}

void LCD::bgGreen() {
    setRGB(0, 255, 0);
}

void LCD::bgBlue() {
    setRGB(0, 0, 255);
}

void LCD::bgWhite() {
    setRGB(255, 255, 255);
}

void LCD::clear() {
    lcd.clear();
}

void LCD::printRow(String string, int row) {
    lcd.setCursor(0, row);
    lcd.print(string);
}
