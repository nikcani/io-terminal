#include <Arduino.h>
#include <arduino_secrets.h>
#include <Wifi.h>
#include <PubSubClient.h>
#include <Adafruit_NeoPixel.h>

#define PIN_NO_BUTTON 26
#define PIN_NO_LED_RED 14
#define PIN_NO_LED_GREEN 22
#define PIN_NO_BUZZER 33

#define PIN_NO_LED_STRIP 32
#define LED_COUNT 6

WiFiClient espClient;
PubSubClient client(espClient);
Adafruit_NeoPixel strip(LED_COUNT, PIN_NO_LED_STRIP, NEO_GRB + NEO_KHZ800);

volatile bool buttonState;

void buttonClicked() {
    buttonState = digitalRead(PIN_NO_BUTTON);
}

void writeForX(int pin, int milliseconds) {
    digitalWrite(pin, 1);
    delay(milliseconds);
    digitalWrite(pin, 0);
}

void writeForOneSecond(int pin) {
    writeForX(pin, 1000);
}

void callback(char *topic, byte *payload, unsigned int length) {
    Serial.print("Message arrived [");
    Serial.print(topic);
    Serial.print("] ");
    for (int i = 0; i < length; i++) {
        Serial.print((char) payload[i]);
    }
    Serial.println();

    if (strcmp(topic, "led") == 0) {
        writeForOneSecond(PIN_NO_LED_RED);
        writeForOneSecond(PIN_NO_LED_GREEN);
    } else if (strcmp(topic, "led_red") == 0) {
        writeForOneSecond(PIN_NO_LED_RED);
    } else if (strcmp(topic, "led_green") == 0) {
        writeForOneSecond(PIN_NO_LED_GREEN);
    } else if (strcmp(topic, "buzzer") == 0) {
        writeForX(PIN_NO_BUZZER, 100);
    }
}

void reconnect() {
    while (!client.connected()) {
        Serial.print("Attempting MQTT connection...");
        if (client.connect("arduinoClient")) {
            Serial.println("connected");
            client.publish("hello", "world");
            client.subscribe("led");
            client.subscribe("led_red");
            client.subscribe("led_green");
            client.subscribe("buzzer");
        } else {
            Serial.print("failed, rc=");
            Serial.print(client.state());
            Serial.println(" try again in 5 seconds");
            // Wait 5 seconds before retrying
            delay(5000);
        }
    }
}

static void wifi_init(void) {
    Serial.begin(115200);
    WiFi.begin(SECRET_WIFI_SSID, SECRET_WIFI_PASS);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.println("Connecting to WiFi..");
    }
    Serial.println("Connected to the WiFi network");
    Serial.println(WiFi.gatewayIP());
    Serial.println(WiFi.localIP());
}

static void mqtt_init(void) {
    client.setServer(SECRET_MQTT_SERVER, 1883);
    client.setCallback(callback);
}

void test_led(int led_no) {
    strip.setPixelColor(led_no, 255, 0, 0);
    strip.show();
    delay(1000);
    strip.setPixelColor(led_no, 0, 255, 0);
    strip.show();
    delay(1000);
    strip.setPixelColor(led_no, 0, 0, 255);
    strip.show();
    delay(1000);
}

void test_led_brightness(int led_no) {
    strip.setBrightness(0);
    strip.setPixelColor(led_no, 255, 0, 0);
    strip.show();
    delay(1000);
    strip.setBrightness(8);
    strip.setPixelColor(led_no, 255, 0, 0);
    strip.show();
    delay(1000);
    strip.setBrightness(16);
    strip.setPixelColor(led_no, 255, 0, 0);
    strip.show();
    delay(1000);
    strip.setBrightness(32);
    strip.setPixelColor(led_no, 255, 0, 0);
    strip.show();
    delay(1000);
    strip.setBrightness(64);
    strip.setPixelColor(led_no, 255, 0, 0);
    strip.show();
    delay(1000);
    strip.setBrightness(128);
    strip.setPixelColor(led_no, 255, 0, 0);
    strip.show();
    delay(1000);
    strip.setBrightness(255);
    strip.setPixelColor(led_no, 255, 0, 0);
    strip.show();
    delay(1000);
}

void led_strip_setup() {
    strip.begin();
    strip.show(); // Initialize all pixels to 'off'
    delay(1000);
    test_led(0);
    test_led(1);
    test_led(2);
    test_led(3);
    test_led(4);
    test_led(5);
    test_led_brightness(0);
    test_led_brightness(1);
    test_led_brightness(2);
    test_led_brightness(3);
    test_led_brightness(4);
    test_led_brightness(5);
}

void setup() {
    /*pinMode(PIN_NO_LED_RED, OUTPUT);
    digitalWrite(PIN_NO_LED_RED, LOW);

    pinMode(PIN_NO_LED_GREEN, OUTPUT);
    digitalWrite(PIN_NO_LED_GREEN, LOW);

    pinMode(PIN_NO_BUZZER, OUTPUT);
    digitalWrite(PIN_NO_BUZZER, LOW);

    pinMode(PIN_NO_BUTTON, INPUT);
    attachInterrupt(PIN_NO_BUTTON, buttonClicked, CHANGE);*/

    led_strip_setup();

    wifi_init();

    mqtt_init();
}

void loop() {
    if (!client.connected()) {
        reconnect();
    }
    client.loop();
    if (buttonState) {
        buttonState = false;
        client.publish("button", "pressed");
    }
}
