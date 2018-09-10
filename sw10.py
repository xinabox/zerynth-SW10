"""
.. module:: SW10

***************
 SW10 Module
***************

This is a Module for the `SW10 xChip <https://wiki.xinabox.cc/SW10_-_Temperature_Sensor>`_ ambient temperature sensor.
The board is based off the LM75 temperature-to-digital converter manufactured by NXP Semiconductors.
The board uses I2C for communication.

Data Sheets:

-  `LM75 <https://www.nxp.com/docs/en/data-sheet/LM75B.pdf>`_

	"""

import i2c

LM75B_REG_CONF = 0x01
LM75B_REG_TEMP = 0x00
LM75B_REG_TOS = 0x03
LM75B_REG_THYST = 0x02

class SW10(i2c.I2C):
	'''

===============
SW10 class
===============

.. class:: SW10(self, drvname, addr=0x48, clk=100000)

		Create an instance of the SW10 class.

		:param drvname: I2C Bus used '( I2C0, ... )'
		:param addr: Slave address, default 0x48
		:param clk: Clock speed, default 100kHz

	'''

	def __init__(self, drvname = I2C0, addr = 0x48, clk = 100000):
		i2c.I2C.__init__(self, drvname, addr, clk)
		self._addr = addr
		try:
			self.start()
		except PeripheralError as e:
			print(e)

	def init(self):
		'''
.. method:: init(self)

		Empty function. Only used to conform with other modules.
		No configuartion required for LM75.

		'''
		return True

	def getTempC(self):
		'''
.. method:: getTempC(self)

		Returns the ambient temerature in degree celcius

		'''
		tempC = self.readTemperature()
		return tempC

	def getTempF(self):
		'''
.. method:: getTempF(self)

		Returns the ambient temerature in degree fahrenheit

		'''
		tempF = (self.readTemperature() * 1.8 + 32)
		return tempF

	def readTemperature(self):
		'''
.. method:: readTemperature(self)

		Reads the raw temperature from LM75.

		returns the raw temperature.

		'''
		data = self.write_read(LM75B_REG_TEMP, 2)
		tempC = (data[0] * 256 + data[1])/32 *0.125

		return tempC