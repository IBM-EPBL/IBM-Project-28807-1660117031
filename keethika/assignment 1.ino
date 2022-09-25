// C++ code
//
#include<Servo.h>
Servo s;
void setup()
{
  Serial.begin(9600);
   pinMode(4,INPUT);
   pinMode(2, INPUT);
  pinMode(2, OUTPUT);
  s.attach(3);
}
 

void loop()
{
  double a = analogRead(A0);
  double c = (((a/1024)*5)-0.5)*100;
  Serial.print("Celusius Value: ");
  Serial.println(c);
  delay(1000);
  
  if (c>50)
    digitalWrite(13,HIGH);
  else
    digitalWrite(13,LOW);
  int p = digitalRead(4);
  Serial.println(p);
  
  if (p==1){
    Serial.println("motion detected");
    delay(1000);
  }
  else{
      Serial.println("mption not detected");
       delay(1000);
  }
  s.write(0);
  delay(1000);
  s.write(30);
  delay(1000);
  s.write(60);
  delay(1000);
  s.write(130);
  delay(1000);
  s.write(1800);
  delay(1000);


 
  
}