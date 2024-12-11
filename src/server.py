import socket
import threading
HOST = '127.0.0.1'
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

rooms = {}
clients = {}
players = {}


room = 3
player = 3539


def receiveMessage(data, address):
    messageType, content = data.decode('utf-8').split(',', 1)
    playerId = address[1]

    if messageType == "connect":
        rooms[room][player] = {"address": address, "x": 0, "y": 0}


    elif messageType == "position":
        x, y = map(int, content.split(','))
        if playerId in players:
            players[playerId]["x"] = x
            players[playerId]["y"] = y
        
    elif messageType == "disconnect":
        if playerId in players:
            del players[playerId]

            

def sendMessage():
    playerData = ';'.join([f"{pid},{p['x']},{p['y']}" for pid, p in players.items()])
    for player in players.values():

        server.sendto(playerData.encode('utf-8'), player["address"])
    


def startServer():
    while True:
        try:
            data, address = server.recvfrom(1024)
            threading.Thread(target=receiveMessage, args=(data, address)).start()
            sendMessage()
        except Exception as e:
            print(f"Error: {e}")

startServer()