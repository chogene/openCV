const int first = 11;
const int second = 12;
const int third = 13;
const int dt = 1000;

void setup() 
{
    Serial.begin(115200);  
    pinMode(first, OUTPUT);
    pinMode(second, OUTPUT);
    pinMode(third, OUTPUT);
}

void loop() 
{
        int received = Serial.read();  // Read the single byte as an integer
        int command = received - '0';
 
        Serial.print("Received: ");
        Serial.println(command);  // Echo back the received integer for debugging
        if (command == 3)
        {
            digitalWrite(first, HIGH);
            digitalWrite(second, LOW);
            digitalWrite(third, LOW);
        }
        else if (command == 4)
        {
            digitalWrite(second, HIGH);
            digitalWrite(first, LOW);
            digitalWrite(third, LOW);
        }
        else if (command == 5)
        {
            digitalWrite(third, HIGH);
            digitalWrite(first, LOW);
            digitalWrite(second, LOW);
        }
        
}
