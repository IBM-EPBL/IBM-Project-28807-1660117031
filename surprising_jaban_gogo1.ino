void setup()
{
  pinMode(4,INPUT);
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  
}
void loop()
{
  int p = digitalRead(4);
  if (p==1) {
       digitalWrite(13, HIGH);
       Serial. println("Motion Detected! ") ;
       delay (1000);
  }
  else{
    digitalWrite(13, LOW);
    Serial. println("Motion not Detected") ;
    delay (1000) ;
}
}