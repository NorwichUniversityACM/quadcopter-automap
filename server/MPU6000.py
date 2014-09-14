import Adafruit_BBIO.SPI as SPI
class MPU6000:
	spi = None
	RREG = 0x80
	WREG = 0x00
	REGMASK = 0x7F

	R_SELF_TEST_X = 0x0D
	R_SELF_TEST_Y = 0x0E
	R_SELF_TEST_Z = 0x0F
	R_SELF_TEST_A = 0x10

	R_CONFIG = 0x1A
	R_GYRO_CONFIG = 0x1B
	R_ACCEL_CONFIG = 0x1C
	R_FIFO_EN = 0x23
	
	R_ACCEL_XOUT_H = 0x3B
	R_ACCEL_XOUT_L = 0x3C
	R_ACCEL_YOUT_H = 0x3D
	R_ACCEL_YOUT_L = 0x3E
	R_ACCEL_ZOUT_H = 0x3F
	R_ACCEL_ZOUT_L = 0x40

	R_TEMP_OUT_H = 0x41
	R_TEMP_OUT_L = 0x42

	R_GYRO_XOUT_H = 0x43
	R_GYRO_XOUT_L = 0x44
	R_GYRO_YOUT_H = 0x45
	R_GYRO_YOUT_L = 0x46
	R_GYRO_ZOUT_H = 0x47
	R_GYRO_ZOUT_L = 0x48

	R_EXT_SENS_DATA_00 = 0x49
	R_EXT_SENS_DATA_23 = 0x60	

	R_USER_CTRL = 0x6A
	R_PWR_MGMT_1 = 0x6B
	R_FIFO_COUNT_H = 0x72
	R_FIFO_COUNT_L = 0x73
	R_FIFO = 0x74
	R_WHOAMI = 0x75
	
	def __init__(self):
	def smashhl(h , l):
		return (h << 8) + l
		
	def open(self):
		spi = SPI(0, 0)
		spi.msh=1000000	
		spi.bpw = 8
		spi.threewire = False
		spi.lsbfirst = False
		spi.mode = 1
		spi.cshigh = False
		spi.open(0, 0)
	def close(self):
		spi.close()
	def writeReg(self, reg, data):
		spi.xfer2([MPU6000.WREG+(reg & REGMASK),data]);
	def readReg(self, reg):
		d = spi.xfer2([MPU6000.RREG+(reg & REGMASK)]);
		return d 
	def initialize(self):
	

