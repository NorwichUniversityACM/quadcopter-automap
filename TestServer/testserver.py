from PySide import QtCore, QtGui
import time
import socket
import threading

changed = True
input_percentage = 0
print "Running..."
killed = False

def comm ():
        TCP_IP = '127.0.0.1'
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
                if int(data) < 30 and int(data) > -2:
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
        start_freq = 300.0
        start_duty = 0.0

        period = 1.0 / start_freq
        minimum = 100.0 * (.001 / period)
        maximum = 100.0 * (.002 / period)

        print "Frequency:" + str(start_freq)
        print "Period:" + str(period)
        print "Minimum:" + str(minimum)
        print "Maximum:" + str(maximum)

        print "Start"

        while input_percentage >= 0:
                        duty_cycle = ((0.01*input_percentage) * (maximum - minimum)) + minimum
                        print "Duty Cycle: " + str(duty_cycle)
                        if changed == True:
                                changed = False
                                print "input_percentage:",input_percentage
                        else:
                                time.sleep(0.1)


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

commthread = threading.Thread(target=comm, args = ())
pwmcontrolthread = threading.Thread(target=pwmcontrol, args = ())
# guithread = threading.Thread(target=gui, args = ())
commthread.daemon = True
pwmcontrolthread.daemon = True
# guithread.daeomon = True
# guithread.start()
commthread.start()
pwncontrolthread.start()



# class Ui_Dialog(object):
    # def setupUi(self, Dialog):
        # Dialog.setObjectName("M")
        # Dialog.resize(400, 133)
        # self.progressBar = QtGui.QProgressBar(Dialog)
        # self.progressBar.setGeometry(QtCore.QRect(20, 10, 361, 23))
        # self.progressBar.setProperty("value", 24)
        # self.progressBar.setObjectName("progressBar")
        # self.pushButton = QtGui.QPushButton(Dialog)
        # self.pushButton.setGeometry(QtCore.QRect(20, 40, 361, 61))
        # self.pushButton.setObjectName("pushButton")

        # self.worker = Worker()
        # self.worker.updateProgress.connect(self.setProgress)

        # self.retranslateUi(Dialog)
        # QtCore.QMetaObject.connectSlotsByName(Dialog)

        # self.progressBar.minimum = 1
        # self.progressBar.maximum = 100

    # def retranslateUi(self, Dialog):
        # Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        # self.pushButton.setText(QtGui.QApplication.translate("Dialog", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        # self.progressBar.setValue(0)
        # self.pushButton.clicked.connect(self.worker.start)

    # def setProgress(self, progress):
        # self.progressBar.setValue(progress)

# #Inherit from QThread
# class Worker(QtCore.QThread):

    # #This is the signal that will be emitted during the processing.
    # #By including int as an argument, it lets the signal know to expect
    # #an integer argument when emitting.
    # updateProgress = QtCore.Signal(int)

    # #You can do any extra things in this init you need, but for this example
    # #nothing else needs to be done expect call the super's init
    # def __init__(self):
        # QtCore.QThread.__init__(self)

    # #A QThread is run by calling it's start() function, which calls this run()
    # #function in it's own "thread". 
    # def run(self):
        # #Notice this is the same thing you were doing in your progress() function
        # for i in range(1, 101):
            # #Emit the signal so it can be received on the UI side.
            # self.updateProgress.emit(i)
            # time.sleep(0.1)

# def gui()
	# if __name__ == "__main__":
		# import sys
		# app = QtGui.QApplication(sys.argv)
		# Dialog = QtGui.QDialog()
		# ui = Ui_Dialog()
		# ui.setupUi(Dialog)
		# Dialog.show()
		# sys.exit(app.exec_())
	
while killed == False:
        commthread.join()#if connection closes
        input_percentage = 0
        commthread.start()

print "Program Done"