const int trigPin = 9;  
const int echoPin = 10; 
int data = 0;

 long duration ;
  long distance_cm ;
void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(10);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance_cm = duration / 58;
  if(distance_cm <100){
  Serial.println(distance_cm);
  }

  delay(1000);
}
