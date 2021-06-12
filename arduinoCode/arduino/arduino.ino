// Ultrasonic sensor ----------
// Trigger pin
const int trig = 7;
// Echo pin
const int echo = 6;

// distance diff trigger

// Ultrasonic sensor ----------

// Motion sensor --------------
// motion sensor input
const int motion =5;
// Motion sensor --------------

// Leds -----------------------
// blue led output
const int blue = 13;
// red led output
const int red = 2;
// orange led output
const int orange = 3;
// yellow led output
const int yellow = 4;
// Leds -----------------------

// Serial Input char ----------
char inputChar;
// Serial Input char ----------

void setup(){
    // Ultrasonic sensor
    pinMode(trig, OUTPUT);
    pinMode(echo, INPUT);

    //Motion sensor
    pinMode(motion, INPUT);
    
    // LEDS
    pinMode(blue, OUTPUT);
    pinMode(red, OUTPUT);
    pinMode(orange, OUTPUT);
    pinMode(yellow, OUTPUT);

    Serial.begin(9600);
}

bool prevMotion = false;
bool prevCrossed = false;

void loop(){
      
    if (digitalRead(motion) == HIGH){
      Serial.println("motion");
      
    }
    if (crossed() == true){
      Serial.println("crossed");
    }
   
}

float duration;
float distance;

double dist(){
    digitalWrite(trig, LOW);
    delayMicroseconds(2);
    digitalWrite(trig, HIGH);
    delayMicroseconds(10);
    digitalWrite(trig, LOW);
    duration = pulseIn(echo, HIGH);
    distance = duration * 0.034 / 2;
    return distance;
}

bool crossed(){
    if (dist() < 30){
        return true;
    }
    else {
        return false;
    }
}