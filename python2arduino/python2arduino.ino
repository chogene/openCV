const int first = 11;
const int second = 12;
const int third = 13;
const int dt = 1000;

void setup() 
{
    Serial.begin(115200);  // Set the same baud rate as in your Python code
    pinMode(first, OUTPUT);
    pinMode(second, OUTPUT);
    pinMode(third, OUTPUT);
}

void loop() 
{
    if (Serial.available() > 0) 
    {
        int received = Serial.read();  // Read the single byte as an integer
        Serial.print("Received: ");
        Serial.println(received);  // Echo back the received integer for debugging
        if (received == 3)
        {
            digitalWrite(first, HIGH);
        }
        else if (received == 4)
        {
            digitalWrite(second, HIGH);
        }
        else if (received == 5)
        {
            digitalWrite(third, HIGH);
        }
    }
    digitalWrite(first, LOW);
    digitalWrite(second, LOW);
    digitalWrite(third, LOW);

    delay(dt);
}
