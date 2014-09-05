	
import Adafruit_BBIO.PWM as PWM
class HardwareBase:
        MOTORS = {0: "P9_14", 1:"P8_13", 2:"P9_21", 3:"P9_42"}
        FREQUENCY = 300.0
        PERIOD = 1.0 / FREQUENCY
        MINIMUM_DUTY_CYCLE = 100.0 * (.001 / PERIOD)
        MAXIMUM_DUTY_CYCLE = 100.0 * (.002 / PERIOD)

        def __init__(self):
                self.curr_motor_speed = {0:0,1:0,2:0,3:0}
        def start(self):
                for motor in HardwareBase.MOTORS:
                        PWM.start(HardwareBase.MOTORS[motor],HardwareBase.MINIMU
M_DUTY_CYCLE, HardwareBase.FREQUENCY)

        def stop(self):
                for motor in HardwareBase.MOTORS:
                        PWM.stop(HardwareBase.MOTORS[motor])

        def percent_to_duty(self,percent):
                return ((0.01*percent) * (HardwareBase.MAXIMUM_DUTY_CYCLE - Hard
wareBase.MINIMUM_DUTY_CYCLE)) + HardwareBase.MINIMUM_DUTY_CYCLE
        def getMotorSpeed(self,motor_num):
                return self.curr_motor_speed[motor_num]
        def setMotorSpeed(self,motor_num, percent):
                if percent >= 100:
                        percent = 99
                elif percent < 0:
                        percent = 0
                self.curr_motor_speed[motor_num] = percent
                PWM.set_duty_cycle(HardwareBase.MOTORS[motor_num], self.percent_
to_duty(percent))
        def getSonarDistance(self,sonar_num):
                return 0
        def getPitch(self):
                return 0
        def getRoll(self):
                return 0
        def getYaw(self):
                return 0

