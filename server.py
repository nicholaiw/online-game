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

clientsLock = threading.Lock()
roomsLock = threading.Lock()

def createRoom(clientID, name):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    while True:
        roomCode = ''.join(random.choices(characters, k=4))
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


def receiveData(data, address):

    data = data.decode('utf-8')
    print(data)

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
            _, roomCode, name = data.split(';', 2)

            if roomCode in rooms:
                rooms[roomCode]["players"][clientID] = {
                    "name": name,
                    "positionX": 0,
                    "positionY": 0
                }

        elif data.startswith("position"):
            _, positionData = data.split(';', 1)
            positionX, positionY = positionData.split(',', 1)
            positionX = int(positionX)
            positionY = int(positionY)

            print(f"client:{clientID}   x-cords:{positionX}    y-cords_{positionY}")

            for roomCode, roomInfo in rooms.items():
                if clientID in roomInfo["players"]:
                    print('updated player position ')
                    roomInfo["players"][clientID]["positionX"] = positionX
                    roomInfo["players"][clientID]["positionY"] = positionY
                    break



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
