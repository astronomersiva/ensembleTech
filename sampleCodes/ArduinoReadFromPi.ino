
void setup()
{
  Serial.begin(9600);  
}

void loop()
{
  if(Serial.available())
  {
    while(Serial.available()>0)
    {
      char inByte = Serial.read();
      Serial.print(inByte);
    }
    Serial.print('\n');
    Serial.flush();
  }
  delay(3000);
}
