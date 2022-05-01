#include <Arduino.h>
#include <Wire.h>
#include "rgb_lcd.h"

#define BUTTON_OK 33
int BUTTON_OK_STATE = 0;

#define BUTTON_CLEAR 14
int BUTTON_CLEAR_STATE = 0;

rgb_lcd lcd;

// I make colors here for some reason
//color red
const int colorR_ROT = 255;
const int colorG_ROT = 0;
const int colorB_ROT = 0;

//color green
const int colorR_GRUEN = 0;
const int colorG_GRUEN = 255;
const int colorB_GRUEN = 0;

//color blue
const int colorR_BLAU = 0;
const int colorG_BLAU = 0;
const int colorB_BLAU = 255;

//color white
const int colorR_WEISS = 255;
const int colorG_WEISS = 255;
const int colorB_WEISS = 255;


String x[] = {"Never", "gonna", "give", "you up!", "Jetzt mal ernst","Wer soll denn", "darauf kommen", "dass man ein","------KABEL-----", "--AUFSCHNEIDEN--", "muss! }:-("};
int stringCount = 0; 

void setup(){
    // set up the LCD's number of columns and rows:
    lcd.begin(16, 2);
    // initialize the serial communications:
    Serial.begin(9600);

    // initialize the pushbutton pin as an input:
    pinMode(BUTTON_OK, INPUT);
    pinMode(BUTTON_CLEAR, INPUT);

    //rbg backlight color set
    lcd.setRGB(colorR_GRUEN,colorG_GRUEN,colorB_GRUEN);
    //rgb set coursor for fist column
    lcd.setCursor(0, 0);
    lcd.print("Ready!");

    //setup second column
    lcd.setCursor(0, 1);
    lcd.print("Start!");
    lcd.setCursor(10, 1);
    lcd.print("Clear!");

    Serial.println("setup done");
}

void loop()
{
    BUTTON_OK_STATE = digitalRead(BUTTON_OK);
    if(BUTTON_OK_STATE == HIGH){
        lcd.setRGB(colorR_ROT,colorG_ROT, colorB_ROT);
        delay(500);
        lcd.setCursor(0, 1);
        lcd.print("Next!");
        lcd.setCursor(0,0);
        lcd.println(x[stringCount]+ "                           ");

        //für debug
        Serial.println("StringCount = " + (String)stringCount);
        Serial.println("String word = " + x[stringCount]);

        //wrap around 
        stringCount = (stringCount +1) % 11;
        lcd.setRGB(colorR_GRUEN,colorG_GRUEN,colorB_GRUEN);
    }

    BUTTON_CLEAR_STATE = digitalRead(BUTTON_CLEAR);
    if(BUTTON_CLEAR_STATE == HIGH){
        lcd.setRGB(colorR_WEISS,colorG_WEISS,colorB_WEISS);
        delay(1000);
        lcd.clear();
        stringCount = 0;
        //rbg backlight color set
        lcd.setRGB(colorR_GRUEN,colorG_GRUEN,colorB_GRUEN);
        //rgb set coursor for fist column
        lcd.setCursor(0, 0);
        lcd.print("Ready!");

        //setup second column
        lcd.setCursor(0, 1);
        lcd.print("Start!");
        lcd.setCursor(10, 1);
        lcd.print("Clear!");
    }
}