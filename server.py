import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

players = {}


def receiveData(data, address):
    DataType, data = data.decode('utf-8').split(',', 1)
    playerId = address[1]

    if DataType == "connect":
        players[playerId] = {"address": address, "x": 0, "y": 0}


    elif DataType == "position":
        x, y = map(int, data.split(','))
        if playerId in players:
            players[playerId]["x"] = x
            players[playerId]["y"] = y
        
    elif DataType == "disconnect":
        if playerId in players:
            del players[playerId]

            

def sendData():
    playerData = ';'.join([f"{pid},{p['x']},{p['y']}" for pid, p in players.items()])
    for player in players.values():
        server.sendto(playerData.encode('utf-8'), player["address"])

def startServer():
    while True:
        try:
            data, address = server.recvfrom(1024)
            threading.Thread(target=receiveData, args=(data, address)).start()
            sendData()
        except Exception as e:
            print(f"Error: {e}")

startServer()
