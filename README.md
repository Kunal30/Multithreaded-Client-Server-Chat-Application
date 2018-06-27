# Multithreaded-Client-Server-Chat-Application
Network Connection Mechanism:

A network connection is initiated by a client program when it creates a socket for the communication with the server. To create the socket in Python, the python socket library is used for establishing a TCP Connection. After that, we use the connect(host,port) function of that socket object to connect to the server. At this stage, the server must be started on the machine having the specified address and listening for connections on a specific port number. The server uses a specific port dedicated only to listening for connection requests from clients. So, its specific port is dedicated only to listening for new connection requests. The server side socket associated with specific port is called server socket. Here after defining a TCP connection, we need to bind in the host IP and the port number, to define the socket on the server side, so that multiple clients could connect to it. When a connection request arrives on this socket from the client side, the client and the server establish a connection. A new thread is started by the server to manage this client’s requests.

Thus, to summarize the above description sequentially, the connection is established as follows:

When the server receives a connection request on its specific server port, it creates a new thread for each client’s request and binds a port number to it.

It sends the new client’s information to all existing connected clients.

The server goes on now by listening on the port:

It waits for any new incoming connection requests on its specific port.

It reads and writes messages on established connection with the accepted client. The server communicates with the client by reading from and writing to the port. The message incoming from the client is used to find out the destination client(s) and then the message is forwarded to the requested client. Also, if other connection requests arrive, the server accepts them and processes them through multithreading and creates a separate thread for every new connection. Thus, at any instant, the server must be able to communicate simultaneously with many clients and to wait on the same time for incoming requests on its specific server port. The communication with each client is done via the client and server sockets. We’ve used stream communication protocol. The stream communication protocol is known as TCP (transfer control protocol). TCP is a connection -oriented protocol. In order to communicate over the TCP, a connection must first be established between the two sockets. While one of the sockets listens for a connection request (server), the other asks for a connection (client). Once the two sockets are connected, they can be used to transmit and/or to receive data. When we say "two sockets are connected" we mean the fact that the server accepted a connection. 
