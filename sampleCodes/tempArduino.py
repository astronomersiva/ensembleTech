int LDR = 0; 

void setup() 
{ 
  pinMode(LDR, INPUT); 
  Serial.begin(9600); 
} 

void loop() 
{ 
  int v = analogRead(LDR); 
  Serial.println(v); 
  delay(1000); 
}
