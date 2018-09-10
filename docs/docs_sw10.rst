.. module:: SW10

***************
 SW10 Module
***************

This is a Module for the `SW10 xChip <https://wiki.xinabox.cc/SW10_-_Temperature_Sensor>`_ ambient temperature sensor.
The board is based off the LM75 temperature-to-digital converter manufactured by NXP Semiconductors.
The board uses I2C for communication.

Data Sheets:

-  `LM75 <https://www.nxp.com/docs/en/data-sheet/LM75B.pdf>`_

        
===============
SW10 class
===============

.. class:: SW10(self, drvname, addr=0x48, clk=100000)

                Create an instance of the SW10 class.

                :param drvname: I2C Bus used '( I2C0, ... )'
                :param addr: Slave address, default 0x48
                :param clk: Clock speed, default 100kHz

        
.. method:: init(self)

                Empty function. Only used to conform with other modules.
                No configuartion required for LM75.

                
.. method:: getTempC(self)

                Returns the ambient temerature in degree celcius

                
.. method:: getTempF(self)

                Returns the ambient temerature in degree fahrenheit

                
.. method:: readTemperature(self)

                Reads the raw temperature from LM75.

                returns the raw temperature.

                
