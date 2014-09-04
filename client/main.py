import socket
import Queue
import threading

TCP_IP = '10.0.0.1'
TCP_PORT = 666
BUFFER_SIZE = 1024
#Constants

s = None
data_queue = Queue.Queue()

receiving = True
sending = True
active = True

send_per = 0

def connect(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
def close():
        s.close()
def send(message):
        s.send(message)
def receive():
        data_queue.put(s.recv(BUFFER_SIZE))
def receive_loop():
        while receiving:
                receive()
                time.sleep(0.5)
def send_loop():
        while sending:
                send(str(send_per))
                time.sleep(.01)
def print_received():
        while active:
                while not data_queue.empty():
                        print data_queue.get()
        time.sleep(.01)
if __name__ == "__main__":
        
        connect(TCP_IP, TCP_PORT)
        sending = True
        receiving = True
        active = True   
                  
        rec_d = threading.Thread(target=receive_loop, args = ())
        rec_d.daemon = True
        rec_d.start()   
        send_d = threading.Thread(target=send_loop, args = ())
        send_d.daemon = True
        send_d.start()
        print_d = threading.Thread(target=print_received, args = ())
        print_d.daemon = True
        print_d.start()
                
        while send_per >= 0:
                send_per = input("#:")
        
        sending = False
        receiving = False
        active = False

        rec_d.join()
        send_d.join()
        print_d.join()
        close()
        
        print "Failure...Connection closed/timeout/etc"                 

