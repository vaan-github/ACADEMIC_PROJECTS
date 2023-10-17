#include <cvzone.h>

SerialData serialData(2, 1); //(numOfValsRec,digitsPerValRec)
int valsRec[2]; // array of int with size numOfValsRec 

void setup() {
  pinMode(13, OUTPUT); //green
  pinMode(12, OUTPUT); //red
  serialData.begin();
}

void loop() {

  serialData.Get(valsRec);
  digitalWrite(13, valsRec[0]);
  digitalWrite(12, valsRec[1]);
  delay(10);
}
