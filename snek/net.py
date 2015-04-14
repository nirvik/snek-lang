import socket
import pickle
import threading 
import time 

class Pipes(socket.socket):
        
    def __init__(self,event,host,port):
        super(Pipes,self).__init__(socket.AF_INET,socket.SOCK_DGRAM)
        self.bind((host,port))
        self.settimeout(100)
        self.event = event 
        self.host = host
        self.port = port 
        print 'Created socket'

    def negotiate(self):
        self.connect((self.host,self.port))
        return True
    
    def sendMessage(self,dest_host, dest_port):
        print 'Establishing Connection'
        self.sendto(self.event,(dest_host,dest_port))

    def submitReactor(self,recv_buffer=4096,delim='\n'):
        buffer = ''
        while True:
            conn,addr = self.recvfrom(recv_buffer)
            if conn:
                buffer += conn
                print buffer 
            else:
                break
        print ' Received Connection and says : ' + buffer

    def receive(self):
        print 'Waiting.. To receive'
        t = threading.Thread(target = self.submitReactor , args = ())
        t.daemon = False 
        t.start()

    def __del__(self):
        self.close()
        print 'sock closed'


