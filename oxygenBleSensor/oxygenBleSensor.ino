#include <Arduino_MKRENV.h>
#include <ArduinoBLE.h>
#include "DFRobot_OxygenSensor.h"


BLEService oxygenConcService("BLE ID"); // create service
BLEFloatCharacteristic  oxygenConcentrationCharacteristic("ID", BLERead | BLENotify | BLEBroadcast);


#define Oxygen_IICAddress ADDRESS_3
#define COLLECT_NUMBER  10             // collect number, the collection range is 1-100.
DFRobot_OxygenSensor oxygen;



void setup() {
  // put your setup code here, to run once:
  
  Serial.begin(9600);

  Serial.println("started!");
  
  while (!Serial);

  // begin BLE initialization
  if (!BLE.begin())
  {
    Serial.println("starting Bluetooth® Low Energy module failed!");
    while (1);
  }
  BLE.setLocalName("oxygenMonitor_01");
  BLE.setAdvertisedService(oxygenConcService);
  oxygenConcService.addCharacteristic(oxygenConcentrationCharacteristic);
  BLE.addService(oxygenConcService);

   BLE.advertise();
  Serial.println("Bluetooth® device active, waiting for connections...");

  // Print out full UUID and MAC address.
  Serial.println("Peripheral advertising info: ");
  Serial.print("Name: ");
  Serial.println("oxygenMonitor_01");
  Serial.print("MAC: ");
  Serial.println(BLE.address());

  while(!oxygen.begin(Oxygen_IICAddress)){
  Serial.println("I2c device number error !");
  delay(1000);
  }

}

void loop() {
  // put your main code here, to run repeatedly:

    // listen for Bluetooth® Low Energy peripherals to connect:
   BLEDevice central = BLE.central();

    if (central) {
      Serial.print("Connected to central: ");
      // print the central's MAC address:
      Serial.println(central.address());

      while (central.connected()) {
        // if the remote device wrote to the characteristic,

      float oxygenData = oxygen.getOxygenData(COLLECT_NUMBER);
      oxygenConcentrationCharacteristic.writeValue(oxygenData);
      Serial.print(" oxygen concentration is ");
      Serial.print(oxygenData);
      Serial.println(" %vol");

      Serial.println();
      // delay(1000);

      // delay(100000);
      delay(1000);
    }
    // when the central disconnects, print it out:
    Serial.print(F("Disconnected from central: "));
    Serial.println(central.address());
    }
  }


