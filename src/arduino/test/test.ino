#include <Servo.h>

Servo myservo;

int pin = 3;
String s;

void setup()
{
  myservo.attach(pin);
  Serial.begin(9600);
}

void loop()
{
  if(Serial.available() > 0)
  {
    //s = Serial.readString();
    int data = Serial.read();
    myservo.write(data);
  }
}

