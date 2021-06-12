// Ultrasonic sensor ----------
// Trigger pin
const int trig = 7;
// Echo pin
const int echo = 6;

// distance
int dist;

// distance diff trigger

// Ultrasonic sensor ----------

// Motion sensor --------------
// motion sensor input
const int motion =1;
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

void loop(){
    // check serial port
        // set boolean for exepcting someone to true or false
    
    if (Serial.available() > 0){
        inputChar = Serial.read();
    }

    while (inputChar == 'y'){
        if (digitalRead(motion) == HIGH){
            Serial.println("motion");
        }
        if (crossed() == true){
          Serial.println("crossed");
        }
    }
    else{

    }
    // Are you expecting someone?
        //No
        // check if there is motion
            // if there is send signal to serial port (alret)
        
        // check if someone crossed
            // if they did, send signal to serial port (alret)

        //Yes
        // check if their is motion
            //send signal through serial port (check if their is a person)

        // check if someone crossed
            //send signal through serial port (check if their is a person)
    
    

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
