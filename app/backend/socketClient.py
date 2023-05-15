import socket

# socket AF_INET establish the system we are on, SOCK_STREAM is the two way byte protocol to use
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# socket connects to the port and gets the host name
s.connect((socket.gethostname(), 5743))

while True:
    # recieves the number of bytes (not associated with PORT number)
    msg = s.recv(5746)
    # print the messege to console
    print(msg.decode("utf-8"))