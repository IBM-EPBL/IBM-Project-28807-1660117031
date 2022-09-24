void setup()
{
  Serial.begin(9600);
}
void loop()
{
  double a =analogRead(A0);
  double c =(((a/1024)*5)-0.5)*100;
  Serial.print("celsius value:");
  Serial.println(c);
  delay(1000);
}
{


   Seriai.begin(9600);
   pinMode(13,OUTPUT);
}
 
 {
  double a =analogRead(A0);
  double c =(((a/1024)*5)-0.5)*100;
  Serial.print("celsius value:");
  Serial.println(c);
  delay(1000);
  
  if (c>50)
    digitalWrite (13,HIGH);
  else
    digitalWrite (13,LOW);
 }

{
  pinMode(4,INPUT);
  Serial.begin(9600);
}

{
  int p =digitalRead(4);
  if (p==1) {
    digitalWrite(13,HIGH);
    Serial.println("Motion detected!");
    delay(1000);
  }
  else{
    digitalWrite(13,LOW);
    Serial.println("motion not detected");
    delay (1000);
  }
#include<Servo.h>
  Servo s;
  void setup()
  {
    s.attach(3);
  }
  void loop()
  {
    S.write(0);
    delay (1000);
    S.write(30);
    delay(1000);
    S.write(70);
    delay(1000);
    S.write(130);
    delay(1000);
    S.write(180);
    delay(1000);
  }
void setup()
{
  pinMode(12,OUTPUT);
}
 void ioop()
 {
   tone(12,20);
   delay
 }
  
    
    
    
    
    
    
    
  
   
    
             
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
  
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                
                 
  
  
