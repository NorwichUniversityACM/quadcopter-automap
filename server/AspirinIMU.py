from MPU6000 import MPU6000
import time
import threading
import gc
import operator
class AspirinIMU:
	HMC5883_SLAVE_ADDRESS_W = 0x3C
	HMC5883_SLAVE_ADDRESS_R = 0x3D
	
	
	def init(self):
		self.CUR_ROT = (0,0,0)
		self.mpu = MPU6000()

		self.GYRO_BIAS = (0.027,-0.036,0.024)


		mpu = self.mpu
	
		mpu.open()
		mpu.writeReg(MPU6000.R_PWR_MGMT_1, 0x80)
		time.sleep(1)	
		if mpu.readReg(MPU6000.R_WHOAMI) != 0x68:
			print "Error connecting to MPU"
			return False

		mpu.writeReg(MPU6000.R_PWR_MGMT_1, 0x3)
		mpu.writeReg(MPU6000.R_INT_ENABLE, 0x1)
		mpu.writeReg(MPU6000.R_CONFIG, 0x3)
		mpu.writeReg(MPU6000.R_SMPRT_DIV, 0x10) #originally 0x4
		mpu.writeReg(MPU6000.R_GYRO_CONFIG, 0x0) #x18
		mpu.writeReg(MPU6000.R_ACCEL_CONFIG, 0x0)
		mpu.writeReg(MPU6000.R_INT_PIN_CFG, 0x10)	
	
		mpu.writeReg(MPU6000.R_USER_CTRL, 0b01000000)	
		mpu.writeReg(MPU6000.R_FIFO_EN, 0b01111000)
		
	def startPolling(self):
		self.polling = True
		self.fifo_poll_thread = threading.Thread(target=self.pollFifo, args=())
		self.fifo_poll_thread.daemon = True
		self.fifo_poll_thread.start()				
	
	def stopPolling(self):
		self.polling = False
		self.fifo_poll_thread.join()

	def getTemp(self):
		mpu = self.mpu
		temph = mpu.readReg(MPU6000.R_TEMP_OUT_H)
		templ = mpu.readReg(MPU6000.R_TEMP_OUT_L)
		temp = MPU6000.smashhl(temph, templ) 
		return (int(temp) / 340.0) + 36.53
	
	def getGyro(self):
		mpu = self.mpu
		gyX = MPU6000.smashhl(mpu.readReg(MPU6000.R_GYRO_XOUT_H), mpu.readReg(MPU6000.R_GYRO_XOUT_L))
		gyY = MPU6000.smashhl(mpu.readReg(MPU6000.R_GYRO_YOUT_H), mpu.readReg(MPU6000.R_GYRO_YOUT_L))	
		gyZ = MPU6000.smashhl(mpu.readReg(MPU6000.R_GYRO_ZOUT_H), mpu.readReg(MPU6000.R_GYRO_ZOUT_L))
		raw_gyro = (gyX, gyY, gyZ)
		gyro = tuple([d / 131.0 for d in raw_gyro])
		return gyro
		
	def getAccel(self):
		mpu = self.mpu
		aX = MPU6000.smashhl(mpu.readReg(MPU6000.R_ACCEL_XOUT_H), mpu.readReg(MPU6000.R_ACCEL_XOUT_L))
		aY = MPU6000.smashhl(mpu.readReg(MPU6000.R_ACCEL_YOUT_H), mpu.readReg(MPU6000.R_ACCEL_YOUT_L))	
		aZ = MPU6000.smashhl(mpu.readReg(MPU6000.R_ACCEL_ZOUT_H), mpu.readReg(MPU6000.R_ACCEL_ZOUT_L))
		raw_accel = (aX, aY, aZ)
		accel = tuple([d / 16384.0 for d in raw_accel])
		return accel

	def getFifoCount(self):	
		mpu = self.mpu
		fifo = MPU6000.smashhl(mpu.readRegU(MPU6000.R_FIFO_COUNT_H), mpu.readRegU(MPU6000.R_FIFO_COUNT_L))
		return fifo
	
	def getFifo(self):
		mpu = self.mpu
		return mpu.readReg(MPU6000.R_FIFO_R_W)
	def resetFifo(self):
		mpu = self.mpu
		mpu.writeReg(MPU6000.R_USER_CTRL, 0b01000100)

	def pollFifo(self):
		while self.polling:
		        count = self.getFifoCount()
			
		        while count > 0:
               			if(count % 12 != 0):
                        		self.resetFifo()
                        		break
				
                		aX = MPU6000.smashhl(self.getFifo(), self.getFifo())
				aY = MPU6000.smashhl(self.getFifo(), self.getFifo())
				aZ = MPU6000.smashhl(self.getFifo(), self.getFifo())
                		gX = MPU6000.smashhl(self.getFifo(), self.getFifo())
                		gY = MPU6000.smashhl(self.getFifo(), self.getFifo())
                		gZ = MPU6000.smashhl(self.getFifo(), self.getFifo())
				raw_accel =  aX,aY,aZ
				raw_gyro = gX,gY,gZ
				
				
				gyro = tuple([d / (131.0 * 58.82) for d in raw_gyro])
				accel = tuple([d / 16384.0 for d in raw_accel])
				
				#self.GYRO_BIAS = tuple(map(operator.div,tuple(map(operator.add, self.GYRO_BIAS, gyro)), (2,2,2)))
				
				gyro = tuple(map(operator.add, self.CUR_ROT, gyro))	
				self.CUR_ROT = tuple(map(operator.add, gyro, self.GYRO_BIAS))	
				count = self.getFifoCount()
        		time.sleep(.01)
	def getCurrentRotation(self):
		return self.CUR_ROT
	def getGyroBias(self):
		return self.GYRO_BIAS
	def setGyroBias(self, gyro_bias):
		self.GYRO_BIAS = gyro_bias
