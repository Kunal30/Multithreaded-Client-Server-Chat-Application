import socket      #importing necessary modules
import thread
import string

 
#########
# Below function alert all other connected clients if a new connects to the server.
# It takes nickname of the connected client and according sends the message to all other connected clients that a new client is available
########		

def send_message_all(nickname):
	for soc in clients_conn:
		if soc!=nickname:
			clients_conn[soc].send("\r\t\t"+nickname.upper()+" is online now\n")
	for z in clients_conn:
		if z!=nickname:
			clients_conn[nickname].send("\r\t\t"+z.upper()+" is online now\n")	
					
		
#########
# Below fucntion takes the message the send to by the client to the server which is to be forwarded to specific clients
# and this fuction extracts the receiver and convert it into a list and send it back along with the actual message
#########
def getreceiver(data):
		l=string.split(data,":")
		a=string.split(l[0]," ")
		for x in range(len(a)):
			a[x]=a[x].replace("@","")
		for k in range(len(a)):
			a[k]=a[k].lower()	
		return (a,l[1])


###############
# This function is one on which thread runs. It takes of sending and receiving of messages of client and forwarding it 
# to other clients mentioned in the user's message
##################
def clientthread(conn):
		print "connected by",addr
		conn.send("Specify a nick name:")  #asking the user his nickname
		nick = conn.recv(1024)
		nick=nick.lower()
		clients[str(addr)]=nick        #adding an entry to store the nickname
		clients_conn[nick]=conn        #adding an entry to store the connection corresponding to nickname
		print clients
		print clients_conn
		send_message_all(nick)        #alerting all users about the new connected client
		while 1:
			try:
				data=conn.recv(1024)   #receving message
				a,b=getreceiver(data)   #extracting the receivers from the message
				j=conn.getpeername()
			except:
				for v in clients_conn:
  					if v!=clients[str(j)]:
  						clients_conn[v].send("\r\t\t"+clients[str(j)]+" is offline now\n")  #handling the case when a user disconnects and
  				clients_conn.pop(clients[str(j)])                                           # notifying other clients
  				clients.pop(str(j))
  				print "--------------------------"
  				print clients_conn
  				print clients
  				print "------------------------------"
  				conn.close()
  				continue
			#print a,b
			#print nick
			for f in range(0,len(a)):	
				clients_conn[a[f]].send("\r"+nick+":"+b)	#sending incomming message to mentionded receivers







host = '10.42.0.222'               #declaration of port and hostname
port = 12341

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #creating a TCP socket
s.bind((host, port))                                   #binding the hostname and port to socket created
s.listen(5)                #listening to atmax 5 connection including server
clients={} #add:nickname
clients_conn={}  #nickname:conn


print "server up and running\n"

for i in range(5):
	conn, addr = s.accept()         #accepting new connection
	try:
		thread.start_new_thread(clientthread,(conn,)) #creating a new thread for the new client
  	except:
  		for v in clients_conn:                         #handling if the thread fails
  			if v!=clients[str(conn.getpeername())]:
  				clients_conn[v].send(clients[str(conn.getpeername())]+" is offline now")
  		clients_conn.pop(clients[str(conn.getpeername())])
  		clients.pop(str(conn.getpeername()))
  		conn.close()
s.close()                 #closing the connection
  
  
  
  
  
  
  
  
  
  
  
  
  
