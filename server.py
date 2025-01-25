import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

clients = {}
rooms = {}


def receiveData(Data, address):
    DataType, data, clientID = Data.decode('utf-8').split(';', 2)

    if DataType == "connect":
        clients[clientID] = address
    elif DataType == "disconnect":
        del clients[clientID]


def sendData():
    playerData = ';'.join([f"{pid},{p['x']},{p['y']}" for pid, p in rooms.items()])
    for client in clients.values():
        server.sendto(playerData.encode('utf-8'), client)


def startServer():
    while True:
        try:
            data, address = server.recvfrom(1024)
            threading.Thread(target=receiveData, args=(data, address)).start()
            sendData()
        except Exception as e:
            print(f"Error: {e}")

startServer()
