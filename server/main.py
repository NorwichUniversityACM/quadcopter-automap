#!/usr/bin/env python

import Adafruit_BBIO.PWM as PWM
import socket
import threading
import time

changed = True
input_percentage = 0
print "Running..."
killed = False

def comm ():
        TCP_IP = '10.0.0.1'
        TCP_PORT = 666
        BUFFER_SIZE = 20

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((TCP_IP, TCP_PORT))
        s.listen(1)

        conn, addr = s.accept()
        print 'Connection address:', addr
        while 1:
                data = conn.recv(BUFFER_SIZE)
                if not data: break
                print "received data:", data
                if data < 30 and data > -2:
                        gentlepercentage(data)
                        if data == -1:
                                killed = True
                else:
                        print 'not valid input'
                conn.send(data) #echo
        conn.close()
        return

def pwmcontrol ():
        changed = False
        PWM.cleanup()
        start_freq = 300.0
        start_duty = 0.0

        period = 1.0 / start_freq
        minimum = 100.0 * (.001 / period)
        maximum = 100.0 * (.002 / period)

        print "Frequency:" + str(start_freq)
        print "Period:" + str(period)
        print "Minimum:" + str(minimum)
        print "Maximum:" + str(maximum)

        PWM.start("P9_14",start_duty,start_freq)
        PWM.start("P8_13",start_duty,start_freq)
        PWM.start("P9_21",start_duty,start_freq)
        PWM.start("P9_42",start_duty,start_freq)

        print "Start"

        while input_percentage >= 0:
                        duty_cycle = ((0.01*input_percentage) * (maximum - minimum)) + minimum
                        print "Duty Cycle: " + str(duty_cycle)
                        PWM.set_duty_cycle("P8_13",duty_cycle)
                        PWM.set_duty_cycle("P9_14",duty_cycle)
                        PWM.set_duty_cycle("P9_21",duty_cycle)
                        PWM.set_duty_cycle("P9_42",duty_cycle)
                        if changed == True:
                                changed = False
                                print "input_percentage:",input_percentage
                        else:
                                time.sleep(0.1)


        PWM.stop("P9_14")
        PWM.stop("P8_13")
        PWM.stop("P9_21")
        PWM.stop("P9_42")
        PWM.cleanup()
        quit()
        return

def gentlepercentage(goalpercentage):
        while input_percentage < goalpercentage + 0.4:
                input_percentage = input_percentage + 0.4
                changed = True
                time.sleep(0.5)

        while input_percentage > goalpercentage:
                input_percentage = input_percentage - 0.4
                changed = True
                time.sleep(0.5)
        if input_percentage != goalpercentage:
                input_percentage = goalpercentage
                changed = True
        return

commthread = comm()
pwncontrolthread = pwmcontrol()
commthread.start()
pwncontrolthread.start()

while killed == False:
        commthread.join()#if connection closes
        input_percentage = 0
        commthread.start()

print "Program Done"