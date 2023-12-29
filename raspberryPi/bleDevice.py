
class Device:
    def __init__(self, name, mac):
        self.name = name
        self.mac = mac
        self.services = []
    
    def addServices(self,service):
        self.services.append(service)
        return self.services

class Service:
    def __init__(self, name, uuid):
        self.name = name
        self.uuid = uuid
        self.characteristics = []
    
    def setCharacteristics(self,name,uuid,datatype,unit):
        characteristic = {} 
        characteristic["name"] = name
        characteristic["uuid"] = uuid
        characteristic["datatype"] = datatype
        characteristic["unit"] = unit
        characteristic["service"] = self.name
        return characteristic
    
    def addCharacteristics(self,characteristic):
        self.characteristics.append(characteristic)
        return self.characteristics

