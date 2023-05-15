import socket
import datetime as dt
import time 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5743))
s.listen(10)



while True:
    today = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes(str(today), "utf-8"))
    while True:
        time.sleep(1)
        today = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        clientsocket.send(bytes(str(today), "utf-8"))
