import serial
import time
#port = '/dev/ttyUSB0'
#msr = serial.Serial(port, 9600)

# MSR 605/206 Commands
ESC = '\x1B'
FS = '\x1C'
ACK = '\x1B\x79'
RESET = '\x1B\x61'
READ_ISO = '\x1B\x72'
WRITE_ISO = '\x1B\x77'
COMMUNICATIONS_TEST = '\x1B\x65'
ALL_LED_OFF = '\x1B\x81'
ALL_LED_ON = '\x1B\x82'
GREEN_LED_ON = '\x1B\x83'
YELLOW_LED_ON = '\x1B\x84'
RED_LED_ON = '\x1B\x85'
SENSOR_TEST = '\x1B\x86'
RAM_TEST = '\x1B\x87'
# End MSR 605/206 Commands

class pyMSR:

	def __init__(self, port):
		self.__msr = serial.Serial(port, 9600)
		self.__msr.write(RESET)
		self.__msr.write(COMMUNICATIONS_TEST)
		if (self.__msr.read() != '\x1B'):
			print "could not init"
		if (self.__msr.read() != 'y'):
			print "could not init"
		else: 
			print "MSR Initialized On Port " + port
			self.__msr.write(RESET)

	def reset(self, printinfo=False)
		self.__msr.write(RESET)
		if (printinfo == True):
			print "MSR has been reset"

	def close(self):
		self.__msr.close()

	def __read(self, byte):
		a = self.__msr.read()
		if (a != byte):
			#print "Expected [" + binascii.hexlify(byte) + "] got [" + binascii.hexlify(a) + "]"
			return 0
    		return 1

	def read_until(self, byte):
		b = ""
		d = ""
		while True:
			b = self.__msr.read()
			if (b == byte):
				return d
			d += b

	def allLED(self, printinfo=False)
		self.__msr.write(ALL_LED_ON)
		if (printinfo == True):
			print "All LED's have been turned on"

	def noLED(self, printinfo=False)
		self.__msr.write(ALL_LED_OFF)
		if (printinfo == True):
			print "All LED's have been turned off"


	def getFirmware(self):
		self.__msr.write('\x1B\x76')
		self.__read(ESC)
		time.sleep(.1)
		ver = ""
		while (self.__msr.inWaiting()):
			ver += self.__msr.read()
		print ver

	def getDevice(self):
		self.__msr.write('\x1B\x74')
		self.__read(ESC)
		time.sleep(.1)
		device = ""
		while (self.__msr.inWaiting()):
			device += self.__msr.read()
		if (device[-1:] != 'S'):
			print "Error!"
			return 0
		print device[:-1]
	
	
	def readTrack(self, track=1)
		if (track == 1):
			trackid = '\x01'
		elif (track == 2):
			trackid = '\x02'
		elif (track == 3):
			trackid = '\x03'
		else:
			print "ERROR! Only 3 tracks are availible"
			return ""
		self.__msr.write(READ_ISO)
		if (self.__msr.read() != ESC):
			print "Expected Byte Mismatch"
			return data
		if (self.__msr.read() != 's'):
			print "Expected Byte Mismatch"
			return data
		if (self.__msr.read() == track):
			data = self.read_until(ESC)
		else:
			print "Expected Byte Mismatch"
			return data
		self.__msr.write(RESET)

			
	def readISO(self)
		self.__msr.write(READ_ISO)
		data[]
		if (self.__msr.read() != ESC):
			print "Expected Byte Mismatch"
			return data
		if (self.__msr.read() != 's'):
			print "Expected Byte Mismatch"
			return data
		track = ['\x01', '\x02', '\x03']
		i = 0
		while (i<2):
			if (self.__msr.read() == track[i]):
				data[i] = self.read_until(ESC)
			else:
				print "Expected Byte Mismatch"
				return data
		retval = "Track 1: ".data[0].'\n'."Track 2: ".data[1].'\n'."Track 3: ".data[2]
		return retval
		self.__msr.write(RESET)

