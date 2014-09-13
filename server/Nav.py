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
		
	def rollratio():
		#Motor 2 and 4
	
	def heightPID():
		#allMotors
	
	def yawPID():
		#allMotors
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
			setMotors()
			