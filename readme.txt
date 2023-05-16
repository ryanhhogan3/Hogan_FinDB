################
# FLASK APP FOR FINANCE 

################
# LIBRARIES USED:
# SYSTEM
# FLASK
#   flask-navigation
# SOCKETS

#  DATA & DATA MANAGEMENT
#   yfinance
#   pandas


Communication Contract
Ryan Hogan
CS361

Requesting data from my microservice:

Establish a client file in python
Use the socket library that comes with python
Establish a socket connection using:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.AF_INET establishes we are on the same system
socket.SOCK_STREAM provides two way byte streams allowing us to communicate using sockets
Connect the socket to the proper port
  s.connect((socket.gethostname(), 5743))
Get host name get the host of the port
Establish a while true loop to receive streaming data
Create a variable msg to receive from the port
Print the message to the console.
Process for the client is complete
The MSG variable is an EXAMPLE of the REQUEST
The print statement is an EXAMPLE of the RECIEVE data requirement since it receives data and prints it to the console. 
while True:
    msg = s.recv(5746)
    print(msg.decode("utf-8"))
    
    
# UML DIAGRAM
![Alt text](https://github.com/ryanhhogan3/Hogan_FinDB/blob/master/images/UML%20Diagrma%20Assignment%208.png)
    
