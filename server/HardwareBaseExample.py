from HardwareBase import HardwareBase
import time
h = HardwareBase()
h.start()
h.setMotorSpeed(0, 10)
time.sleep(2)
h.setMotorSpeed(1, 10)
time.sleep(2)
h.setMotorSpeed(2, 10)
time.sleep(2)
h.setMotorSpeed(3, 10)
time.sleep(2)  
h.setMotorSpeed(0, 15)
h.setMotorSpeed(1, 15)
h.setMotorSpeed(2, 15)
h.setMotorSpeed(3, 15)
time.sleep(5)
percent = 15.0
while(percent > 4):
        percent = percent - .3
        time.sleep(.3) 
        h.setMotorSpeed(0, percent)
        h.setMotorSpeed(1, percent)
        h.setMotorSpeed(2, percent)
        h.setMotorSpeed(3, percent)

