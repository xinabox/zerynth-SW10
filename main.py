import streams
import sw10

streams.serial()

SW10 = sw10.SW10(I2C0)
SW10.init()

while True:
    tempC = SW10.getTempC()
    tempF = SW10.getTempF()
    
    print('Temperature: ',tempC,' C')
    print('Temperature: ',tempF,' F')
    
    sleep(2000)