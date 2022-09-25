#include<Servo.h>
Servo s;
int buzz=12;
void setup()
{
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(buzz,OUTPUT);
  pinMode(4,INPUT);
  s.attach(3);
}

void loop()
{
  for(int i=0;i<=180;i=i+10)
  {
  s.write(i);
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000); 
  }
  for(int p=0;p<=180;p=p++)
  {
  double a = analogRead(A0);
  double c = (((a/1024*5)-0.5)*100);
  Serial.print("celcius value:");
  Serial.println(c);
  
  if(c>60)
  {
    tone(buzz,200);
    delay(250);
    noTone(buzz);
    tone(buzz,200);
    delay(250);
    tone(buzz,200);
    delay(250);
    noTone(buzz);
    tone(buzz,200);
    delay(250);
    noTone(buzz);
    }
  else
     
  delay(1000);
}
  int v = digitalRead(4);
  if(v==1)
  {
        Serial.println("motion detected");
        delay(1000);
  }
  else 
  {
    Serial.println("motion not detected");
    delay(1000);
  }
    
  
}

