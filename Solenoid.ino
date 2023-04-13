void setup() {
  Serial.println("Starting!");
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
}


void loop() {
  Serial.println("Adafruit MPU6050 test!");
  digitalWrite(7, HIGH);   //clockwise rotation
  digitalWrite(8, LOW);
  Serial.println("State1");
  delay(5000);
  digitalWrite(8, HIGH);   //anticlockwise rotation
  digitalWrite(7, LOW);
  Serial.println("State2");
  delay(5000);



}
