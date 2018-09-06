import i2c

LM75B_REG_CONF = 0x01
LM75B_REG_TEMP = 0x00
LM75B_REG_TOS = 0x03
LM75B_REG_THYST = 0x02

class SW10(i2c.I2C):
    def __init__(self, drvname=I2C0, addr=0x48, clk=100000):
        i2c.I2C.__init__(self, drvname, addr, clk)
        self._addr = addr
        try:
            self.start()
        except PeripheralError as e:
            print(e)
        
    def init(self):
        pass
    
    def getTempC(self):
        tempC = self.readTemperature()
        return tempC
        
    def getTempF(self):
        tempF = (self.readTemperature() * 1.8 + 32)
        return tempF
        
    def readTemperature(self):
        data = self.write_read(LM75B_REG_TEMP, 2)
        tempC = (data[0] * 256 + data[1])/32 *0.125

        return tempC