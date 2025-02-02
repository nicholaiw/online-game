import socket
import random
import threading
import concurrent.futures

HOST = '127.0.0.1'
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

clients = {}
rooms = {}

def createRoom(clientID, name):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    while True:
        roomCode = ''.join(random.choices(characters, k=6))
        if roomCode not in rooms:
            rooms[roomCode] = {
                "players": {
                    clientID: {
                        "name": name,
                        "positionX": 0,
                        "positionY": 0
                    }
                }
            }
            break     

clientsLock = threading.Lock()
roomsLock = threading.Lock()

def receiveData(data, address):
    data = data.decode('utf-8')
    clientID, data = data.split(';', 1)

    with clientsLock:
        if data.startswith("connect"):
            clients[clientID] = address
        elif data.startswith("disconnect"):
            if clientID in clients:
                del clients[clientID]

    with roomsLock:
        if data.startswith("disconnect"):
            for roomCode, roomInfo in list(rooms.items()):
                if clientID in roomInfo["players"]:
                    del roomInfo["players"][clientID]
                    if not roomInfo["players"]:
                        del rooms[roomCode]
                    break

        elif data.startswith("createGame"):
            _, name = data.split(';', 1)
            createRoom(clientID, name)

        elif data.startswith("joinGame"):
            _, roomCode = data.split(';', 1)
            if roomCode in rooms:
                rooms[roomCode]["players"][clientID] = {
                    "name": "Player",
                    "positionX": 0,
                    "positionY": 0
                }


def sendData():
    with roomsLock:
        for roomCode, roomInfo in list(rooms.items()):
            playerData = f"roomUpdate;{roomCode};" + ';'.join([
                f"{clientID},{player['name']},{player['positionX']},{player['positionY']}"
                for clientID, player in list(roomInfo["players"].items())
            ])
            for clientID in list(roomInfo["players"].keys()):
                if clientID in clients:
                    server.sendto(playerData.encode('utf-8'), clients[clientID])



def updateSendData():
    while True:
        sendData()



def startServer():
    updateThread = threading.Thread(target=updateSendData)
    updateThread.start()

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        while True:
            try:
                data, address = server.recvfrom(1024)
                executor.submit(receiveData, data, address)
            except Exception as e:
                print(f"Error: {e}")

startServer()
