//mit hilfe von
//https://dronebotworkshop.com/esp32-servo/

#include <Arduino.h>
#include <Wire.h>
#include <ESP32Servo.h>

#define BUTTON_LEFT 33
int BUTTON_LEFT_STATE = 0;

#define BUTTON_RIGHT 14
int BUTTON_RIGHT_STATE = 0;

//max und min pos vom servo
// die positionen habe ich einfach so definiert
// können natürlich auch einfach geändert werden
// waren bei tests die ermittelten min und max positionen des servos
const int minPos = 5; // offene position des schließfachs
const int maxPos = 180; // geschlossene position des schließfachs

//anschlusspin des servos, nicht alle pins funktionieren
const int SERVO_PIN = 16;
int pos = minPos;
Servo myServo;

//SF = SchließFach
void openSF(){
	if(pos >= minPos){
		myServo.write(minPos);
		pos = minPos; 
		Serial.println("FACH WIRD GEÖFFNET");
		delay(1500);
	}
}

//SF = SchließFach
void closeSF(){
	if(pos <= maxPos){
		myServo.write(maxPos);
		pos = maxPos; 
		Serial.println("FACH WIRD GESCHLOSSEN");
		delay(1500);
	}
}

//zeigt die aktuelle position des motors an ---- faulheitsfunkion ^^
void showAktPos(){
	Serial.print("Aktuelle Position: ");
	//xxx.read() liest die aktuelle position des servos aus (int-wert)
	Serial.println(myServo.read());
}

//ein kleiner test um denn servo zu aktivieren
//und um zeit zu verschaffen damit ich mich mit dem serial minitor verbinden kann
void test(){
	Serial.println("alles auf minimal position");
	myServo.write(minPos);
	showAktPos();
	delay(3000);

	Serial.println("ich bin sowas auf 180");
	myServo.write(maxPos);

	showAktPos();
	delay(3000);
	Serial.println("TEST BEENDET und READY");
}


void setup(){
    Serial.begin(9600);
    pinMode(BUTTON_LEFT, INPUT);
    pinMode(BUTTON_RIGHT,INPUT);

	//der esp braucht einen timer um den servo anzusprechen und zu synchronisieren
	//es ist optional, dann werden alle timer im system genutzt
	ESP32PWM::allocateTimer(0);
	//die rate mit dem servo angesprchen wird hier 100 Hz
	myServo.setPeriodHertz(100);
	//servopin muss angegeben werden
	myServo.attach(SERVO_PIN);
	
	//Servo test
	test();
}

void loop()
{
	//BUTTONS
	// linker button "ÖFFNET"
	BUTTON_LEFT_STATE = digitalRead(BUTTON_LEFT);

	//rechter button "SCHLIEßT"
	BUTTON_RIGHT_STATE = digitalRead(BUTTON_RIGHT);

	//anmerkung: vielleicht noch überprüfen ob der andere button nicht auch noch gedrückt wird
	if(BUTTON_LEFT_STATE == HIGH){
		Serial.println("Linke Taste gedrueckt");
		openSF();
		showAktPos();
	}
	else if(BUTTON_RIGHT_STATE == HIGH){
		Serial.println("Rechte Taste gedrueckt");	
		closeSF();
		showAktPos();
	}
	//soviele dalays im code damit der motor nicht überhitzt
	delay(1000);
}

/*	
	alternative anstuerungsmöglichkeit
	funktioniert nicht ganz zufriedenstellend (wert 1000 = minimum, wert 2000 = maximum)
	https://www.arduino.cc/reference/en/libraries/servo/writemicroseconds/

	myServo.writeMicroseconds(1000);
	delay(1000);
	showAktPos(); //pos 44
	delay(1000);
	
	myServo.writeMicroseconds(1500);
	delay(1000);
	showAktPos(); //pos 93
	delay(1000);

	myServo.writeMicroseconds(2000);
	delay(1000);
	showAktPos(); //pos 141
	delay(1000);
	*/