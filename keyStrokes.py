import uinput
import time
import socket

from Queue import Queue
import threading


class Connection:

	def __init__(self,ip,port,keyStream):
		self.soc = socket.socket()
		self.soc.connect((ip,port))
		self.thread = threading.Thread(target = self.recvData, args = (keyStream,))
		self.thread.start()

	def recvData(self,keyStream):
		print "Receiving thread started"
		while True:
			data = self.soc.recv(1024)
			print data
			if not data:
				break
			print data,
			for x in list(data):
				keyStream.put(x)
		self.soc.close()


class HandleKeyStrokes:
	def __init__(self,keyStream):
		self.capLetter = [uinput.KEY_A, uinput.KEY_B, uinput.KEY_C, uinput.KEY_D, uinput.KEY_E, uinput.KEY_F,uinput.KEY_G, uinput.KEY_H, uinput.KEY_I, uinput.KEY_J, uinput.KEY_K, uinput.KEY_L, uinput.KEY_M,uinput.KEY_N, uinput.KEY_O, uinput.KEY_P, uinput.KEY_Q, uinput.KEY_R, uinput.KEY_S, uinput.KEY_T,uinput.KEY_U, uinput.KEY_V, uinput.KEY_W, uinput.KEY_X, uinput.KEY_Y, uinput.KEY_Z]
		#self.smallLetter = []
		#self.keyArray = self.capLetter + self.smallLetter
		self.device = uinput.Device(self.capLetter)
		self.generateKeyInterrupt(keyStream)

	def generateKeyInterrupt(self,keyStream):
		while True:
			key = keyStream.get()
			keyStream.task_done()
			
			key = ord(key) - 65
			print "Key : ",key
			if key > 26 :
				pass
			else:
				key = self.capLetter[key]
				print "Got ",key
				print self.device
				self.device.emit_click(key)





if __name__ == "__main__":
	
	ip = raw_input("Enter ip of pc whose keyboard u want to use : ")
	port = int(raw_input("Enter port number : "))

	keyStream = Queue()
	con = Connection(ip,port,keyStream)

	keyHandler = HandleKeyStrokes(keyStream)
