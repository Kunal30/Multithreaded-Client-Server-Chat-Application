import socket #importing necessary modules
import select
import sys       #used for reading and writing and for exiting the program

host = '10.172.17.01'               #declaration of host and port
port = 12341

##########################################
def inpu():                                 #displaying the prompt
    sys.stdout.write(">>")
    sys.stdout.flush()
##########################################


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        #creating a tcp connection
s.settimeout(100)                           

s.connect((host,port))             #connecting to server
print s.recv(1024),
nick_name = raw_input()            
s.send(nick_name)                 #sending nickname to server
#friend = raw_input()
#s.send(friend)
print "Message format\n"            #specifing the format of message
print "@sender @sender2:Your message\n"
print "press ctrl+c for closing\n"
print "-------------------------------------------------\n"
#print s.recv(1024)
print "-------------------------------------------------\n"
inpu()                           #displaying the prompt
while 1:
				sock_list = [sys.stdin, s]      #creating a list consisting of socket and std input
				try:
					read_sockets, write_sockets, error_sockets = select.select(sock_list,[],[])  #reading socket for incoming messages 
				except:																			# and user input
					print "Successfully disconnected from chat server"	
					sys.exit()
				for each_sock in read_sockets:
				    if each_sock == s:
				        data = each_sock.recv(1024)                   #sending the message to the server along with the receivers
				        if not data:                                  
				            print "\nDisconnected from chat server"   
				            sys.exit()
				        else:
				            sys.stdout.write(data)                  #displaying the incomming message on the screen
				            inpu()
				    else:
				        message = sys.stdin.readline()             #reading the user input and sending the message to server
				        s.send(message)
				        inpu()







