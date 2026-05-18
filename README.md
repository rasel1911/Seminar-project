# Ultrasonic Distance Sensor with LED Indicator

## Overview
This Arduino sketch implements a distance measurement system using an HC-SR04 ultrasonic sensor that controls five LEDs. As an object approaches the sensor, LEDs light up progressively to indicate proximity levels.

## Hardware Requirements

### Components
- **Arduino Board** (Uno, Nano, Mega, etc.)
- **HC-SR04 Ultrasonic Sensor** (measure distance up to ~5 meters)
- **5 LED Indicators** (with appropriate current-limiting resistors)
- **Resistors** (220Ω recommended for LEDs)
- **Connecting Wires**
- **Power Supply**

### Pin Configuration
| Component | Arduino Pin |
|-----------|------------|
| HC-SR04 TRIG | Pin 9 |
| HC-SR04 ECHO | Pin 10 |
| LED 1 | Pin 2 |
| LED 2 | Pin 3 |
| LED 3 | Pin 4 |
| LED 4 | Pin 5 |
| LED 5 | Pin 6 |

## How It Works

### Distance Measurement
The HC-SR04 sensor measures distance by sending ultrasonic sound waves and calculating the echo time:
1. A 10µs trigger pulse is sent to the sensor
2. The sensor sends out 40 kHz ultrasonic waves
3. The echo pin measures the time until the sound bounces back
4. Distance is calculated using: **distance = duration / 58** (in centimeters)

### LED Indicator System
The 5 LEDs light up based on distance thresholds:

| LED | Threshold | Behavior |
|-----|-----------|----------|
| LED 1 | ≤ 20 cm | Lights up when object is within 20 cm |
| LED 2 | ≤ 15 cm | Lights up when object is within 15 cm |
| LED 3 | ≤ 10 cm | Lights up when object is within 10 cm |
| LED 4 | ≤ 5 cm | Lights up when object is within 5 cm |
| LED 5 | ≤ 2 cm | Lights up when object is within 2 cm |

**Result:** As an object approaches, LEDs light up sequentially, creating a visual proximity indicator.

## Code Structure

### Constants
```cpp
const int TRIG_PIN = 9;          // HC-SR04 trigger pin
const int ECHO_PIN = 10;         // HC-SR04 echo pin
const int LED_PINS[5] = {2, 3, 4, 5, 6};  // LED pins
const int THRESHOLDS[5] = {20, 15, 10, 5, 2};  // Distance thresholds (cm)
```

### Main Functions

#### `setup()`
- Initializes all GPIO pins (outputs for trigger and LEDs, input for echo)
- Starts Serial communication at 9600 baud

#### `loop()`
- Reads distance from the sensor
- Prints distance to Serial Monitor
- Updates LED states based on distance
- Repeats every 100ms (~10 readings per second)

#### `getDistance()`
- Sends trigger pulse to HC-SR04
- Measures echo pulse duration
- Converts duration to distance in centimeters
- Returns 999 if no echo (object out of range)

#### `updateLEDs(long distance)`
- Compares measured distance against thresholds
- Turns LEDs ON (HIGH) if distance is less than or equal to threshold
- Turns LEDs OFF (LOW) otherwise

## Installation & Usage

1. **Connect Hardware** according to the pin configuration above
2. **Upload Code** to Arduino using Arduino IDE
3. **Open Serial Monitor** (Tools > Serial Monitor) at 9600 baud
4. **Test:** Move an object closer to and farther from the sensor
5. **Observe:** LEDs will light up as the object approaches

## Serial Output
The sketch prints distance readings to the Serial Monitor:
```
Distance: 45 cm
Distance: 30 cm
Distance: 15 cm
...
```

## Customization

### Adjust Distance Thresholds
Modify the `THRESHOLDS` array:
```cpp
const int THRESHOLDS[5] = {20, 15, 10, 5, 2};  // Change these values (cm)
```

### Change Sampling Rate
Modify the delay in the `loop()` function:
```cpp
delay(100);  // Change from 100ms to desired interval (ms)
```

### Change Pin Assignments
Update the pin constants at the top:
```cpp
const int TRIG_PIN = 9;    // Change to desired pin
const int ECHO_PIN = 10;   // Change to desired pin
const int LED_PINS[5] = {2, 3, 4, 5, 6};  // Change to desired pins
```

## Technical Specifications

- **Measurement Range:** ~2 cm to 5 meters
- **Accuracy:** ±3 cm typical
- **Sampling Rate:** ~10 Hz (adjustable)
- **Update Frequency:** 100ms per cycle
- **Serial Baud Rate:** 9600

## Troubleshooting

| Issue | Solution |
|-------|----------|
| LEDs not lighting | Check wiring and LED polarity (anode to pin, cathode to ground) |
| No distance readings | Verify HC-SR04 pins and wiring; check Serial Monitor connection |
| Inconsistent readings | Ensure sensor is not at extreme angles; allow environment stabilization |
| All LEDs stay on | Object may be too close or sensor requires recalibration |
| No LEDs light up | Object may be out of range (>5m) or threshold values need adjustment |

## Notes
- The HC-SR04 works best with solid objects at angles perpendicular to the sensor
- Soft or angled surfaces may reflect sound poorly
- Allow ~50-100ms between measurements for best accuracy
- Consider adding debouncing if using for safety-critical applications

## License
This project is open-source and available for educational and personal use.
