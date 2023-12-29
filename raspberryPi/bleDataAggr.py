
from bluepy import btle
import aggrHelper as aggrhelp
import ble_device_setup as bleSet
from mqttClient import client
import time

sleepTime = 1 #in mins

def getData(device_01,periphSleep):
    
    MAC = device_01.mac

    print("BLE Central Device")
    print("Connect to:" + MAC)

    data = []
    try:
        blePeriphDevice = btle.Peripheral(MAC)
        characteristics = blePeriphDevice.getCharacteristics()

        for bleDevChar in device_01.services:
            
            datai = aggrhelp.getServiceChar(characteristics=characteristics,devCharacteristics=bleDevChar.characteristics,device=device_01,sleepTime=periphSleep)
            data += datai

        blePeriphDevice.disconnect()

        print("\n--- disconnecting ---\n")
        return data 
    except:
        print("no connection established ")

        return data

    


while True:
    pollTime = sleepTime * 60
    pheripheralSleep = pollTime - 20

    for aBleDevice in bleSet.bleDeviceData["devices"]:
        floor_cond_01 = bleSet.bleDevice.Device(name=aBleDevice["name"],mac=aBleDevice["mac"])
        bleServices = bleSet.bleServiceData["services"]

        for service in bleServices:
            bleSet.configureAService(floor_cond_01,service)
        data = getData(device_01 = floor_cond_01,periphSleep=pheripheralSleep)

        if (len(data) != 0):
            for someData in data:
                topic = "IoT_data/" + str(someData["device"])+ "/" + str(someData["service"]) + "/" + str(someData["characteristic"])
                (rc, mid) = client.publish(topic, str(someData), qos=1)
        else:
            pass
        
        time.sleep(10)

    time.sleep(pollTime)
