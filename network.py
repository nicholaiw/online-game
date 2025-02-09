import socket
import threading
import uuid

class Network:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client.bind(('', 0))
        self.clientID = str(uuid.uuid4())
        self.roomData = {}
        self.serverAddress = (self.host, self.port)



    def receiveData(self):

        while True:
            data, _ = self.client.recvfrom(1024)
            data = data.decode('utf-8')

            
            if data.startswith("roomUpdate"):
                dataParts = data.split(';')
                roomCode = dataParts[1]

                players = {}
                for playerInfo in dataParts[2:]:
                    playerDetails = playerInfo.split(',')
                    playerId = playerDetails[0]
                    players[playerId] = {
                        'name': playerDetails[1],
                        'positionX': int(playerDetails[2]),
                        'positionY': int(playerDetails[3])
                    }
                self.roomData = {'roomCode': roomCode, 'players': players}
            


                

    def startReceiving(self):
        receiveThread = threading.Thread(target=self.receiveData)
        receiveThread.start()


                             
    def sendData(self, data):
        self.client.sendto(f'{self.clientID};{data}'.encode('utf-8'), self.serverAddress)

