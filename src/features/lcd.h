#include <Arduino.h>
#include <rgb_lcd.h>

class LCD {
public:
    LCD();

    void printFirstRow(String string);

    void printSecondRow(String string);

    void setRGB(unsigned char r, unsigned char g, unsigned char b);

    void bgWhite();

private:
    rgb_lcd lcd;
    String first_row;
    String second_row;

    void printRow(String string, int row);
};
