import HardwareBase as hardware
class navigation:
	#Variables
	def init():
		self.targetheight = 0
		self.targetpitch = 0
		self.targetroll = 0
		self.height = hardware.getHeight()
		self.pitch = hardware.getPitch()
		self.roll = hardware.getRoll()
		self.yaw = hardware.getYaw()
		#Motor1 = front
		#Motor2 = right
		#Motor3 = back
		#Motor4 = left
		motor1 = hardware.getMotorSpeed(1)
		motor2 = hardware.getMotorSpeed(2)
		motor3 = hardware.getMotorSpeed(3)
		motor4 = hardware.getMotorSpeed(4)
		
	def pitchratio():
		#Motor 1 and 3
		pK = 1
		pI = 1
		pD = 1
		
	def rollratio():
		#Motor 2 and 4
		pK = 1
		pI = 1
		pD = 1
	
	def heightPID():
		#allMotors
		pK = 1
		pI = 1
		pD = 1
		#P
		distancefromtarget = self.targetheight - self.height
		motor1 = motor1 - (distancefromtarget * pK)
		motor2 = motor2 - (distancefromtarget * pK)
		motor3 = motor3 - (distancefromtarget * pK)
		motor4 = motor4 - (distancefromtarget * pK)
		#I
		motor1 = motor1 - (self.heightld - distancefromtarget) * pI
		motor2 = motor2 - (self.heightld - distancefromtarget) * pI
		motor3 = motor3 - (self.heightld - distancefromtarget) * pI
		motor4 = motor4 - (self.heightld - distancefromtarget) * pI
		self.heightld = distancefromtarget # last distance
		#D
		
		
	
	def yawPID():
		#allMotors
		pK = 1
		pI = 1
		pD = 1
		
	def checkMotors():
		if motor1 < 0:
			motor1 = 0
		else if motor1 > 100:
			motor1 = 100
		if motor2 < 0:
			motor2 = 0
		else if motor2 > 100:
			motor2 = 100
		if motor3 < 0:
			motor3 = 0
		else if motor3 > 100:
			motor3 = 100
		if motor4 < 0:
			motor4 = 0
		else if motor4 > 100:
			motor4 = 100
		
	def setMotors():
		hardware.setMotorSpeed(1,motor1)
		hardware.setMotorSpeed(2,motor2)
		hardware.setMotorSpeed(3,motor3)
		hardware.setMotorSpeed(4,motor4)
		
	def start():
		while True:
			#Runtime loop
			pitchratio()
			rollratio()
			heightPID()
			yawPID()
			checkMotors()
			setMotors()
			
