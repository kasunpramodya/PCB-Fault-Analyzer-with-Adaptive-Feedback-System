const int ledPin = 8;
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (Serial.available() > 0){
    String msg = Serial.readString();

    if (msg == "ON"){
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if (msg == "OFF"){
      digitalWrite(LED_BUILTIN, LOW);
    }
    // else {
    //   for (int i = 0; i < 5; i++){
    //     digitalWrite(redPin, HIGH);
    //     delay(100);
    //     digitalWrite(redPin, LOW);
    //     delay(100);
    //   }
    }
  }
