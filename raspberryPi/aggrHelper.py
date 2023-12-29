
import struct

def getInt(byteObj):
    return (int.from_bytes(byteObj, byteorder='little'))

def getFloat(byteObj):
    [tmp] = struct.unpack('f',byteObj)
    return tmp

def getunsignedLong(byteObj):
    [tmp] = struct.unpack('L',byteObj)
    return tmp

def getLong(byteObj):
    [tmp] = struct.unpack('l',byteObj)
    return tmp

def getStr(byteObj):
    return (byteObj.decode('UTF-8')) 


def getChar(char,datatype):
    btobj = char.read()

    if datatype == 'str':
        return getStr(btobj)
    elif datatype == 'float':
        return getFloat(btobj)
    elif datatype == 'int':
        return getInt(btobj)
    elif datatype == 'ulong':
        return getunsignedLong(btobj)
    elif datatype == 'long':
        return getLong(btobj)
    else:
        return "not parseable"


def getServiceChar(characteristics,devCharacteristics,device,sleepTime):
    outputList = []
   
    for devChar in devCharacteristics: 
        for char in characteristics:
            output = {}
            if(char.uuid == devChar['uuid']):
                print(devChar['name']," UUID matched!")
                nanoRP2040_Char = getChar(char=char,datatype =devChar['datatype'])
                output = {str(devChar['name']):nanoRP2040_Char,"device":device.name,"mac":device.mac,"service":devChar["service"],"characteristic":str(devChar['name']),"unit":str(devChar['unit'])}
                outputList.append(output)
                characteristics.remove(char)
                
    return outputList