const int TRIG_PIN = 9;
const int ECHO_PIN = 10;

// LEDs connected to pins 2–6
const int LED_PINS[5] = {2, 3, 4, 5, 6};

// Distance thresholds in cm (adjust to your needs)
const int THRESHOLDS[5] = {80, 60, 40, 20, 10};

void setup() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  for (int i = 0; i < 5; i++) {
    pinMode(LED_PINS[i], OUTPUT);
  }

  Serial.begin(9600);
}

void loop() {
  long distance = getDistance();
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  updateLEDs(distance);

  delay(100); // read ~10 times per second
}

// Measure distance using HC-SR04
long getDistance() {
  // Send a 10µs pulse to trigger
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // Read the echo pulse duration
  long duration = pulseIn(ECHO_PIN, HIGH, 30000); // timeout 30ms (~5m max)

  // Convert to centimeters (speed of sound = 343 m/s)
  long distance = duration / 58;

  // Return 999 if no echo (out of range)
  return (distance == 0) ? 999 : distance;
}

// Turn on LEDs based on how close the object is
void updateLEDs(long distance) {
  for (int i = 0; i < 5; i++) {
    if (distance <= THRESHOLDS[i]) {
      digitalWrite(LED_PINS[i], HIGH); // turn on
    } else {
      digitalWrite(LED_PINS[i], LOW);  // turn off
    }
  }
}